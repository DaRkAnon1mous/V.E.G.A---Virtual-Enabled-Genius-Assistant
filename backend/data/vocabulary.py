"""
Custom vocabulary for JARVIS voice assistant
Contains all command keywords and phrases for better recognition
"""

# Core command words
CORE_COMMANDS = [
    "jarvis", "time", "date", "exit", "quit", "goodbye", "bye", "hello", "hi",
    "wikipedia", "search", "google", "email", "send", "play", "song", "music",
    "joke", "funny", "remember", "reminder", "screenshot", "battery", "cpu",
    "system", "shutdown", "restart", "logout", "help", "commands", "what"
]

# Complete command phrases
COMMAND_PHRASES = [
    # Basic commands
    "what time is it", "tell me the time", "current time",
    "what date is it", "tell me the date", "current date", "today's date",
    "exit", "quit", "goodbye", "bye jarvis", "see you later",
    "hello jarvis", "hi jarvis", "hey jarvis","yes","no",
    
    # Information commands
    "search wikipedia", "wikipedia search", "tell me about",
    "search google", "google search", "search for",
    
    # Communication
    "send email", "send an email", "compose email", "write email",
    
    # Entertainment
    "play song", "play music", "play a song", "play some music",
    "tell me a joke", "tell joke", "say something funny", "make me laugh",
    "remember this", "remember that", "save this", "note this",
    "what do you remember", "my reminders", "last reminder", "show reminders",
    
    # System control
    "take screenshot", "capture screen", "screenshot",
    "battery status", "cpu usage", "system status", "battery percentage",
    "shutdown computer", "shut down", "shutdown system",
    "restart computer", "restart system", "reboot",
    "logout", "log out", "sign out",
    
    # Help
    "what can you do", "help me", "show commands", "list commands",
    "what are your commands", "your capabilities"
]

# Names and entities
NAMES_ENTITIES = [
    "john", "mom", "boss", "friend", "me",
    "youtube", "google", "gmail", "windows","shrey"
]

# Technical terms
TECH_TERMS = [
    "internet", "connection", "network", "wifi", "bluetooth",
    "screenshot", "battery", "percentage", "usage"
]

# Create combined vocabulary
CUSTOM_VOCABULARY = list(set(
    CORE_COMMANDS + 
    COMMAND_PHRASES + 
    NAMES_ENTITIES + 
    TECH_TERMS +
    # Add individual words from phrases
    [word for phrase in COMMAND_PHRASES for word in phrase.split()]
))

# Grammar rules for better context understanding
GRAMMAR_RULES = [
    "[unk] <command> [unk]",
    "jarvis <command>",
    "<command> please",
    "can you <command>",
    "please <command>",
    "i want to <command>",
    "help me <command>"
]
