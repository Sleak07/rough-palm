import os

def check_images_exist(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print("Folder not found.")
        return False
    
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    
    # Check if there are any files with common image extensions
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    images_exist = any(file.lower().endswith(tuple(image_extensions)) for file in files)
    
    return images_exist

# Example usage:
folder_path = '/path/to/your/folder'
images_exist = check_images_exist(folder_path)

if images_exist:
    print("Images exist in the folder.")
else:
    print("No images found in the folder.")

if __name__ == "__main__":
    # You need to provide a folder path when calling check_images_exist()
    # For example:
    folder_path = '/path/to/your/folder'
    check_images_exist(folder_path)
