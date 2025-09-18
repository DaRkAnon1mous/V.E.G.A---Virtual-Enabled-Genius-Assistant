"""
Flask WebSocket Server for VEGA Voice Assistant - UPDATED VERSION
"""
from flask import Flask, render_template, send_from_directory, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import threading
import json
from datetime import datetime
import os
import sys
from dotenv import load_dotenv

# Load environment variables FIRST
load_dotenv()

# Add your VEGA modules to path
sys.path.append('.')

# Import your existing VEGA modules
from utils.speech import speak, takeCommand
from skills.basic import wishme, get_time, get_date, show_commands
from skills.entertainment import tell_joke, remember_this, recall_reminders
from skills.web import search_wikipedia, handle_music_command, search_google
from skills.communication import handle_email
from skills.system_control import (
    take_screenshot, show_cpu_battery, 
    system_shutdown, system_restart, system_logout
)

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("FLASK_SECRET_KEY", "default-secret-key-for-dev")

# Enhanced CORS setup for development
CORS(app, 
     origins=["http://localhost:3000", "http://127.0.0.1:3000"], 
     allow_headers=["Content-Type"], 
     methods=["GET", "POST"])

# Enhanced SocketIO setup
socketio = SocketIO(app, 
                   cors_allowed_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
                   async_mode='eventlet',
                   logger=True,
                   engineio_logger=True)

# Store chat history
chat_history = []

class VegaWebInterface:
    def __init__(self, socketio):
        self.socketio = socketio
        self.is_listening = False
        self.is_speaking = False
        
    def emit_to_frontend(self, event, data):
        """Emit data to frontend"""
        try:
            if self.socketio:
                print(f"📤 Emitting {event}: {data}")
                self.socketio.emit(event, data)
        except Exception as e:
            print(f"❌ Emit error: {e}")
    
    def add_to_history(self, message_type, text):
        """Add message to chat history"""
        message = {
            'type': message_type,
            'text': text,
            'timestamp': datetime.now().isoformat(),
            'id': len(chat_history) + 1
        }
        chat_history.append(message)
        return message
    
    def web_speak(self, text):
        """Modified speak function that emits to frontend"""
        try:
            if os.environ.get('RENDER', 'false').lower() == 'true':
                print(f"🗣️ VEGA (text-only): {text}")
                message = self.add_to_history('assistant', text)
                self.emit_to_frontend('assistant_speaking', message)
                return
            print(f"🗣️ VEGA Speaking: {text}")
            message = self.add_to_history('assistant', text)
            self.emit_to_frontend('assistant_speaking', message)
            speak(text)
            self.emit_to_frontend('assistant_finished_speaking', {})
        except Exception as e:
            print(f"❌ Web speak error: {e}")
            error_msg = self.add_to_history('system', f"Error: {str(e)}")
            self.emit_to_frontend('error', error_msg)
    
    def web_takeCommand(self):
        """Modified takeCommand that emits real-time updates"""
        try:
            if os.environ.get('RENDER', 'false').lower() == 'true':
                print("🎤 Voice input disabled on Render. Use text commands.")
                return "none"
            self.is_listening = True
            self.emit_to_frontend('listening_started', {})
            print("🎤 Starting to listen...")
            query = takeCommand()
            self.is_listening = False
            self.emit_to_frontend('listening_stopped', {})
            if query and query.lower() != "none":
                print(f"🗣️ User said: {query}")
                message = self.add_to_history('user', query)
                self.emit_to_frontend('user_spoke', message)
                return query
            else:
                print("⚠️ No speech detected")
                message = self.add_to_history('system', "No speech detected. Please try again.")
                self.emit_to_frontend('no_speech_detected', message)
                return "none"
        except Exception as e:
            print(f"❌ Web takeCommand error: {e}")
            self.is_listening = False
            error_msg = self.add_to_history('system', f"Listen error: {str(e)}")
            self.emit_to_frontend('error', error_msg)
            return "none"
    
    def get_command_confidence(self, query, keywords):
        """Improved confidence calculation considering phrase context"""
        query_words = query.lower().split()
        if not query_words:
            return 0.0
        
        # Define common contextual words that shouldn't penalize confidence
        contextual_words = {'what', 'is', 'the', 'to', 'for', 'me', 'my', 'please'}
        
        # Count matches among significant words (excluding contextual words)
        significant_words = [word for word in query_words if word not in contextual_words]
        if not significant_words:
            significant_words = query_words  # Fallback if all words are contextual
        
        matches = sum(1 for word in significant_words if word in keywords)
        total_significant = max(len(significant_words), 1)  # Avoid division by zero
        
        # Base confidence from keyword matches
        base_confidence = matches / total_significant
        
        # Boost confidence if multiple keywords are present
        keyword_count = sum(1 for word in query_words if word in keywords)
        if keyword_count > 1:
            base_confidence *= (1 + 0.2 * (keyword_count - 1))  # Add 20% per extra keyword
        
        # Ensure confidence doesn't exceed 1.0
        return min(base_confidence, 1.0)
    
    def process_web_command(self, query):
        """Modified process_command for web interface"""
        query = query.lower().strip()
        print(f"🔄 Processing command: {query}")
        
        # Your existing command mapping
        command_map = {
            "time": (["time", "clock"], get_time),
            "date": (["date", "today"], get_date),
            "exit": (["exit", "quit", "goodbye", "bye"], lambda: False),
            "wikipedia": (["wikipedia", "search", "tell", "about"], lambda: search_wikipedia(query)),
            "google": (["google", "search"], search_google),
            "email": (["email", "send", "mail"], handle_email),
            "music": (["play", "song", "music"], handle_music_command),
            "joke": (["joke", "funny", "laugh"], lambda: tell_joke()),
            "remember": (["remember", "save", "note"], remember_this),
            "reminder": (["reminder", "recall", "what", "remember"], recall_reminders),
            "screenshot": (["screenshot", "capture", "screen"], take_screenshot),
            "system": (["battery", "cpu", "system", "status"], show_cpu_battery),
            "shutdown": (["shutdown", "shut", "down"], system_shutdown),
            "restart": (["restart", "reboot"], system_restart),
            "logout": (["logout", "log", "out", "sign"], system_logout),
            "help": (["help", "commands", "what", "can", "do"], show_commands),
            "greeting": (["hello", "hi", "hey"], lambda: self.web_speak("Hello! How can I help you today?"))
        }
        
        # Find best matching command
        best_match = None
        best_confidence = 0
        
        for cmd_name, (keywords, func) in command_map.items():
            confidence = self.get_command_confidence(query, keywords)
            if confidence > best_confidence:
                best_confidence = confidence
                best_match = (cmd_name, func)
        
        # Lower the confidence threshold to 0.2 to catch more natural phrases
        if best_match and best_confidence > 0.2:
            cmd_name, func = best_match
            print(f"🎯 Executing: {cmd_name} (confidence: {best_confidence:.2f})")
            
            # Emit command execution info
            self.emit_to_frontend('command_executed', {
                'command': cmd_name,
                'confidence': best_confidence,
                'query': query
            })
            
            if cmd_name == "exit":
                self.web_speak("Goodbye! Have a great day!")
                return False
            else:
                # Execute the function
                try:
                    result = func()
                    return result if result is not None else True
                except Exception as e:
                    print(f"❌ Command execution error: {e}")
                    self.web_speak(f"Sorry, I encountered an error: {str(e)}")
                    return True
        else:
            if best_match:
                cmd_name, _ = best_match
                print(f"🤔 Best match was '{cmd_name}' but confidence too low: {best_confidence:.2f}")
            
            self.web_speak("I didn't understand that command. Say 'help' to see available commands.")
            return True

