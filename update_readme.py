#!/usr/bin/env python3
"""
Script to update README.md with GitHub stats including:
- Public repositories
- Top repositories by stars
- Contribution statistics
"""

import os
import sys
from github import Github
from datetime import datetime

def format_repo_list(repos, max_count=10):
    """Format repository list as markdown."""
    lines = []
    for i, repo in enumerate(repos[:max_count], 1):
        stars = repo.stargazers_count
        forks = repo.forks_count
        description = repo.description or "No description"
        lines.append(f"{i}. **[{repo.name}]({repo.html_url})** - {description} ⭐ {stars} 🍴 {forks}")
    return "\n".join(lines) if lines else "*No repositories found*"

def get_contribution_stats(g, username):
    """Get contribution statistics."""
    user = g.get_user(username)
    total_repos = user.public_repos
    total_gists = user.public_gists
    followers = user.followers
    following = user.following
    
    return {
        'total_repos': total_repos,
        'total_gists': total_gists,
        'followers': followers,
        'following': following
    }

def main():
    # Get GitHub token and username from environment
    token = os.environ.get('GITHUB_TOKEN')
    username = os.environ.get('GITHUB_USERNAME')
    
    if not token:
        print("Error: GITHUB_TOKEN environment variable not set")
        sys.exit(1)
    
    if not username:
        print("Error: GITHUB_USERNAME environment variable not set")
        sys.exit(1)
    
    try:
        # Initialize GitHub API client
        g = Github(token)
        user = g.get_user(username)
        
        # Get all public repositories
        repos = list(user.get_repos(type='public', sort='updated'))
        
        # Get top repositories by stars
        top_repos = sorted(repos, key=lambda r: r.stargazers_count, reverse=True)
        
        # Get contribution stats
        stats = get_contribution_stats(g, username)
        
        # Build new content
        new_content = f"""## Hi there 👋

I'm {user.name or username}, a passionate developer working on exciting projects!

### 📊 GitHub Statistics

- 📁 **Public Repositories:** {stats['total_repos']}
- 📝 **Public Gists:** {stats['total_gists']}
- 👥 **Followers:** {stats['followers']}
- 🤝 **Following:** {stats['following']}

### 🌟 Top Repositories by Stars

{format_repo_list(top_repos, max_count=5)}

### 📚 Recently Updated Repositories

{format_repo_list(repos, max_count=5)}

### 🔗 Connect with me

- GitHub: [@{username}](https://github.com/{username})

---

*Last updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC*

<!--
**{username}/{username}** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.
-->
"""
        
        # Write updated README
        with open('README.md', 'w') as f:
            f.write(new_content)
        
        print("README.md updated successfully!")
        print(f"Total repositories: {stats['total_repos']}")
        print(f"Top repository: {top_repos[0].name if top_repos else 'None'} ({top_repos[0].stargazers_count if top_repos else 0} stars)")
    
    except Exception as e:
        print(f"Error updating README: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
