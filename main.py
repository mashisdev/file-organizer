import os
import shutil

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg", ".tiff", ".ico", ".heic", ".jfif"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv", ".webm", ".3gp", ".mpeg", ".mpg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".xls", ".xlsx", ".csv", ".ppt", ".pptx", ".epub"],
    "Music": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma", ".alac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso"],
    "Executables": [".exe", ".msi", ".bat", ".sh", ".app", ".jar", ".py", ".pl", ".rb", ".cmd", ".com"],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2", ".eot"],
    "Code": [".html", ".css", ".js", ".ts", ".jsx", ".tsx", ".php", ".c", ".cpp", ".h", ".hpp", ".java", ".cs", ".json", ".xml", ".yml", ".yaml", ".sql", ".md"],
    "Design": [".psd", ".ai", ".xd", ".fig", ".sketch", ".indd"],
    "3D Models": [".obj", ".fbx", ".stl", ".blend", ".3ds"]
}

def get_category(extension):
    for category, extensions in CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def get_folder_size(path):
    total_size = 0
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.isfile(fp):
                total_size += os.path.getsize(fp)
    return total_size

def format_size(bytes_size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_size < 1024:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024
    return f"{bytes_size:.2f} PB"

def organize_files(folder_path):
    if not os.path.isdir(folder_path):
        print("❌ The provided path is not valid.")
        return

    print("🔄 Organizing files...")

    moved_files = {}

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        if os.path.isfile(item_path):
            _, extension = os.path.splitext(item)
            category = get_category(extension)
            destination_folder = os.path.join(folder_path, category)

            if category != "Others" or (category == "Others" and extension):
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                shutil.move(item_path, os.path.join(destination_folder, item))
                print(f"✅ Moved: {item} → {category}/")
                moved_files[category] = moved_files.get(category, 0) + 1

    print("\n📦 Folder sizes:")
    for category in moved_files.keys():
        category_path = os.path.join(folder_path, category)
        size = get_folder_size(category_path)
        print(f"   📁 {category}: {format_size(size)}")

    print("\n🎉 All files have been successfully organized!")

if __name__ == "__main__":
    user_path = input("📂 Enter the path of the folder you want to organize: ").strip()
    organize_files(user_path)