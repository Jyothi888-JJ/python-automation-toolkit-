import yt_dlp

def download_latest_videos(feed_url, output_folder, count=5):
    ydl_opts = {
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
        'playlistend': count
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([feed_url])
        print("Downloaded latest videos successfully.")

feed_url = "https://www.youtube.com/feeds/videos.xml?channel_id=YOUR_CHANNEL_ID"
download_latest_videos(feed_url, "./backups", count=5)
