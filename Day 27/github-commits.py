import requests
import os
import json
from datetime import datetime

# Function to convert ISO 8601 date to epoch
def iso_to_epoch(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
    return int(dt.timestamp())

# Function to load the last fetched date (in epoch) from a checkpoint file
def load_checkpoint(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return int(file.read().strip())
    return None

# Function to save the last fetched date (in epoch) to a checkpoint file
def save_checkpoint(file_path, epoch):
    with open(file_path, 'w') as file:
        file.write(str(epoch))

# Function to fetch commits from the GitHub API
def fetch_commits(owner, repo, checkpoint_file, per_page=30, token=None):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}" if token else None
    }

    # Load the last fetched date (in epoch)
    last_fetched_epoch = load_checkpoint(checkpoint_file)
    params = {"per_page": per_page}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        commits = response.json()

        if commits:
            # Process commits
            last_fetched_epoch_temp = last_fetched_epoch
            for commit in commits:
                commit_date = commit['commit']['author']['date']
                commit_date_epoch = iso_to_epoch(commit_date)
                if last_fetched_epoch is None or commit_date_epoch > last_fetched_epoch:
                    print(json.dumps(commit))
                    if last_fetched_epoch_temp is None or last_fetched_epoch_temp < commit_date_epoch:
                        last_fetched_epoch_temp = commit_date_epoch
                    
            save_checkpoint(checkpoint_file, last_fetched_epoch_temp)
        else:
            print("No new commits found.")
    else:
        print(f"Error: Unable to fetch commits. Status code: {response.status_code}, Message: {response.text}")

# Configuration
OWNER = "OWNER_NAME"  # Replace with the repository owner
REPO = "REPO_NAME"    # Replace with the repository name
CHECKPOINT_FILE = "/opt/splunk/etc/apps/search/bin/checkpoint.txt"  # Path to checkpoint file
GITHUB_TOKEN = "GTIHUB_TOKEN"  # Replace with your GitHub token

# Fetch commits
fetch_commits(OWNER, REPO, CHECKPOINT_FILE, token=GITHUB_TOKEN)
