import os
import psutil
from pathlib import Path
from datetime import datetime
import pyautogui

def get_screenshot_path():
    """Generate screenshot file path"""
    home = Path.home()
    folder = home / "Pictures" / "VoiceAssistantScreenshots"
    folder.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return folder / f"screenshot_{timestamp}.png"

def get_system_stats():
    """Get CPU and battery information"""
    cpu_usage = psutil.cpu_percent()
    
    battery = psutil.sensors_battery()
    battery_percent = battery.percent if battery else None
    
    return {
        'cpu': cpu_usage,
        'battery': battery_percent
    }
