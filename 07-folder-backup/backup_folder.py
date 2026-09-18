import os
import shutil
import datetime

def backup_and_zip(source_dir, backup_dir):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_name = f"backup_{timestamp}"
    zip_path = os.path.join(backup_dir, zip_name)
    
    shutil.make_archive(zip_path, 'zip', source_dir)
    print(f"Backup created successfully at {zip_path}.zip")

source_folder = "/path/to/source_folder"
backup_folder = "/path/to/backup_folder"
backup_and_zip(source_folder, backup_folder)
