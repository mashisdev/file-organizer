import os
import tempfile
import pytest
from main import get_category, get_folder_size, format_size, organize_files

def test_get_category():
    assert get_category(".jpg") == "Images"
    assert get_category(".mp4") == "Videos"
    assert get_category(".docx") == "Documents"
    assert get_category(".xyz") == "Others"

def test_format_size():
    assert format_size(500) == "500.00 B"
    assert format_size(1024) == "1.00 KB"
    assert format_size(1048576) == "1.00 MB"

def test_get_folder_size():
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, "test.txt")
        with open(file_path, "wb") as f:
            f.write(b"x" * 100)
        assert get_folder_size(tmpdir) == 100

def test_organize_files():
    with tempfile.TemporaryDirectory() as tmpdir:
        
        # Create test files
        filenames = ["image.jpg", "video.mp4", "doc.pdf", "unknown.xyz"]
        for name in filenames:
            with open(os.path.join(tmpdir, name), "w") as f:
                f.write("dummy content")

        organize_files(tmpdir)

        # Check that files were moved to the correct folders
        assert os.path.exists(os.path.join(tmpdir, "Images", "image.jpg"))
        assert os.path.exists(os.path.join(tmpdir, "Videos", "video.mp4"))
        assert os.path.exists(os.path.join(tmpdir, "Documents", "doc.pdf"))
        assert os.path.exists(os.path.join(tmpdir, "Others", "unknown.xyz"))