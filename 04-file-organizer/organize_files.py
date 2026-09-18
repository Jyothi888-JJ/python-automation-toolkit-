import os
import shutil

def organize_files(folder_path):
    files = os.listdir(folder_path)
    
    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            if file.endswith('.pdf'):
                dest = os.path.join(folder_path, 'docs')
            elif file.endswith('.txt'):
                dest = os.path.join(folder_path, 'text')
            elif file.endswith('.jpg'):
                dest = os.path.join(folder_path, 'images')
            else:
                continue
                
            os.makedirs(dest, exist_ok=True)
            shutil.move(file_path, dest)
            print(f"Moved {file} to {dest}")

organize_files("/path/to/target_directory")
