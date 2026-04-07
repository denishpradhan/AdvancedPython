import os
import shutil

# Path to your messy folder (CHANGE THIS)
source_folder =input("Enter the path to your messy folder: ")
destination_folder = source_folder

# File type categories
categories = {
    "Kicks": ["kick"],
    "Snares": ["snare"],
    "HiHats": ["hat", "hihat"],
    "Claps": ["clap"],
    "Loops": ["loop"],
    "Bass": ["bass"],
    "Others": [],
}

# Create folders if they don't exist
for category in categories:
    folder_path = os.path.join(destination_folder, category)
    os.makedirs(folder_path, exist_ok=True)

# Go through each file inside the source folder
for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file) # joins the file to the source folder path

    if os.path.isfile(file_path):
        moved = False

        for category, keywords in categories.items():
            for keyword in keywords:
                if keyword.lower() in file.lower():
                    shutil.move(file_path, os.path.join(destination_folder, category, file))
                    moved = True
                    break
            if moved:
                break

        if not moved:
            shutil.move(file_path, os.path.join(destination_folder, "Others", file))

print("Files organized successfully!")