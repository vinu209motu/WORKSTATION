import time
from gdrive_uploader import GoogleDriveUploader
from screenshot_manager import ScreenshotManager
import threading
import os

def start_screenshot_manager():
    """
    Initializes and starts the ScreenshotManager.
    """
    try:
        # Path to the credentials file (update this with the correct path)
        credentials_path = r'C:\Users\vini1\OneDrive\Desktop\workstation\credentials.json'

        # Create an instance of GoogleDriveUploader with the credentials path
        uploader = GoogleDriveUploader(credentials_path=credentials_path)

        # Initialize the ScreenshotManager with a 60-second interval
        manager = ScreenshotManager(interval=60, drive_uploader=uploader)

        # Start the screenshot manager
        manager.start()

    except Exception as e:
        print(f"Error in starting ScreenshotManager: {e}")

if __name__ == "__main__":
    # Run the ScreenshotManager in a separate thread
    screenshot_thread = threading.Thread(target=start_screenshot_manager, daemon=True)
    screenshot_thread.start()

    # Keep the main program running
    print("Main program is running. Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program terminated by user.")

