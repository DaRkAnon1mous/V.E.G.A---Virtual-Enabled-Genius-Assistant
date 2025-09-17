from datetime import datetime
from utils.speech import speak

def get_time():
    """Tell current time"""
    time = datetime.now().strftime("%I:%M:%S")
    speak(f"The current time is {time}")

def get_date():
    """Tell current date"""
    now = datetime.now()
    speak(f"The current date is {now.day} {now.month} {now.year}")

def wishme():
    """Greet user based on time of day"""
    speak("Hello !")
    hour = datetime.now().hour
    
    if 6 <= hour <= 12:
        speak("Good Morning")
    elif 12 < hour <= 18:
        speak("Good Afternoon")
    elif 18 < hour <= 24:
        speak("Good Evening")
    else:
        speak("Good Night")
    
    speak("VEGA at your service. Please tell me how may I help you?")

def show_commands():
    """List available commands"""
    commands = [
        "I can tell time and date",
        "Search Wikipedia",
        "Send emails",
        "Play songs on YouTube",
        "Take screenshots",
        "Show CPU and battery status",
        "Tell jokes",
        "Remember things for you",
        "Control system shutdown, restart, or logout"
    ]
    speak("Here's what I can do for you:")
    for command in commands:
        speak(command)
