# Tasks-001: Self-Updating Profile README Implementation

## Overview
Breakdown of implementation tasks for junior developers to complete in parallel. Each task is independent, testable, and estimated for quick completion.

## Phase 1: Repository Setup (15 minutes)

### Task 1.1: Initialize Git Repository
- **File**: `./` (root)
- **Action**: `git init` and initial commit
- **Outcome**: Repository ready for GitHub push
- **Test**: `git status` shows clean state
- **Dependencies**: None

### Task 1.2: Create GitHub Repository
- **File**: GitHub.com
- **Action**: Create `shrwnsan/shrwnsan` public repository
- **Outcome**: Remote repository exists
- **Test**: Repository accessible at https://github.com/shrwnsan/shrwnsan
- **Dependencies**: Task 1.1

### Task 1.3: Push Initial Content
- **File**: Remote repository
- **Action**: Push LICENSE and README.md to GitHub
- **Outcome**: Base files deployed
- **Test**: Files visible in repository
- **Dependencies**: Task 1.1, 1.2

## Phase 2: GitHub Actions Infrastructure (30 minutes)

### Task 2.1: Create Workflow Directory
- **File**: `.github/workflows/`
- **Action**: Create directory structure
- **Outcome**: Workflow directory exists
- **Test**: `ls -la .github/workflows/` shows empty directory
- **Dependencies**: Task 1.3

### Task 2.2: Base Workflow Configuration
- **File**: `.github/workflows/update-readme.yml`
- **Action**: Create basic GitHub Actions workflow
- **Template**:
```yaml
name: Update README
on:
  schedule:
    - cron: '0 0 * * *'  # Daily at midnight UTC
  workflow_dispatch:  # Manual trigger
jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
```
- **Outcome**: Workflow file created with basic structure
- **Test**: YAML validates successfully
- **Dependencies**: Task 2.1

### Task 2.3: Python Environment Setup
- **File**: `.github/workflows/update-readme.yml`
- **Action**: Add Python dependencies and script execution
- **Add to workflow**:
```yaml
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install requests PyYAML
      - name: Update README
        run: python scripts/update_readme.py
```
- **Outcome**: Python environment configured in workflow
- **Test**: Workflow steps syntactically correct
- **Dependencies**: Task 2.2

## Phase 3: Data Fetching Script (45 minutes)

### Task 3.1: Create Scripts Directory
- **File**: `scripts/`
- **Action**: Create directory for Python scripts
- **Outcome**: Scripts directory exists
- **Test**: Directory created and empty
- **Dependencies**: Task 1.3

### Task 3.2: Basic Script Structure
- **File**: `scripts/update_readme.py`
- **Action**: Create main Python script with basic structure
- **Template**:
```python
#!/usr/bin/env python3
import os
import re
import requests
from pathlib import Path

def update_readme():
    """Main function to update README with dynamic content"""
    readme_path = Path("README.md")

    # Read current README
    with open(readme_path, 'r') as f:
        content = f.read()

    # Update sections will go here

    # Write updated README
    with open(readme_path, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    update_readme()
```
- **Outcome**: Basic script structure created
- **Test**: Script runs without errors
- **Dependencies**: Task 3.1

### Task 3.3: GitHub API Integration
- **File**: `scripts/update_readme.py`
- **Action**: Add function to fetch repository data
- **Add function**:
```python
def get_research_posts():
    """Fetch recent posts from research repository"""
    url = "https://api.github.com/repos/shrwnsan/research/issues"
    params = {"state": "open", "sort": "created", "direction": "desc", "per_page": 5}
    response = requests.get(url, params=params)
    return response.json() if response.status_code == 200 else []
```
- **Outcome**: GitHub API integration working
- **Test**: Function returns list of issues/research posts
- **Dependencies**: Task 3.2

### Task 3.4: Content Template Generation
- **File**: `scripts/update_readme.py`
- **Action**: Add function to generate markdown from API data
- **Add function**:
```python
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
```
- **Outcome**: Markdown formatting working
- **Test**: Function produces valid markdown output
- **Dependencies**: Task 3.3

## Phase 4: README Update Logic (30 minutes)

### Task 4.1: Add Comment Markers
- **File**: `README.md`
- **Action**: Add markers around Researching section
- **Update**:
```markdown
**Researching:**
<!--START_SECTION:research-->
* {Recent 5 posts from https://github.com/shrwnsan/research/}
<!--END_SECTION:research-->
```
- **Outcome**: Dynamic section marked with comments
- **Test**: Markers visible in README
- **Dependencies**: Task 1.3

### Task 4.2: Content Replacement Logic
- **File**: `scripts/update_readme.py`
- **Action**: Add function to replace content between markers
- **Add function**:
```python
def replace_section(content, section_name, new_content):
    """Replace content between START and END markers"""
    pattern = rf'<!--START_SECTION:{section_name}-->(.*?)<!--END_SECTION:{section_name}-->'
    replacement = f'<!--START_SECTION:{section_name}-->\n{new_content}\n<!--END_SECTION:{section_name}-->'
    return re.sub(pattern, replacement, content, flags=re.DOTALL)
```
- **Outcome**: Content replacement logic implemented
- **Test**: Function correctly replaces marked sections
- **Dependencies**: Task 4.1

### Task 4.3: Integration in Main Script
- **File**: `scripts/update_readme.py`
- **Action**: Wire all functions together in main execution
- **Update main function**:
```python
def update_readme():
    readme_path = Path("README.md")

    with open(readme_path, 'r') as f:
        content = f.read()

    # Fetch and format research posts
    posts = get_research_posts()
    formatted_posts = format_research_posts(posts)

    # Update README
    content = replace_section(content, "research", formatted_posts)

    with open(readme_path, 'w') as f:
        f.write(content)
```
- **Outcome**: Complete integration working
- **Test**: Script runs and updates README
- **Dependencies**: Tasks 3.4, 4.2

## Phase 5: Git Automation (20 minutes)

### Task 5.1: Add Git Operations to Workflow
- **File**: `.github/workflows/update-readme.yml`
- **Action**: Add git configuration and commit steps
- **Add to workflow**:
```yaml
      - name: Commit and push changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add README.md
          git diff --staged --quiet || git commit -m "Auto-update README [skip ci]"
          git push
```
- **Outcome**: Git automation added to workflow
- **Test**: Workflow steps syntactically correct
- **Dependencies**: Task 2.3

### Task 5.2: Test Complete Workflow
- **File**: GitHub repository
- **Action**: Trigger workflow manually and verify results
- **Outcome**: Complete end-to-end automation working
- **Test**: README updates with research posts
- **Dependencies**: All previous tasks

## Parallel Execution Plan

### Can be done simultaneously:
- Tasks 1.1, 2.1, 3.1 (directory setup)
- Tasks 2.2, 3.2 (basic file creation)
- Tasks 2.3, 3.3, 4.1 (dependencies and API setup)
- Tasks 3.4, 4.2, 5.1 (advanced features)

### Required sequence:
- Phase 1 → Phase 2 → Phase 3 → Phase 4 → Phase 5

### Total estimated time: 2 hours 20 minutes
- **Junior dev (parallel work)**: 45-60 minutes
- **Single dev (sequential)**: 2 hours 20 minutes

## Success Metrics
- [ ] README updates automatically when workflow runs
- [ ] Research section shows recent posts
- [ ] Manual content (WIP section) remains unchanged
- [ ] Commits are clean with descriptive messages
- [ ] No merge conflicts or broken states