# Initialize VEGA web interface
vega_web = VegaWebInterface(socketio)

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy", "service": "VEGA Voice Assistant Web Interface"})

@app.route('/test')
def test_route():
    return jsonify({"message": "Backend is working!", "assistant": "VEGA", "time": datetime.now().isoformat()})

@app.route('/chat-history')
def get_chat_history():
    return jsonify({"history": chat_history})

@socketio.on('connect')
def handle_connect():
    print('🔌 Client connected to VEGA')
    # Send current chat history to newly connected client
    emit('connected', {
        'message': 'Connected to VEGA backend', 
        'timestamp': datetime.now().isoformat(),
        'history': chat_history
    })

@socketio.on('disconnect')
def handle_disconnect():
    print('🔌 Client disconnected from VEGA')
    vega_web.is_listening = False

@socketio.on('start_listening')
def handle_start_listening():
    print('🎤 Web: Start listening request received')
    
    def listen_and_process():
        try:
            query = vega_web.web_takeCommand()
            if query and query != "none":
                vega_web.process_web_command(query)
        except Exception as e:
            print(f"❌ Listen and process error: {e}")
            error_msg = vega_web.add_to_history('system', f"Listen error: {str(e)}")
            vega_web.emit_to_frontend('error', error_msg)
    
    listen_thread = threading.Thread(target=listen_and_process)
    listen_thread.daemon = True
    listen_thread.start()

@socketio.on('stop_listening')
def handle_stop_listening():
    print('🛑 Web: Stop listening request received')
    vega_web.is_listening = False
    emit('listening_stopped', {})

@socketio.on('send_text_command')
def handle_text_command(data):
    """Handle text commands from frontend"""
    command = data.get('command', '')
    print(f'💬 Web: Text command received: {command}')
    
    def process_text_command():
        try:
            # Add user message to history and emit
            message = vega_web.add_to_history('user', command)
            vega_web.emit_to_frontend('user_spoke', message)
            
            # Process the command
            vega_web.process_web_command(command)
        except Exception as e:
            print(f"❌ Text command error: {e}")
            error_msg = vega_web.add_to_history('system', f"Text command error: {str(e)}")
            vega_web.emit_to_frontend('error', error_msg)
    
    process_thread = threading.Thread(target=process_text_command)
    process_thread.daemon = True
    process_thread.start()

@socketio.on('initialize_vega')
def handle_initialize():
    """Initialize VEGA greeting"""
    print('🚀 Web: Initialize VEGA request received')
    
    def initialize():
        try:
            # Add system message about initialization
            init_msg = vega_web.add_to_history('system', 'Initializing VEGA...')
            vega_web.emit_to_frontend('system_message', init_msg)
            
            # Use your existing wishme function
            wishme()
        except Exception as e:
            print(f"❌ Initialize error: {e}")
            error_msg = vega_web.add_to_history('system', f"Initialize error: {str(e)}")
            vega_web.emit_to_frontend('error', error_msg)
    
    init_thread = threading.Thread(target=initialize)
    init_thread.daemon = True
    init_thread.start()

@socketio.on('clear_chat_history')
def handle_clear_history():
    """Clear chat history"""
    global chat_history
    chat_history = []
    emit('chat_history_cleared', {})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)