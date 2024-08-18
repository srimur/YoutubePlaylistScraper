import pyperclip

def output_notion(videos):
    """Format video details for Notion checklist with hyperlinks and copy to clipboard."""
    markdown_content = ""
    for video in videos:
        title = video['title']
        url = video['url']
        markdown_content += f"- [ ] [{title}]({url})\n"
    
    print(markdown_content)

    # Copy the output to the clipboard
    pyperclip.copy(markdown_content)
    print("\n✅ Notion checklist with hyperlinks has been copied to the clipboard!")
