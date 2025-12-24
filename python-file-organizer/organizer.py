import os
import shutil

# Data categories based on file type
DATA_CATEGORIES = {
    "tabular_data": [".csv", ".xlsx"],
    "structured_data": [".json", ".xml"],
    "logs": [".log", ".txt"],
    "media": [".jpg", ".jpeg", ".png"],
    "documents": [".pdf", ".docx"],
}

path = input("Enter Path: ")

# Folder where segregated data will be stored
target_folder = os.path.join(path, "segregated_data")

if not os.path.exists(target_folder):
    os.makedirs(target_folder)

files = os.listdir(path)

for file in files:
    try:
        file_path = os.path.join(path, file)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        filename, extension = os.path.splitext(file)
        extension = extension.lower()

        if extension == "":
            continue

        moved = False

        # Check which category the file belongs to
        for category, extensions in DATA_CATEGORIES.items():
            if extension in extensions:
                category_path = os.path.join(target_folder, category)
                os.makedirs(category_path, exist_ok=True)
                shutil.move(file_path, os.path.join(category_path, file))
                print(f"Moved {file} → {category}/")
                moved = True
                break

        # If file type does not match any category
        if not moved:
            other_path = os.path.join(target_folder, "others")
            os.makedirs(other_path, exist_ok=True)
            shutil.move(file_path, os.path.join(other_path, file))
            print(f"Moved {file} → others/")

    except Exception as e:
        print(f"Error moving {file}: {e}")

print("✅ Data classification and segregation completed.")
