import random
from datetime import datetime
from utils.speech import speak, takeCommand
from data.jokes import JOKES_LIST
from config.settings import REMINDER_FILE

def tell_joke():
    random_joke = random.choice(JOKES_LIST)
    speak(random_joke)
    print(f"Joke: {random_joke}")

def remember_this():
    speak("What should I remember?")
    data = takeCommand().strip()
    if data:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(REMINDER_FILE, "a") as f:
            f.write(f"[{timestamp}] {data}\n")
        speak("Got it. I've saved your reminder.")
    else:
        speak("I didn't catch that. Please try again.")

def recall_reminders():
    try:
        with open(REMINDER_FILE, "r") as f:
            reminders = f.readlines()
        if reminders:
            speak("Here are your saved reminders:")
            for line in reminders[-3:]:
                speak(line.strip())
        else:
            speak("You don't have any reminders yet.")
    except FileNotFoundError:
        speak("No reminder file found.")
import random
from datetime import datetime
from utils.speech import speak, takeCommand
from data.jokes import JOKES_LIST
from config.settings import REMINDER_FILE

def tell_joke():
    """Tell a random joke"""
    try:
        random_joke = random.choice(JOKES_LIST)
        speak(random_joke)
        print(f"Joke: {random_joke}")
    except Exception as e:
        speak("Sorry, I couldn't think of a joke right now.")
        print(f"Joke error: {e}")

def remember_this():
    """Save a reminder"""
    speak("What should I remember?")
    data = takeCommand().strip()
    
    if data and data != "none":
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(REMINDER_FILE, "a") as f:
                f.write(f"[{timestamp}] {data}\n")
            speak("Got it. I've saved your reminder.")
        except Exception as e:
            speak("Sorry, I couldn't save that reminder.")
            print(f"Reminder error: {e}")
    else:
        speak("I didn't catch that. Please try again.")

def recall_reminders():
    """Read saved reminders"""
    try:
        with open(REMINDER_FILE, "r") as f:
            reminders = f.readlines()
        
        if reminders:
            speak("Here are your saved reminders:")
            for line in reminders[-3:]:  # Last 3 reminders
                speak(line.strip())
        else:
            speak("You don't have any reminders yet.")
    except FileNotFoundError:
        speak("No reminder file found. You haven't saved any reminders yet.")
    except Exception as e:
        speak("Sorry, I couldn't read your reminders.")
        print(f"Recall error: {e}")
