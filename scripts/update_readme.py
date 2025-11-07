#!/usr/bin/env python3
import os
import re
import requests
from pathlib import Path

def get_research_posts():
    """Fetch recent posts from research repository"""
    url = "https://api.github.com/repos/shrwnsan/research/issues"
    params = {"state": "open", "sort": "created", "direction": "desc", "per_page": 5}
    response = requests.get(url, params=params)
    return response.json() if response.status_code == 200 else []

def format_research_posts(posts):
    """Format research posts as markdown"""
    if not posts:
        return "* No recent research posts"

    formatted = []
    for post in posts[:5]:
        title = post.get('title', 'Untitled')
        url = post.get('html_url', '#')
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