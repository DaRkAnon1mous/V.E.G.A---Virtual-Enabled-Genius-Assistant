import pyttsx3
import vosk
import pyaudio
import json
from config.settings import VOICE_RATE, VOICE_INDEX, VOSK_MODEL_PATH
from data.vocabulary import CUSTOM_VOCABULARY

# Initialize Vosk with custom vocabulary
def initialize_vosk_model():
    """Initialize Vosk model with custom vocabulary for better accuracy"""
    try:
        model = vosk.Model(VOSK_MODEL_PATH)
        
        # Create recognizer with custom vocabulary
        rec = vosk.KaldiRecognizer(model, 16000)
        
        # Set custom vocabulary to focus on our commands
        # This tells Vosk to prioritize these words/phrases
        vocabulary_json = json.dumps(CUSTOM_VOCABULARY)
        rec.SetWords(True)  # Enable word-level timestamps
        
        # Set grammar/vocabulary (if the model supports it)
        try:
            rec.SetGrammar(vocabulary_json)
            print("✓ Custom vocabulary loaded for better command recognition")
        except:
            print("✓ Basic model loaded (custom vocabulary not supported by this model)")
        
        return model, rec
        
    except Exception as e:
        print(f"Error initializing Vosk model: {e}")
        # Fallback to basic model
        model = vosk.Model(VOSK_MODEL_PATH)
        rec = vosk.KaldiRecognizer(model, 16000)
        return model, rec

# Initialize once at module level
model, rec = initialize_vosk_model()

def speak(audio):
    """Convert text to speech with optimized settings"""
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        
        if voices and len(voices) > VOICE_INDEX:
            engine.setProperty('voice', voices[VOICE_INDEX].id)
        
        engine.setProperty('rate', VOICE_RATE)
        engine.say(audio)
        engine.runAndWait()
        del engine
    except Exception as e:
        print(f"Speech error: {e}")

def takeCommand(timeout=5):
    """
    Listen to user voice and convert to text with improved accuracy
    Args:
        timeout: Maximum time to wait for speech (seconds)
    """
    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=16000,
        input=True,
        frames_per_buffer=8000
    )
    stream.start_stream()
    
    print("🎤 Listening...")
    
    frames_since_speech = 0
    max_silent_frames = timeout * 25  # Roughly 25 frames per second
    
    while True:
        try:
            data = stream.read(4000, exception_on_overflow=False)
            
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                query = result['text'].strip()
                
                if query:
                    print(f"✓ You said: {query}")
                    # Clean up audio resources
                    stream.stop_stream()
                    stream.close()
                    p.terminate()
                    return query
                    
            else:
                # Check partial results for immediate feedback
                partial_result = json.loads(rec.PartialResult())
                if partial_result.get('partial'):
                    print(f"🔄 Partial: {partial_result['partial']}", end='\r')
            
            # Timeout handling
            frames_since_speech += 1
            if frames_since_speech > max_silent_frames:
                print("\n⏱️  Listening timeout")
                break
                
        except Exception as e:
            print(f"❌ Audio error: {e}")
            break
    
    # Clean up resources
    stream.stop_stream()
    stream.close()
    p.terminate()
    return "None"

def takeCommandWithContext(context_words=None):
    """
    Enhanced command recognition with context-aware vocabulary
    Args:
        context_words: List of words to prioritize in current context
    """
    if context_words:
        # Temporarily boost vocabulary with context words
        temp_vocab = CUSTOM_VOCABULARY + context_words
        vocab_json = json.dumps(temp_vocab)
        try:
            rec.SetGrammar(vocab_json)
        except:
            pass  # Fallback to regular recognition
    
    return takeCommand()
