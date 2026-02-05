# GitHub Profile README Automation

This repository contains an automated system to keep the profile README.md updated with the latest GitHub statistics.

## Features

- **Automatic Updates**: The README is automatically updated daily with fresh statistics
- **GitHub Statistics**: Displays total repositories, gists, followers, and following count
- **Top Repositories**: Shows your top 5 repositories sorted by stars
- **Recent Activity**: Lists your 5 most recently updated repositories
- **Manual Trigger**: Can be manually triggered via GitHub Actions

## How It Works

The automation consists of three main components:

### 1. GitHub Actions Workflow (`.github/workflows/update-readme.yml`)

- Runs daily at midnight UTC (configurable via cron schedule)
- Can be manually triggered via the Actions tab
- Automatically runs on pushes to the main branch

### 2. Python Script (`update_readme.py`)

- Fetches data from the GitHub API using PyGithub
- Retrieves user statistics and repository information
- Formats the data into markdown
- Updates the README.md file

### 3. README.md

The main profile README that gets automatically updated with:
- GitHub statistics
- Top repositories by stars
- Recently updated repositories
- Last update timestamp

## Setup Instructions

1. **Fork or use this repository**: The repository must be named `<username>/<username>` to appear on your GitHub profile

2. **Enable GitHub Actions**: Go to the Actions tab and enable workflows

3. **Manual Trigger (Optional)**: 
   - Go to Actions → "Update README with GitHub Stats"
   - Click "Run workflow"

4. **Automatic Updates**: The workflow will run automatically every day at midnight UTC

## Customization

You can customize the automation by editing:

- **Schedule**: Modify the cron expression in `.github/workflows/update-readme.yml`
- **Number of repos**: Change `max_count` parameter in `update_readme.py`
- **README template**: Modify the format string in `update_readme.py`

## Requirements

- GitHub repository named `<username>/<username>`
- GitHub Actions enabled
- Python 3.10+
- PyGithub library

## License

This automation script is provided as-is for use in GitHub profile READMEs.
