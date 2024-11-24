
Workstation Agent is a Python-based application designed to track user activity, capture periodic screenshots, and upload them to Google Drive. It uses the Google Drive API for secure storage, making it ideal for productivity monitoring and automated logging.

Features
Tracks keyboard and mouse activity, saving logs locally.
Captures screenshots at regular intervals.
Automatically uploads logs and screenshots to Google Drive.
Installation
Clone the repository and navigate to the folder:
git clone https://github.com/yourusername/Workstation.git
cd Workstation
Set up a virtual environment and install dependencies:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
Obtain a credentials.json file from Google Drive API and place it in the project directory.
Usage
Run the application using:
python main.py
The app will track activity, capture screenshots every 60 seconds, and upload them to Google Drive. To stop, press Ctrl+C.

Configuration
Adjust the screenshot interval by modifying the interval parameter in main.py.
To save files in a specific Google Drive folder, update the folder ID in gdrive_uploader.py.
Requirements
Python 3.7+ with libraries: google-api-python-client, google-auth, pynput, pillow.
For detailed setup instructions or customization, refer to the comments in the code.

