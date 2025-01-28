import os
import shutil
from datetime import datetime
import hashlib

directory = "/Users/kaif/Desktop/Automation/File_Handling"

file_types = {
    'Documents': ['.pdf', '.docx', '.txt'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Audio': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar', '.7z'],
    'Executables': ['.exe', '.msi'],
    'Python Scripts': ['.py'],
    'Applications': ['.app'],
    'Web Pages': ['.html', '.xml'],
    'Spreadsheets': ['.xls', '.xlsx'],
    'Presentations': ['.ppt', '.pptx'],
    'Code': ['.cpp', '.java', '.c'],
    'Others': []  # For uncategorized files
}

def calculate_hash(file_path):
    """Calculate the MD5 hash of a file."""
    try:
        hash_algo = hashlib.md5()
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hash_algo.update(chunk)
        return hash_algo.hexdigest()
    except Exception as e:
        print(f"Error calculating hash for {file_path}: {e}")
        return None

file_hashes = {}

def organize_files(directory):
    """Organize files in the given directory based on their types."""
    try:
        if not os.path.exists(directory):
            print(f"Error: The directory '{directory}' does not exist.")
            return
        
        print(f"Organizing files in directory: {directory}")
        
        # Create subdirectories for file categories
        for folder in file_types.keys():
            folder_path = os.path.join(directory, folder)
            os.makedirs(folder_path, exist_ok=True)
        
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            
            # Skip subdirectories
            if os.path.isdir(file_path):
                print(f"Skipping directory: {file_path}")
                continue
            
            # Check for duplicate files
            file_hash = calculate_hash(file_path)
            if file_hash is None:
                continue  # Skip if hash couldn't be calculated
            
            if file_hash in file_hashes:
                print(f"Duplicate detected: {file} and {file_hashes[file_hash]}")
                continue
            else:
                file_hashes[file_hash] = file
            
            # Check for existing file in destination folder to avoid overwriting
            moved = False
            for folder, extensions in file_types.items():
                if any(file.endswith(ext) for ext in extensions):
                    folder_path = os.path.join(directory, folder)
                    destination_path = os.path.join(folder_path, file)
                    
                    # Check if file already exists in destination folder
                    if os.path.exists(destination_path):
                        new_name = f"{os.path.splitext(file)[0]}_duplicate{os.path.splitext(file)[1]}"
                        destination_path = os.path.join(folder_path, new_name)
                        print(f"File with the same name exists. Renamed to: {new_name}")
                    
                    try:
                        shutil.move(file_path, destination_path)
                        print(f"Moved {file} to {folder_path}")
                        with open(os.path.join(directory, 'logs.txt'), 'a') as log_file:
                            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            log_file.write(f"[{timestamp}] Moved {file} to {folder_path}\n")
                        moved = True
                    except Exception as e:
                        print(f"Failed to move {file}: {e}")
                        with open(os.path.join(directory, 'errors.txt'), 'a') as error_file:
                            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            error_file.write(f"[{timestamp}] Failed to move {file}: {str(e)}\n")
                    break
            
            # Move uncategorized files to 'Others'
            if not moved:
                folder_path = os.path.join(directory, 'Others')
                destination_path = os.path.join(folder_path, file)
                
                # Check if file exists in 'Others' folder
                if os.path.exists(destination_path):
                    new_name = f"{os.path.splitext(file)[0]}_duplicate{os.path.splitext(file)[1]}"
                    destination_path = os.path.join(folder_path, new_name)
                    print(f"File with the same name exists in 'Others'. Renamed to: {new_name}")
                
                try:
                    shutil.move(file_path, destination_path)
                    print(f"Moved {file} to 'Others'")
                    with open(os.path.join(directory, 'logs.txt'), 'a') as log_file:
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        log_file.write(f"[{timestamp}] Moved {file} to 'Others'\n")
                except Exception as e:
                    print(f"Failed to move {file} to 'Others': {e}")
                    with open(os.path.join(directory, 'errors.txt'), 'a') as error_file:
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        error_file.write(f"[{timestamp}] Failed to move {file} to 'Others': {str(e)}\n")
        
        # Clean up empty folders
        for folder in file_types.keys():
            folder_path = os.path.join(directory, folder)
            if not os.listdir(folder_path):  # Check if the folder is empty
                try:
                    shutil.move(folder_path, os.path.join(directory, 'Clean_Up', folder))
                    print(f"Moved empty folder '{folder}' to 'Clean_Up'")
                except Exception as e:
                    print(f"Failed to move empty folder '{folder}': {e}")

        print("Files have been organized successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
        with open(os.path.join(directory, 'errors.txt'), 'a') as error_file:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            error_file.write(f"[{timestamp}] Error: {str(e)}\n")

# Run the file organizer
organize_files(directory)
