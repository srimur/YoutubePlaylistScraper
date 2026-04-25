"""Tests for the Notion API exporter.

We don't hit Notion in tests — that'd need a real token and a sacrificial
page. Instead we mock ``requests.Session`` and verify the exporter's *shape*:
which endpoints it hits, when it stops, and how progress + ordering work.
"""

from __future__ import annotations

from datetime import datetime, timezone
from unittest.mock import MagicMock

import pytest
import requests as _req

from playlistpipe.core.models import Playlist, Video
from playlistpipe.exporters.notion_api import (
    NotionApiExporter,
    NotionConfig,
    NotionError,
)


def _video(i: int, title: str = "T") -> Video:
    return Video(
        video_id=f"vid{i:02d}AbCdEf"[:11],
        title=title,
        url=f"https://youtu.be/vid{i:02d}",
        channel="Chan",
        duration_seconds=120,
        position=i,
    )


def _playlist(videos):
    return Playlist(
        title="Test Playlist",
        url="https://www.youtube.com/playlist?list=ABC",
        channel="Chan",
        videos=tuple(videos),
        scraped_at=datetime(2026, 4, 1, tzinfo=timezone.utc),
    )


def _exporter(*, parent: str | None = "p" * 32, database: str | None = None):
    cfg = NotionConfig(
        token="secret_test_token_xyz",
        parent_page_id=parent,
        database_id=database,
    )
    session = MagicMock()
    # The constructor calls .headers.update — make that a no-op-friendly mock.
    session.headers = {}
    return NotionApiExporter(cfg, session=session), session


class TestValidateAccess:
    def test_calls_pages_endpoint_for_parent_page_setup(self):
        exp, session = _exporter()
        ok = MagicMock()
        ok.ok = True
        session.get.return_value = ok

        exp.validate_access()

        url = session.get.call_args[0][0]
        assert "/pages/" in url
        assert "p" * 32 in url

    def test_calls_databases_endpoint_when_database_id_set(self):
        exp, session = _exporter(parent=None, database="d" * 32)
        ok = MagicMock()
        ok.ok = True
        session.get.return_value = ok

        exp.validate_access()

        url = session.get.call_args[0][0]
        assert "/databases/" in url

    def test_raises_NotionError_on_404(self):
        exp, session = _exporter()
        resp = MagicMock()
        resp.ok = False
        resp.status_code = 404
        resp.json.return_value = {"message": "Could not find page with ID..."}
        session.get.return_value = resp

        with pytest.raises(NotionError) as ei:
            exp.validate_access()
        assert "404" in str(ei.value)

    def test_raises_NotionError_on_network_failure(self):
        exp, session = _exporter()
        session.get.side_effect = _req.RequestException("conn reset")

        with pytest.raises(NotionError):
            exp.validate_access()


class TestProgressAndOrdering:
    def _wire_session(self, session):
        """Make every API call return a generic 'ok' JSON body."""
        resp = MagicMock()
        resp.ok = True
        resp.json.return_value = {
            "id": "fake-db-id",
            "results": [],
            "has_more": False,
        }
        session.request.return_value = resp

    def test_progress_callback_fires_once_per_video(self, monkeypatch):
        # Skip the per-row pacing sleep so the test stays fast.
        monkeypatch.setattr(
            "playlistpipe.exporters.notion_api.time.sleep", lambda _s: None,
        )

        exp, session = _exporter(database="d" * 32)
        self._wire_session(session)

        playlist = _playlist([_video(i) for i in range(1, 6)])

        seen: list[tuple[int, int, int]] = []

        def cb(done, total, v):
            seen.append((done, total, v.position))

        exp.export(playlist, progress_cb=cb)

        # 5 videos → 5 progress events
        assert [s[0] for s in seen] == [1, 2, 3, 4, 5]
        assert all(s[1] == 5 for s in seen)

    def test_videos_are_inserted_in_reverse_position_order(self, monkeypatch):
        """Notion's default view sorts by creation time, newest first.

        We rely on this by inserting in reverse — position 5 first, position 1
        last — so the user's default view reads 1 → N. This test pins that
        behavior so a future "clean up the loop" doesn't silently regress it.
        """
        monkeypatch.setattr(
            "playlistpipe.exporters.notion_api.time.sleep", lambda _s: None,
        )

        exp, session = _exporter(database="d" * 32)
        self._wire_session(session)

        playlist = _playlist([_video(i) for i in range(1, 6)])

        seen_positions: list[int] = []

        def cb(_done, _total, v):
            seen_positions.append(v.position)

        exp.export(playlist, progress_cb=cb)

        # Reversed: 5, 4, 3, 2, 1
        assert seen_positions == [5, 4, 3, 2, 1]
