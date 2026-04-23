import os
import shutil

# Folder to organize

folder_path = input("Enter the folder path you want to organize: ")

# File type categories

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"],
}

# Creates folders if they don't exist

for folder in file_types:
    folder_name = os.path.join(folder_path, folder)
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

# Move files into their categories

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):
        file_ext = os.path.splitext(filename)[1].lower()

        moved = False
        for folder, extensions in file_types.items():
            if file_ext in extensions:
                shutil.move(file_path, os.path.join(folder_path, folder, filename))
                moved = True
                break

        if not moved:
             print(f"Skipped: {filename}")

print("Organization complete!")
