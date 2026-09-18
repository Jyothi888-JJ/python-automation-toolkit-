# Automated Zip Folder Backup Script

This project demonstrates a simple **Python backup automation script** that compresses a selected folder into a timestamped `.zip` archive and stores it in a specified backup directory.

The script can also be scheduled to run automatically using **Windows Task Scheduler**.

## What This Script Does

1. Selects a source folder to back up.
2. Generates a timestamp for the backup.
3. Compresses the source folder into a `.zip` file.
4. Saves the backup in the specified backup directory.
5. Prints the location of the created backup.

## Example Backup Name

```text
backup_20260918_183000.zip
```

Each backup gets a unique timestamp-based filename.

## Technologies Used

* Python
* `os` module
* `shutil` module
* `datetime` module
* Windows Task Scheduler

## How It Works

```text id="3u7j5p"
Source Folder
      ↓
Generate Timestamp
      ↓
Create ZIP Archive
      ↓
Save to Backup Folder
      ↓
Backup Completed
```

## Setup

### 1. Update the Folder Paths

Change:

```python id="3y8e1q"
source_folder = "/path/to/source_folder"
backup_folder = "/path/to/backup_folder"
```

to the folders you want to use.

For example:

```python id="8u9h4n"
source_folder = "C:/Users/User/Documents"
backup_folder = "D:/Backups"
```

### 2. Run the Script

```bash id="q0k9as"
python backup.py
```

## Example Output

```text id="0j6h9r"
Backup created successfully at D:/Backups/backup_20260918_183000.zip
```

## Scheduling with Windows Task Scheduler

The script can be configured in **Windows Task Scheduler** to run automatically at a specific time or interval.

For example:

```text
Daily → Run backup.py → Create timestamped ZIP backup
```

## Purpose

This project demonstrates how **Python can automate file backups and archiving**, while Windows Task Scheduler can be used to run the backup process automatically.
