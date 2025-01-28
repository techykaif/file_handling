
# File Organizer Script

A Python-based automation script that organizes files in a directory into categorized subfolders based on their file types. This script is designed to save time and keep your workspace clean and organized.

## Features
- **File Categorization**: Automatically sorts files into predefined categories such as Documents, Images, Videos, Code, etc.
- **Duplicate Detection**: Identifies duplicate files using MD5 hash and prevents redundancy.
- **Error Handling**: Logs errors in an `errors.txt` file for troubleshooting.
- **Action Logging**: Records all file movements in a `logs.txt` file.
- **Empty Folder Cleanup**: Moves empty folders to a `Clean_Up` directory for better organization.

## File Categories
The script organizes files into the following categories:
- Documents (`.pdf`, `.docx`, `.txt`)
- Images (`.jpg`, `.jpeg`, `.png`, `.gif`)
- Videos (`.mp4`, `.mkv`, `.avi`)
- Audio (`.mp3`, `.wav`)
- Archives (`.zip`, `.rar`, `.7z`)
- Executables (`.exe`, `.msi`)
- Python Scripts (`.py`)
- Applications (`.app`)
- Web Pages (`.html`, `.xml`)
- Spreadsheets (`.xls`, `.xlsx`)
- Presentations (`.ppt`, `.pptx`)
- Code (`.cpp`, `.java`, `.c`)
- Others (uncategorized files)

## How It Works
1. The script scans the specified directory.
2. Files are moved to corresponding subfolders based on their extensions.
3. Duplicate files are detected using MD5 hash, and their names are modified to avoid overwriting.
4. Logs of successful actions and errors are saved in `logs.txt` and `errors.txt`, respectively.
5. Empty folders are moved to a `Clean_Up` directory.

## Prerequisites
- Python 3.6 or higher
- Required libraries: `os`, `shutil`, `datetime`, `hashlib`

## Setup and Usage
1. Clone the repository or download the script
```bash
git clone https://github.com/techykaif/file_handling
cd file_handling
```
2. Set the `directory` variable in the script to the path of the directory you want to organize.
3. Run the script:
   ```bash
   python file_organizer.py
   ```
4. Check the `logs.txt` and `errors.txt` files for details about the operation.

## Example Output
After running the script, your directory structure might look like this:

```
/Documents
   - example.pdf
/Images
   - photo.jpg
/Videos
   - video.mp4
/Others
   - uncategorized_file.xyz
/logs.txt
/errors.txt
```

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request with suggestions or improvements.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any queries or feedback, feel free to reach out:
- **Name**: Mohd Kaif Ansari
- **LinkedIn**: [Connect with me on LinkedIn](https://www.linkedin.com/in/mohd-kaif-ansari-0754522bb/)

Feel free to customize the contact section and add any other details you find relevant! 😊
