"""
JARVIS Voice Assistant with Enhanced Speech Recognition
"""

from utils.speech import speak, takeCommand
from skills.basic import wishme, get_time, get_date, show_commands
from skills.entertainment import tell_joke, remember_this, recall_reminders
from skills.web import search_wikipedia, handle_music_command, search_google
from skills.communication import handle_email
from skills.system_control import (
    take_screenshot, show_cpu_battery, 
    system_shutdown, system_restart, system_logout
)


def get_command_confidence(query, keywords):
    """
    Calculate confidence score for command matching based on spoken words
    
    Confidence = (number of query words that match keywords) / (total query words)
    This ensures single-word commands like 'bye' get full confidence (1.0)
    """
    query_words = query.lower().split()
    if not query_words:  # Handle empty query
        return 0.0
    
    matches = sum(1 for word in query_words if word in keywords)
    return matches / len(query_words)  # Fixed: divide by query length, not keyword length


def process_command(query):
    """Enhanced command processing with confidence scoring"""
    query = query.lower().strip()
    
    # Command matching with confidence
    command_map = {
        "time": (["time", "clock"], get_time),
        "date": (["date", "today"], get_date),
        "exit": (["exit", "quit", "goodbye", "bye"], lambda: False),
        "wikipedia": (["wikipedia", "search", "tell", "about"], lambda: search_wikipedia(query)),
        "google": (["google", "search"], search_google),
        "email": (["email", "send", "mail"], handle_email),
        "music": (["play", "song", "music"], handle_music_command),
        "joke": (["joke", "funny", "laugh"], lambda: (speak("Let me think of a good one..."), tell_joke())[1]),
        "remember": (["remember", "save", "note"], remember_this),
        "reminder": (["reminder", "recall", "what", "remember"], recall_reminders),
        "screenshot": (["screenshot", "capture", "screen"], take_screenshot),
        "system": (["battery", "cpu", "system", "status"], show_cpu_battery),
        "shutdown": (["shutdown", "shut", "down"], system_shutdown),
        "restart": (["restart", "reboot"], system_restart),
        "logout": (["logout", "log", "out", "sign"], system_logout),
        "help": (["help", "commands", "what", "can", "do"], show_commands),
        "greeting": (["hello", "hi", "hey"], lambda: speak("Hello! How can I help you today?"))
    }
    
    # Find best matching command
    best_match = None
    best_confidence = 0
    
    for cmd_name, (keywords, func) in command_map.items():
        confidence = get_command_confidence(query, keywords)
        if confidence > best_confidence:
            best_confidence = confidence
            best_match = (cmd_name, func)
    
    # Execute command if confidence is high enough
    if best_match and best_confidence > 0.3:  # 30% confidence threshold
        cmd_name, func = best_match
        print(f"🎯 Executing: {cmd_name} (confidence: {best_confidence:.2f})")
        
        if cmd_name == "exit":
            speak("Goodbye sir! Have a great day!")
            return False
        else:
            result = func()
            return result if result is not None else True
    else:
        # Lower threshold for debugging - show what was attempted
        if best_match:
            cmd_name, _ = best_match
            print(f"🤔 Best match was '{cmd_name}' but confidence too low: {best_confidence:.2f}")
        
        speak("I didn't understand that command. Say 'help' to see available commands.")
        return True


def main():
    """Main function with enhanced error handling"""
    try:
        print("🚀 JARVIS Voice Assistant Starting...")
        
        wishme()
        
        while True:
            query = takeCommand()
            
            if query and query.lower() != "none":
                print(f"💭 Processing: '{query}'")
                
                should_continue = process_command(query)
                if not should_continue:
                    break
            else:
                print("⚠️  No command detected or recognition failed")
                
    except KeyboardInterrupt:
        print("\n🛑 Assistant interrupted by user")
        speak("Assistant interrupted. Goodbye!")
    except Exception as e:
        speak("Sorry, I encountered an error. Please restart me.")
        print(f"❌ Main error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
