# Automated Bulk Git Repository Synchronization

This project demonstrates a simple **Python automation script** that keeps a local Git repository synchronized with a remote repository.

If the local repository does not exist, the script clones it. If it already exists, the script runs `git pull` to get the latest changes.

## What This Script Does

1. Checks whether the local repository directory exists.
2. If it does not exist, clones the remote repository.
3. If it already exists, runs `git pull`.
4. Keeps the local repository updated with the remote repository.

## Technologies Used

* Python
* Git
* `os` module
* `subprocess` module

## How It Works

```text id="f6q3nz"
Remote Git Repository
        ↓
Check Local Directory
        ↓
   Does it exist?
     ↙       ↘
   No         Yes
    ↓           ↓
 Git Clone   Git Pull
    ↓           ↓
 Local Repository Updated
```

## Setup

### 1. Configure the Repository URL

Update:

```python id="7s3xqp"
repo_url = "https://github.com/example/repo.git"
```

with the Git repository you want to synchronize.

### 2. Configure the Local Directory

Update:

```python id="x4n7cv"
local_dir = "/path/to/local/repo"
```

with the location where you want the repository to be stored.

### 3. Make Sure Git Is Installed

Verify Git is available:

```bash id="p8d2km"
git --version
```

### 4. Run the Script

```bash id="m5v1rq"
python git_sync.py
```

## Example Output

### Repository Does Not Exist

```text id="r2k8lw"
Cloning https://github.com/example/repo.git...
```

### Repository Already Exists

```text id="n6t3qa"
Updating repository in /path/to/local/repo...
```

## Purpose

This project demonstrates how **Python can automate common Git operations** and reduce the manual effort required to keep local repositories synchronized with remote repositories.
