# PRD-001: Self-Updating Profile README

## Overview
Create an automated GitHub profile README that dynamically updates content using GitHub Actions, inspired by Simon Willison's self-updating profile system.

## Key Concepts

### Repository Setup
- Create a public repository matching GitHub username: `shrwnsan/shrwnsan`
- GitHub automatically displays `README.md` from this repository at top of profile page
- Repository name must exactly match GitHub username

### Automation Architecture
- **GitHub Actions**: Trigger automated updates on schedule or events
- **Python Scripts**: Fetch data from various APIs (GitHub GraphQL, RSS feeds, etc.)
- **Comment Markers**: HTML comments in README delimiting dynamic content sections
- **Content Replacement**: Scripts update content between markers while preserving rest of README

### Implementation Pattern
```markdown
<!--START_SECTION:projects-->
Dynamic content here
<!--END_SECTION:projects-->
```

## Requirements

### Functional Requirements
1. **Dynamic Research Section**: Display recent 5 posts from `https://github.com/shrwnsan/research/`
2. **WIP Section**: Manual updates for current projects (Search-Plus plugin featured)
3. **Automated Updates**: Schedule regular content refresh without manual intervention
4. **Fallback Handling**: Graceful degradation if data sources are unavailable

### Technical Requirements
1. **GitHub Actions Workflow**: Trigger automation (schedule: daily, manual: workflow dispatch)
2. **Python Data Fetcher**: Interface with GitHub API to retrieve repository data
3. **Template System**: Preserve manual content while updating dynamic sections
4. **Error Handling**: Log failures and maintain last known good state

### Non-Functional Requirements
1. **Performance**: Complete updates within 2-3 minutes
2. **Reliability**: 99%+ successful update rate
3. **Maintainability**: Clear separation between manual and automated content
4. **Security**: Use GitHub's built-in secrets for API tokens

## Success Criteria
- ✅ README updates automatically without breaking manual content
- ✅ Research section displays accurate recent posts from repository
- ⏳ Updates run reliably on schedule (pending GitHub deployment)
- ✅ Clean commit history with meaningful messages
- ✅ Zero downtime or broken README states

## Dependencies
- GitHub repository `shrwnsan/shrwnsan` (public)
- GitHub Actions (free tier sufficient)
- GitHub API for repository data access
- Python 3.x runtime in Actions

## Risks & Mitigations
- **API Rate Limits**: Implement caching and respect GitHub API limits
- **Merge Conflicts**: Use force pushes for automated updates
- **Data Source Changes**: Build flexible parsing for repository structure changes
- **Workflow Failures**: Implement error notifications and retry logic

## Implementation Status: ✅ COMPLETE

### Completion Date
**November 7, 2025** - Successfully implemented all core requirements

### Implementation Highlights
- **Workflow Automation**: GitHub Actions with daily and manual triggers
- **API Integration**: Python script successfully fetches from `shrwnsan/research` issues
- **Content Safety**: HTML comment markers preserve manual content
- **Professional Standards**: Conventional commits with proper attribution
- **Error Handling**: Graceful fallback when repository has no issues/posts

### Lessons Learned
1. **Virtual Environment Critical**: Python dependencies require `.venv` for local testing
2. **Git Automation**: `[skip ci]` flag prevents workflow loops when auto-committing
3. **API Rate Limits**: Current implementation respects GitHub limits with minimal calls
4. **Comment Marker Precision**: Exact marker matching prevents content corruption
5. **Requirements.txt**: Essential for reproducible Python environments in Actions

### Technical Implementation Notes
- Uses `requests` library for GitHub API calls (more reliable than urllib)
- Regex-based content replacement with `re.DOTALL` flag for multi-line sections
- Python 3.9 compatibility for GitHub Actions environment
- Proper Git configuration for automated commits

## Future Enhancements
- Additional dynamic sections (blog posts, project releases)
- Multiple data sources (RSS feeds, external APIs)
- Content formatting improvements
- Analytics and tracking for profile visits