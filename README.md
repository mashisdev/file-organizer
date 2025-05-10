# File organizer 📂

A terminal-based Python application to automatically organize files into categorized folders (images, videos, documents, etc.) based on their extensions. No third-party Python packages required, only built-in modules `os` and `shutil`.

## 🔧Usage:
1. Clone and run

   ```bash
   git clone https://github.com/your-username/file-organizer.git
   cd file-organizer
   py main.py
   ```
3. Enter the path to the folder you want to organize:
   
   ```bash
   📂 Enter the path of the folder you want to organize: C:\Users\Usuario\Downloads
   ```
4. Return example:
   
   ```bash
   🔄 Organizing files...
   ✅ Moved: resume.pdf → Documents/
   ✅ Moved: cat.jpg → Images/
   ✅ Moved: video.mp4 → Videos/
   ✅ Moved: script.py → Code/
   ✅ Moved: archive.zip → Archives/
   ✅ Moved: audio.mp3 → Music/
   ✅ Moved: design.sketch → Design/
   ✅ Moved: notes.txt → Documents/
   ✅ Moved: logo.svg → Images/

   📦 Folder sizes:
      📁 Documents: 82.32 KB
      📁 Images: 1.15 MB
      📁 Videos: 14.08 MB
      📁 Code: 2.34 KB
      📁 Archives: 3.47 MB
      📁 Music: 5.81 MB
      📁 Design: 920.75 KB

   🎉 All files have been successfully organized!
   ```

## 🧪Tests
This project includes automated tests written with [`pytest`](https://docs.pytest.org/), which help verify that the functions of the file organizer work correctly.

<details>
<summary><strong>What is tested?</strong></summary>

- `get_category(extension)`: ensures file extensions are correctly classified into categories.
- `format_size(bytes_size)`: verifies that file sizes are properly formatted (e.g., bytes → KB/MB).
- `get_folder_size(path)`: confirms that the total size of a folder is calculated accurately.
- `organize_files(folder_path)`: tests that files are moved into the correct category folders based on their extensions.

</details>

<details>
<summary><strong>How to run the tests</strong></summary>
   
   Make sure `pytest` is installed and run:
   
   ```bash
   pip install -U pytest
   pytest
   ```

   Output:

   ```bash
   =================== test session starts ===================
   platform
   rootdir:
   collected 4 items
   
   test_main.py ....                                    [100%]
   
   ==================== all tests passed =====================
   ```

</details>

   
