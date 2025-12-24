import os
import shutil

path = input("Enter Path: ")
files = os.listdir(path)

for file in files:
    try:
        if os.path.isdir(os.path.join(path, file)):
            continue

        filename, extension = os.path.splitext(file)
        extension = extension[1:]

        if extension == "":
            continue

        folder_path = os.path.join(path, extension)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        shutil.move(
            os.path.join(path, file),
            os.path.join(folder_path, file)
        )

        print(f"Moved {file} to {extension}/")

    except Exception as e:
        print(f"Error moving {file}: {e}")
