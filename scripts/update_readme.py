#!/usr/bin/env python3
import os
import re
import requests
import feedparser
from pathlib import Path

def get_research_posts():
    """Fetch recent Jekyll posts from research blog using Atom feed"""
    feed_url = "https://shrwnsan.github.io/research/feed.xml"

    try:
        feed = feedparser.parse(feed_url)
        entries = feed["entries"][:5]  # Get only 5 most recent

        posts = []
        for entry in entries:
            posts.append({
                "title": entry["title"],
                "url": entry["link"].split("#")[0],  # Remove anchor if present
                "published": entry["published"].split("T")[0] if entry.get("published") else ""
            })

        return posts

    except Exception as e:
        print(f"Error fetching research feed: {e}")
        return []

def format_research_posts(posts):
    """Format research posts as markdown"""
    if not posts:
        return "* No recent research posts"

    formatted = []
    for post in posts[:5]:
        title = post.get('title', 'Untitled')
        url = post.get('url', '#')
        published = post.get('published', '')

        if published:
            formatted.append(f"* [{title}]({url}) - {published}")
        else:
            formatted.append(f"* [{title}]({url})")

    return "\n".join(formatted)

def replace_section(content, section_name, new_content):
    """Replace content between START and END markers"""
    pattern = rf'<!--START_SECTION:{section_name}-->(.*?)<!--END_SECTION:{section_name}-->'
    replacement = f'<!--START_SECTION:{section_name}-->\n{new_content}\n<!--END_SECTION:{section_name}-->'
    return re.sub(pattern, replacement, content, flags=re.DOTALL)

def update_readme():
    """Main function to update README with dynamic content"""
    readme_path = Path("README.md")

    # Read current README
    with open(readme_path, 'r') as f:
        content = f.read()

    # Fetch and format research posts
    posts = get_research_posts()
    formatted_posts = format_research_posts(posts)

    # Update README
    content = replace_section(content, "research", formatted_posts)

    # Write updated README
    with open(readme_path, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    update_readme()