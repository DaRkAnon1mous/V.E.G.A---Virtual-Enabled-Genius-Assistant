import React, { useState, useEffect, useRef } from 'react';
import io from 'socket.io-client';
import { motion, AnimatePresence } from 'framer-motion';
import './App.css';

const BACKEND_URL = process.env.NODE_ENV === 'production' 
  ? window.location.origin 
  : 'http://localhost:5000';

function App() {
  const [socket, setSocket] = useState(null);
  const [isConnected, setIsConnected] = useState(false);
  const [isListening, setIsListening] = useState(false);
  const [isSpeaking, setIsSpeaking] = useState(false);
  const [messages, setMessages] = useState([]);
  const [textInput, setTextInput] = useState('');
  const [connectionStatus, setConnectionStatus] = useState('Connecting...');

  useEffect(() => {
    const newSocket = io(BACKEND_URL, {
      transports: ['websocket', 'polling'],
      timeout: 10000,
    });

    // Connection handlers
    newSocket.on('connect', () => {
      console.log('✅ Connected to VEGA');
      setIsConnected(true);
      setConnectionStatus('Connected');
      addMessage('system', '✨ VEGA is now online and ready to assist you!');
    });

    newSocket.on('connected', (data) => {
      console.log('Connected with history:', data.history);
      if (data.history && data.history.length > 0) {
        setMessages(data.history);
      }
    });

    newSocket.on('disconnect', () => {
      console.log('❌ Disconnected');
      setIsConnected(false);
      setIsListening(false);
      setIsSpeaking(false);
      setConnectionStatus('Disconnected');
    });

    // Voice interaction handlers
    newSocket.on('listening_started', () => {
      setIsListening(true);
      addMessage('system', '🎤 Listening... speak your command');
    });

    newSocket.on('listening_stopped', () => {
      setIsListening(false);
    });

    newSocket.on('user_spoke', (data) => {
      console.log('User spoke:', data);
      addMessage('user', data.text, data.timestamp);
    });

    newSocket.on('assistant_speaking', (data) => {
      console.log('Assistant speaking:', data);
      addMessage('assistant', data.text, data.timestamp);
      setIsSpeaking(true);
    });

    newSocket.on('assistant_finished_speaking', () => {
      setIsSpeaking(false);
    });

    newSocket.on('system_message', (data) => {
      console.log('System message:', data);
      addMessage('system', data.text, data.timestamp);
    });

    newSocket.on('command_executed', (data) => {
      console.log('Command executed:', data);
    });

    newSocket.on('error', (data) => {
      console.log('Error:', data);
      addMessage('system', `❌ ${data.text || data.message}`);
      setIsListening(false);
      setIsSpeaking(false);
    });

    newSocket.on('no_speech_detected', (data) => {
      console.log('No speech detected:', data);
      addMessage('system', data.text || '⚠️ No speech detected. Please try again.');
      setIsListening(false);
    });

    newSocket.on('chat_history_cleared', () => {
      setMessages([]);
    });

    setSocket(newSocket);
    return () => newSocket.close();
  }, []);

  const addMessage = (type, text, timestamp = null) => {
    const message = {
      type,
      text,
      timestamp: timestamp || new Date().toISOString(),
      id: Date.now() + Math.random()
    };
    setMessages(prev => [...prev, message]);
  };

  const toggleListening = () => {
    if (!socket || !isConnected) return;
    if (isListening) {
      socket.emit('stop_listening');
    } else {
      socket.emit('start_listening');
    }
  };

  const sendTextCommand = () => {
    if (!textInput.trim() || !socket || !isConnected) return;
    
    socket.emit('send_text_command', { command: textInput });
    setTextInput('');
  };

  const initializeVega = () => {
    if (socket && isConnected) {
      socket.emit('initialize_vega');
    }
  };

  const clearHistory = () => {
    if (socket && isConnected) {
      socket.emit('clear_chat_history');
    }
  };

  return (
    <div className="vega-app">
      {/* Animated Background */}
      <AnimatedBackground />
      
      {/* Header */}
      <motion.header 
        className="vega-header"
        initial={{ opacity: 0, y: -100 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 1, type: "spring", stiffness: 100 }}
      >
        <motion.div
          className="vega-title"
          animate={{ 
            backgroundPosition: ['0% 50%', '100% 50%', '0% 50%'],
          }}
          transition={{ 
            duration: 4,
            repeat: Infinity,
            ease: "easeInOut"
          }}
        >
          V.E.G.A
        </motion.div>
        <motion.p 
          className="vega-subtitle"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.5, duration: 0.8 }}
        >
          Voice-Enabled Genius Assistant
        </motion.p>
        
        <motion.div 
          className={`connection-indicator ${isConnected ? 'connected' : 'disconnected'}`}
          initial={{ scale: 0 }}
          animate={{ scale: 1 }}
          transition={{ delay: 1, type: "spring" }}
        >
          <div className={`status-dot ${isConnected ? 'online' : 'offline'}`}></div>
          {connectionStatus}
        </motion.div>
      </motion.header>

      {/* Main Content */}
      <main className="vega-main">
        <div className="vega-container">
          
          {/* Voice Visualizer Section */}
          <div className="visualizer-section">
            <VoiceVisualizer 
              isListening={isListening} 
              isSpeaking={isSpeaking} 
              isConnected={isConnected}
            />
            
            {/* Control Panel */}
            <div className="control-panel">
              <motion.button
                className={`mic-button ${
                  isListening ? 'listening' : 
                  isSpeaking ? 'speaking' : 
                  isConnected ? 'ready' : 'disabled'
                }`}
                whileHover={isConnected ? { scale: 1.1 } : {}}
                whileTap={isConnected ? { scale: 0.9 } : {}}
                onClick={toggleListening}
                disabled={!isConnected || isSpeaking}
                animate={isListening ? { 
                  boxShadow: [
                    "0 0 20px rgba(34, 197, 94, 0.3)",
                    "0 0 40px rgba(34, 197, 94, 0.6)",
                    "0 0 20px rgba(34, 197, 94, 0.3)"
                  ]
                } : isSpeaking ? {
                  boxShadow: [
                    "0 0 20px rgba(59, 130, 246, 0.3)",
                    "0 0 40px rgba(59, 130, 246, 0.6)",
                    "0 0 20px rgba(59, 130, 246, 0.3)"
                  ]
                } : {}}
                transition={{ duration: 1.5, repeat: (isListening || isSpeaking) ? Infinity : 0 }}
              >
                {isListening ? '🛑' : '🎤'}
              </motion.button>
              
              <motion.div 
                className="status-display"
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.3 }}
              >
                {isSpeaking ? '🤖 VEGA is responding...' :
                 isListening ? '🎤 Listening for your command...' :
                 isConnected ? '✨ Ready to assist you' : '🔄 Connecting to VEGA...'}
              </motion.div>
              
              <div className="action-buttons">
                <motion.button
                  className="action-btn initialize-btn"
                  onClick={initializeVega}
                  disabled={!isConnected}
                  whileHover={isConnected ? { scale: 1.05, y: -2 } : {}}
                  whileTap={isConnected ? { scale: 0.95 } : {}}
                >
                  🚀 Initialize VEGA
                </motion.button>
              </div>
            </div>
          </div>

          {/* Chat Interface */}
          <div className="chat-section">
            <motion.div 
              className="chat-container"
              initial={{ opacity: 0, x: 100 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.8, delay: 0.2 }}
            >
              <div className="chat-header">
                <h3>💬 Conversation</h3>
                <button onClick={clearHistory} className="clear-btn" disabled={!isConnected}>
                  🗑️ Clear
                </button>
              </div>
              
              <ChatMessages messages={messages} />
              
              <div className="chat-input-section">
                <input
                  type="text"
                  value={textInput}
                  onChange={(e) => setTextInput(e.target.value)}
                  onKeyPress={(e) => e.key === 'Enter' && sendTextCommand()}
                  placeholder="Type your command here..."
                  disabled={!isConnected}
                  className="chat-input"
                />
                <motion.button 
                  onClick={sendTextCommand}
                  disabled={!isConnected || !textInput.trim()}
                  className="send-btn"
                  whileHover={isConnected && textInput.trim() ? { scale: 1.1 } : {}}
                  whileTap={isConnected && textInput.trim() ? { scale: 0.9 } : {}}
                >
                  📤
                </motion.button>
              </div>
            </motion.div>
          </div>
        </div>
      </main>
    </div>
  );
}

