import socket

def is_connected():
    """Check if internet connection is available"""
    try:
        socket.create_connection(("www.google.com", 80), timeout=5)
        return True
    except OSError:
        return False

def get_confirmation(message="Are you sure?"):
    """Get yes/no confirmation from user"""
    from utils.speech import speak, takeCommand
    speak(message)
    response = takeCommand().lower()
    return "yes" in response
