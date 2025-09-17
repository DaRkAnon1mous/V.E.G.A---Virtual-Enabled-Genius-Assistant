import os
from dotenv import load_dotenv

load_dotenv()

# Email Configuration
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Voice Settings
VOICE_RATE = 172
VOICE_INDEX = 0

# Vosk Model Path
VOSK_MODEL_PATH = "vosk-model-small-en-us-0.15"

# File Paths
REMINDER_FILE = "reminders.txt"

# SMTP Settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
