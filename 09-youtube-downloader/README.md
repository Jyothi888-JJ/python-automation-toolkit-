# YouTube Video Downloader via RSS Channel Feed

This project demonstrates a simple **Python automation script** that uses a YouTube Channel RSS feed and `yt_dlp` to download the latest videos from a channel into a local folder.

## What This Script Does

1. Uses a YouTube Channel RSS feed to identify videos.
2. Connects to the feed using `yt_dlp`.
3. Selects the latest videos based on the configured count.
4. Downloads the videos to a specified folder.
5. Saves each video using its original title.

## Technologies Used

* Python
* YouTube RSS Feed
* `yt_dlp`

## How It Works

```text id="j8h4qa"
YouTube Channel
      ↓
RSS Feed
      ↓
yt_dlp
      ↓
Find Latest Videos
      ↓
Download Videos
      ↓
Local Folder
```

## Setup

### 1. Install yt-dlp

```bash id="c1n6r8"
pip install yt-dlp
```

### 2. Add the YouTube Channel ID

Update:

```python id="h0r4fd"
feed_url = "https://www.youtube.com/feeds/videos.xml?channel_id=YOUR_CHANNEL_ID"
```

Replace `YOUR_CHANNEL_ID` with the channel ID you want to monitor.

### 3. Set the Download Folder

The current script saves videos to:

```python id="w3t6px"
"./backups"
```

You can change this to any local folder.

### 4. Set the Number of Videos

The script currently downloads the latest **5 videos**:

```python id="k7s2qa"
count=5
```

Change the number if required.

### 5. Run the Script

```bash id="e2v9lm"
python youtube_downloader.py
```

## Example Output

```text id="q6m8zt"
Downloaded latest videos successfully.
```

The downloaded videos will be stored in the configured output folder.

## Purpose

This project demonstrates **Python automation, RSS feed processing, and command-line media downloading** using `yt_dlp`.
