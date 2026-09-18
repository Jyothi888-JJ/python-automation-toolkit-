# Cleanup Script for Files Older Than X Days

This project demonstrates a simple **Python cleanup automation script** that scans a directory and automatically deletes files that are older than a specified number of days.

## What This Script Does

1. Scans the specified directory.
2. Checks the modification time of each file.
3. Calculates how old each file is.
4. Compares the file age with the configured threshold.
5. Deletes files older than the specified number of days.
6. Prints a message for each deleted file.

## Example

If the cleanup period is set to **30 days**:

```text
Files newer than 30 days  → Keep
Files older than 30 days  → Delete
```

## Technologies Used

* Python
* `os` module
* `time` module

## How It Works

```text
Target Directory
      ↓
Scan Files
      ↓
Check Modification Time
      ↓
Calculate File Age
      ↓
Older Than X Days?
   ↙           ↘
 Yes            No
  ↓              ↓
Delete File    Keep File
```

## Setup

### 1. Set the Target Directory

Update:

```python
target_dir = r"C:\path\to\folder"
```

with the directory you want to clean.

### 2. Set the Cleanup Period

The current script deletes files older than **30 days**:

```python
cleanup_old_files(target_dir, 30)
```

You can change `30` to another number of days.

### 3. Run the Script

```bash
python cleanup_old_files.py
```

## Example Output

```text
Deleted old_report.pdf (older than 30 days)
Deleted temp_file.txt (older than 30 days)
```

## Purpose

This project demonstrates how **Python can automate routine file cleanup and storage-management tasks** by removing files that are no longer required.