// Advanced Voice Visualizer Component
function VoiceVisualizer({ isListening, isSpeaking, isConnected }) {
  return (
    <div className="voice-visualizer">
      
      {/* Outer Animated Rings */}
      <AnimatePresence>
        {(isListening || isSpeaking) && (
          <>
            {[1, 2, 3, 4].map((ring) => (
              <motion.div
                key={ring}
                className={`visualizer-ring ring-${ring} ${
                  isSpeaking ? 'speaking' : 'listening'
                }`}
                initial={{ scale: 0, opacity: 0 }}
                animate={{
                  scale: [0.8, 1.2, 0.8],
                  opacity: [0.2, 0.6, 0.2],
                  rotate: ring % 2 === 0 ? 360 : -360,
                }}
                exit={{ scale: 0, opacity: 0 }}
                transition={{
                  duration: 2 + ring * 0.3,
                  repeat: Infinity,
                  ease: "easeInOut",
                  delay: ring * 0.1,
                }}
              />
            ))}
          </>
        )}
      </AnimatePresence>

      {/* Central Core */}
      <motion.div
        className={`visualizer-core ${
          isSpeaking ? 'speaking' : 
          isListening ? 'listening' : 
          isConnected ? 'connected' : 'disconnected'
        }`}
        animate={{
          scale: isSpeaking ? [1, 1.3, 1] : isListening ? [1, 1.15, 1] : 1,
          rotate: isConnected ? 360 : 0,
        }}
        transition={{
          scale: {
            duration: 1.5,
            repeat: (isListening || isSpeaking) ? Infinity : 0,
            ease: "easeInOut"
          },
          rotate: {
            duration: 20,
            repeat: isConnected ? Infinity : 0,
            ease: "linear"
          }
        }}
      >
        <motion.div
          className="core-icon"
          animate={isSpeaking ? {
            rotate: [0, 10, -10, 0],
          } : {}}
          transition={{ duration: 0.5, repeat: isSpeaking ? Infinity : 0 }}
        >
          {isSpeaking ? '🔊' : isListening ? '🎤' : isConnected ? '🤖' : '😴'}
        </motion.div>
      </motion.div>

      {/* Sound Wave Bars for Speaking */}
      <AnimatePresence>
        {isSpeaking && (
          <div className="sound-waves">
            {[...Array(8)].map((_, i) => (
              <motion.div
                key={i}
                className="wave-bar"
                style={{
                  left: `${40 + i * 2.5}%`,
                  height: `${20 + i * 8}px`,
                }}
                initial={{ scaleY: 0.3, opacity: 0 }}
                animate={{ 
                  scaleY: [0.3, 2.5, 0.3],
                  opacity: [0.4, 1, 0.4],
                }}
                exit={{ scaleY: 0.3, opacity: 0 }}
                transition={{
                  duration: 0.8,
                  repeat: Infinity,
                  delay: i * 0.1,
                  ease: "easeInOut"
                }}
              />
            ))}
          </div>
        )}
      </AnimatePresence>

      {/* Particle Effects */}
      <div className="particle-container">
        {[...Array(12)].map((_, i) => (
          <motion.div
            key={i}
            className="particle"
            style={{
              left: `${Math.random() * 100}%`,
              top: `${Math.random() * 100}%`,
            }}
            animate={{
              y: [-20, -80, -20],
              opacity: [0, 0.8, 0],
              scale: [0.5, 1.2, 0.5],
            }}
            transition={{
              duration: 3 + Math.random() * 2,
              repeat: Infinity,
              delay: Math.random() * 2,
              ease: "easeInOut"
            }}
          />
        ))}
      </div>
    </div>
  );
}

