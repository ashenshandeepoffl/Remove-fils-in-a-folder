import time
import pyautogui

def delete_folder(folder_name):
    # Open File Explorer
    pyautogui.hotkey('winleft', 'e')
    time.sleep(1)  # Wait for File Explorer to open

    # Focus on the address bar
    pyautogui.hotkey('alt', 'd')
    time.sleep(1)  # Wait for focus

    # Type the path of the folder
    pyautogui.write(folder_name)
    pyautogui.press('enter')
    time.sleep(1)  # Wait for the folder to open

    # Select all items in the folder
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)  # Wait for items to be selected

    # Delete the selected items
    pyautogui.press('delete')
    time.sleep(1)  # Wait for confirmation dialog to appear

    # Confirm the deletion (press Enter)
    pyautogui.press('enter')
    time.sleep(1)  # Wait for deletion process to complete

    print(f"Folder '{folder_name}' deleted successfully.")

if __name__ == "__main__":
    folder_name_to_delete = input("Enter the name of the folder to delete: ")
    delete_folder(folder_name_to_delete)
