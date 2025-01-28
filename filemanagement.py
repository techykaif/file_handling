import os
import shutil
from datetime import datetime
import hashlib

# Define the directory to organize
directory = os.getcwd()  # Use the current working directory

# Define file types and their extensions
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
    'Others': []  # Uncategorized files
}

# A dictionary to track file hashes for duplicates
file_hashes = {}

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

def organize_files(directory):
    """Organize files in the given directory."""
    try:
        if not os.path.exists(directory):
            print(f"Error: The directory '{directory}' does not exist.")
            return
        
        # Create folders for categories and logs
        for folder in file_types.keys():
            os.makedirs(os.path.join(directory, folder), exist_ok=True)
        cleanup_folder = os.path.join(directory, 'Clean_Up')
        os.makedirs(cleanup_folder, exist_ok=True)

        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            
            # Skip directories
            if os.path.isdir(file_path) or file.startswith('.'):
                continue
            
            # Check for duplicate files
            file_hash = calculate_hash(file_path)
            if file_hash and file_hash in file_hashes:
                print(f"Duplicate file skipped: {file}")
                log_action(directory, f"Duplicate file skipped: {file}")
                continue
            elif file_hash:
                file_hashes[file_hash] = file
            
            # Categorize the file
            moved = False
            for folder, extensions in file_types.items():
                if any(file.lower().endswith(ext) for ext in extensions):
                    destination_folder = os.path.join(directory, folder)
                    move_file(file_path, destination_folder)
                    moved = True
                    break
            
            # Move uncategorized files to 'Others'
            if not moved:
                others_folder = os.path.join(directory, 'Others')
                move_file(file_path, others_folder)
        
        # Move empty folders to 'Clean_Up'
        for folder in file_types.keys():
            folder_path = os.path.join(directory, folder)
            if os.path.isdir(folder_path) and not os.listdir(folder_path):
                shutil.move(folder_path, os.path.join(cleanup_folder, folder))
                print(f"Moved empty folder '{folder}' to 'Clean_Up'")
                log_action(directory, f"Moved empty folder '{folder}' to 'Clean_Up'")

        print("File organization completed.")

    except Exception as e:
        log_error(directory, f"General error: {str(e)}")

def move_file(source, destination_folder):
    """Move a file to a destination folder."""
    os.makedirs(destination_folder, exist_ok=True)
    destination_path = os.path.join(destination_folder, os.path.basename(source))
    
    # Handle duplicate names
    if os.path.exists(destination_path):
        base, ext = os.path.splitext(os.path.basename(source))
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        new_name = f"{base}_{timestamp}{ext}"
        destination_path = os.path.join(destination_folder, new_name)
        print(f"File already exists. Renaming to: {new_name}")
    
    try:
        shutil.move(source, destination_path)
        log_action(directory, f"Moved {source} to {destination_path}")
    except Exception as e:
        log_error(directory, f"Failed to move {source}: {str(e)}")

def log_action(directory, message):
    """Log an action to a file."""
    with open(os.path.join(directory, 'logs.txt'), 'a') as log_file:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_file.write(f"[{timestamp}] {message}\n")

def log_error(directory, message):
    """Log an error to a file."""
    with open(os.path.join(directory, 'errors.txt'), 'a') as error_file:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        error_file.write(f"[{timestamp}] {message}\n")

# Run the organizer
organize_files(directory)
