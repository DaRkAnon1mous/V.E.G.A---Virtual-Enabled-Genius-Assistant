import os
import pyautogui
from utils.speech import speak, takeCommand
from utils.helpers import get_confirmation
from utils.system import get_screenshot_path, get_system_stats

def take_screenshot():
    """Take and save screenshot"""
    if get_confirmation("Do you want to take a screenshot?"):
        try:
            path = get_screenshot_path()
            screenshot = pyautogui.screenshot()
            screenshot.save(path)
            speak(f"Screenshot saved successfully.")
            print(f"Screenshot saved at: {path}")
        except Exception as e:
            speak("Failed to take screenshot.")
            print(f"Screenshot error: {e}")

def show_cpu_battery():
    """Show system statistics"""
    try:
        stats = get_system_stats()
        speak(f"CPU usage is {stats['cpu']} percent")
        
        if stats['battery'] is not None:
            speak(f"Battery percentage is {stats['battery']} percent")
        else:
            speak("Battery information not available.")
    except Exception as e:
        speak("Sorry, I couldn't get system information.")
        print(f"System stats error: {e}")

def system_shutdown():
    """Shutdown the system"""
    if get_confirmation("Are you sure you want to shutdown the system?"):
        speak("Shutting down the system. Goodbye!")
        os.system("shutdown /s /t 1")
    else:
        speak("Shutdown cancelled.")

def system_restart():
    """Restart the system"""
    if get_confirmation("Are you sure you want to restart the system?"):
        speak("Restarting the system.")
        os.system("shutdown /r /t 1")
    else:
        speak("Restart cancelled.")

def system_logout():
    """Logout from system"""
    if get_confirmation("Are you sure you want to logout?"):
        speak("Logging out. See you later!")
        os.system("shutdown -l")
    else:
        speak("Logout cancelled.")
