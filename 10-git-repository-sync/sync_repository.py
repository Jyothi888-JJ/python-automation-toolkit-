import os
import subprocess

def sync_repository(repo_url, repo_dir):
    if not os.path.exists(repo_dir):
        print(f"Cloning {repo_url}...")
        subprocess.run(["git", "clone", repo_url, repo_dir])
    else:
        print(f"Updating repository in {repo_dir}...")
        subprocess.run(["git", "-C", repo_dir, "pull"])

repo_url = "https://github.com/example/repo.git"
local_dir = "/path/to/local/repo"
sync_repository(repo_url, local_dir)