// Enhanced Chat Messages Component
function ChatMessages({ messages }) {
  const messagesEndRef = useRef(null);
  const chatContainerRef = useRef(null);

  useEffect(() => {
    if (messagesEndRef.current) {
      messagesEndRef.current.scrollIntoView({ behavior: "smooth" });
    }
  }, [messages]);

  return (
    <div className="chat-messages" ref={chatContainerRef}>
      <AnimatePresence initial={false}>
        {messages.map((message, index) => (
          <motion.div
            key={message.id}
            className={`message ${message.type}`}
            initial={{ opacity: 0, y: 50, scale: 0.8 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, scale: 0.5, transition: { duration: 0.2 } }}
            transition={{ 
              duration: 0.4, 
              delay: index * 0.05,
              type: "spring",
              stiffness: 200,
              damping: 20
            }}
            whileHover={{ scale: 1.02, transition: { duration: 0.2 } }}
          >
            <div className="message-header">
              <span className="sender-info">
                <span className="sender-avatar">
                  {message.type === 'user' ? '👤' : 
                   message.type === 'assistant' ? '🤖' : '⚙️'}
                </span>
                <span className="sender-name">
                  {message.type === 'user' ? 'You' : 
                   message.type === 'assistant' ? 'VEGA' : 'System'}
                </span>
              </span>
              <span className="timestamp">
                {new Date(message.timestamp).toLocaleTimeString()}
              </span>
            </div>
            <motion.div 
              className="message-content"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ delay: 0.1 }}
            >
              {message.text}
            </motion.div>
          </motion.div>
        ))}
      </AnimatePresence>
      <div ref={messagesEndRef} />
    </div>
  );
}

// Animated Background Component
function AnimatedBackground() {
  return (
    <div className="animated-background">
      {/* Flowing Gradient Waves */}
      <div className="gradient-waves">
        {[...Array(3)].map((_, i) => (
          <motion.div
            key={i}
            className={`gradient-wave wave-${i + 1}`}
            animate={{
              x: [-100, 100, -100],
              scale: [1, 1.2, 1],
              opacity: [0.3, 0.6, 0.3],
            }}
            transition={{
              duration: 8 + i * 2,
              repeat: Infinity,
              ease: "easeInOut",
              delay: i * 1.5,
            }}
          />
        ))}
      </div>

      {/* Floating Particles */}
      <div className="floating-particles">
        {[...Array(25)].map((_, i) => (
          <motion.div
            key={i}
            className="floating-particle"
            style={{
              left: `${Math.random() * 100}%`,
              top: `${Math.random() * 100}%`,
            }}
            animate={{
              y: [-30, -120, -30],
              x: [-20, 20, -20],
              opacity: [0, 1, 0],
              scale: [0.5, 1.5, 0.5],
            }}
            transition={{
              duration: 4 + Math.random() * 3,
              repeat: Infinity,
              delay: Math.random() * 3,
              ease: "easeInOut"
            }}
          />
        ))}
      </div>

      {/* Grid Pattern */}
      <motion.div 
        className="grid-pattern"
        animate={{ opacity: [0.1, 0.3, 0.1] }}
        transition={{ duration: 4, repeat: Infinity }}
      />
    </div>
  );
}

export default App;