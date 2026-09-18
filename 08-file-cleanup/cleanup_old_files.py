import os
import time

def cleanup_old_files(directory, days_old):
    current_time = time.time()
    seconds_old = days_old * 86400

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_age = current_time - os.path.getmtime(file_path)
            if file_age > seconds_old:
                os.remove(file_path)
                print(f"Deleted {filename} (older than {days_old} days)")

target_dir = r"C:\path\to\folder"
cleanup_old_files(target_dir, 30)
