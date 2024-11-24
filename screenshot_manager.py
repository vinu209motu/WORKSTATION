import time
from PIL import ImageGrab


class ScreenshotManager:
    def __init__(self, interval, drive_uploader):
        """
        Initializes the ScreenshotManager.
        :param interval: Time interval between screenshots in seconds.
        :param drive_uploader: An instance of GoogleDriveUploader for uploading screenshots.
        """
        self.interval = interval
        self.drive_uploader = drive_uploader

    def take_screenshot(self):
        """
        Captures a screenshot, saves it locally, and uploads it to Google Drive.
        """
        try:
            # Capture the screenshot
            screenshot = ImageGrab.grab()
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"

            # Save the screenshot locally
            screenshot.save(filename)
            print(f"Screenshot saved as {filename}")

            # Upload the screenshot to Google Drive
            self.drive_uploader.upload_file(filename)
            print(f"Screenshot uploaded to Google Drive: {filename}")

        except Exception as e:
            print(f"Error in taking screenshot: {e}")

    def start(self):
        """
        Starts the continuous screenshot-taking process.
        """
        print("Starting ScreenshotManager...")
        while True:
            self.take_screenshot()
            time.sleep(self.interval)


