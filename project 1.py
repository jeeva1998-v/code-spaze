import os
import shutil
from datetime import datetime

# Define the path to the folder containing the files
directory_path = r'C:\path\to\your\directory'

# Get current date
date_stamp = datetime.now().strftime('%Y-%m-%d')

# File extensions and respective folders
file_categories = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif'],
    "Documents": ['.pdf', '.docx', '.txt'],
    "Spreadsheets": ['.xlsx', '.csv']
}

# Create folders for each category if they don't exist
for folder in file_categories.keys():
    folder_path = os.path.join(directory_path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Iterate through each file in the directory
for filename in os.listdir(directory_path):
    # Ignore directories
    if os.path.isdir(os.path.join(directory_path, filename)):
        continue
    
    # Get the file extension
    file_extension = os.path.splitext(filename)[1]
    
    # Check which category the file belongs to
    for folder, extensions in file_categories.items():
        if file_extension in extensions:
            # Define new file name by appending date stamp
            new_filename = f"{os.path.splitext(filename)[0]}_{date_stamp}{file_extension}"
            # Move and rename the file
            src_path = os.path.join(directory_path, filename)
            dest_path = os.path.join(directory_path, folder, new_filename)
            shutil.move(src_path, dest_path)
            print(f"Moved: {src_path} -> {dest_path}")
            break
