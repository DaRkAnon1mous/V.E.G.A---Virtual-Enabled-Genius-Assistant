import wikipedia
import webbrowser as wb
import pywhatkit
from utils.speech import speak, takeCommand, takeCommandWithContext
from utils.helpers import is_connected

def search_wikipedia(query):
    """Search Wikipedia with improved query recognition"""
    try:
        speak("Searching Wikipedia...")
        
        # Clean the query
        query = query.replace("wikipedia", "").replace("search", "").strip()
        
        if not query or len(query) < 2:
            speak("What would you like me to search for on Wikipedia?")
            # Use context-aware recognition for better accuracy
            query = takeCommandWithContext(["search", "wikipedia", "tell", "about"])
        
        if query and query != "none":
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        else:
            speak("I couldn't understand the search term.")
            
    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options[:3]
        speak(f"Multiple results found. Did you mean: {', '.join(options)}?")
        
        # Get clarification with context
        clarification = takeCommandWithContext(options)
        if clarification in [opt.lower() for opt in options]:
            search_wikipedia(clarification)
    
    except wikipedia.exceptions.PageError:
        speak("No Wikipedia page found for that query.")
    except Exception as e:
        speak("Sorry, I couldn't search Wikipedia right now.")
        print(f"Wikipedia error: {e}")

def search_google():
    """Search Google with improved query recognition"""
    speak("What should I search for?")
    
    # Use search-context vocabulary
    search_context = ["search", "google", "find", "look", "for", "about"]
    search_query = takeCommandWithContext(search_context)
    
    if search_query and search_query != "none":
        url = f"https://www.google.com/search?q={search_query}"
        wb.open_new_tab(url)
        speak(f"Searching Google for {search_query}")
    else:
        speak("I didn't catch the search query.")

def handle_music_command():
    """Handle music with music-specific vocabulary"""
    speak("What song would you like to play?")
    
    # Music context words
    music_context = ["play", "song", "music", "artist", "album", "youtube"]
    song = takeCommandWithContext(music_context)
    
    if song and song != "none":
        play_song_online(song)
    else:
        speak("I didn't catch the song name. Please try again.")

def play_song_online(song_name):
    """Play song on YouTube with error handling"""
    if is_connected():
        try:
            pywhatkit.playonyt(song_name)
            speak(f"Playing {song_name} on YouTube.")
        except Exception as e:
            speak("Sorry, I couldn't play that song.")
            print(f"Music error: {e}")
    else:
        speak("No internet connection. Please check your network.")
