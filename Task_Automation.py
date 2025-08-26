import os
import shutil

def move_jpg_files(source_folder, destination_folder):
    # Create the destination folder if it does not exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Loop through all files in the source folder
    for file_name in os.listdir(source_folder):
        if file_name.lower().endswith(".jpg"):  # check if file ends with .jpg
            source_path = os.path.join(source_folder, file_name)
            destination_path = os.path.join(destination_folder, file_name)

            # Move the file
            shutil.move(source_path, destination_path)
            print(f"Moved: {file_name}")

# Example usage
source = r"F:\OneDrive - Systems Limited\Pictures\Test Folder"       # put your source folder path
destination = r"F:\OneDrive - Systems Limited\Pictures\Pictures\JPG_Files"  # put your destination folder path

move_jpg_files(source, destination)
