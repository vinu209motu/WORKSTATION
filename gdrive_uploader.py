from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
import os

class GoogleDriveUploader:
    def __init__(self, credentials_path):
        self.credentials_path = credentials_path
        self.service = self.authenticate()

    def authenticate(self):
        SCOPES = ['https://www.googleapis.com/auth/drive.file']
        flow = InstalledAppFlow.from_client_secrets_file(self.credentials_path, SCOPES)
        creds = flow.run_local_server(port=0)  # Authenticates with user consent via a browser
        return build('drive', 'v3', credentials=creds)

    def upload_file(self, local_file_path, drive_folder_id=None):
        try:
            file_metadata = {'name': os.path.basename(local_file_path)}
            if drive_folder_id:
                file_metadata['parents'] = [drive_folder_id]
            media = MediaFileUpload(local_file_path, resumable=True)
            uploaded_file = self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            print(f"File uploaded successfully. File ID: {uploaded_file.get('id')}")
        except Exception as e:
            print(f"Error uploading file to Google Drive: {e}")

