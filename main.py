import os

def delete_folder(folder_path):
    # Delete the folder and all of its contents
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(folder_path)

    print(f"Folder '{folder_path}' deleted successfully.")

if __name__ == "__main__":
    folder_path_to_delete = input("Enter the path of the folder to delete: ")
    delete_folder(folder_path_to_delete)