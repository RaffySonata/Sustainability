import os
import shutil

# Set your base directory where the nested folders are located
base_directory = '/Users/raffysonata/Downloads/4. Form Excel Isian SPBU & Evidence Setiap Regional 2'
# Set your target directory where you want to consolidate the files
target_directory = '/Users/raffysonata/Library/CloudStorage/OneDrive-Personal/Documents/Work/UGM/Pertamina/SPBU/Form_12082024'

# Create the target directory if it doesn't exist
if not os.path.exists(target_directory):
    os.makedirs(target_directory)

# Initialize a counter for renaming files
file_counter = 1

# Traverse the directory tree
for root, dirs, files in os.walk(base_directory):
    for file in files:
        if file.endswith('.xlsx'):
            old_file_path = os.path.join(root, file)
            new_file_path = os.path.join(target_directory, f"{file_counter}.xlsx")

            # Move the file to the target directory and rename it
            shutil.move(old_file_path, new_file_path)
            print(f"Moved and renamed {old_file_path} to {new_file_path}")

            # Increment the counter
            file_counter += 1
