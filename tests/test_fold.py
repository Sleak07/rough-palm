"""this tests cover pytest to check folder for images"""

import pytest
import os

@pytest.fixture
def image_folder(tmpdir):
    # Create a temporary directory
    folder = tmpdir.mkdir("images")

    # Create some dummy image files
    images = ['image1.jpg', 'image2.png', 'image3.gif']
    for image in images:
        file_path = folder.join(image)
        open(file_path, 'w').close()

    yield folder  # Provide the folder object to the tests

    # Optionally, you can add teardown code here
    # For example, if you want to clean up the temporary directory after the tests
    folder.remove()

# Test function using the fixture
def test_images_exist(image_folder):
    # Get the path to the folder
    folder_path = str(image_folder)

    # Check if images exist in the folder
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    images_exist = any(file.lower().endswith(tuple(image_extensions)) for file in os.listdir(folder_path))
    
    assert images_exist, "No images found in the folder."




