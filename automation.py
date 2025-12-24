import os
import shutil

source_folder = "source_files"
destination_folder = "organized_files"

os.makedirs(destination_folder, exist_ok=True)

for file_name in os.listdir(source_folder):
    if file_name.endswith(".txt"):
        shutil.move(
            os.path.join(source_folder, file_name),
            os.path.join(destination_folder, file_name)
        )

print("Automation complete. Files organized.")
