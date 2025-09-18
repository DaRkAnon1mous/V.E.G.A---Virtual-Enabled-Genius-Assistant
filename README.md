# V.E.G.A - Voice-Enabled Genius Assistant

<div align="center">

![VEGA Logo](https://img.shields.io/badge/V.E.G.A-Voice%20Assistant-blue?style=for-the-badge&logo=react&logoColor=white)

**A Modern Voice Assistant with Real-Time Speech Recognition and Animated UI**

[![React](https://img.shields.io/badge/React-18.2.0-61DAFB?style=flat-square&logo=react&logoColor=white)](https://reactjs.org/)  
[![Flask](https://img.shields.io/badge/Flask-3.0.3-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)  
[![Socket.IO](https://img.shields.io/badge/Socket.IO-5.3.6-010101?style=flat-square&logo=socket.io&logoColor=white)](https://socket.io/)  
[![Framer Motion](https://img.shields.io/badge/Framer%20Motion-10.16.16-0055FF?style=flat-square&logo=framer&logoColor=white)](https://www.framer.com/motion/)  
[![Railway](https://img.shields.io/badge/Deploy-Railway-0B0D0E?style=flat-square&logo=railway&logoColor=white)](https://railway.app/)  
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

</div>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Screenshots](#-screenshots)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Local Development](#local-development)
- [Available Commands](#-available-commands)
- [UI Features](#-ui-features)
- [Configuration](#-configuration)
- [Deployment](#-deployment)
- [Testing](#-testing)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)
- [Support](#-support)

---

## 🌟 Overview

V.E.G.A (Voice-Enabled Genius Assistant) is an innovative voice assistant that combines real-time speech recognition with an animated, responsive user interface. Built using a React frontend and a Flask-SocketIO backend, V.E.G.A offers seamless voice interactions and stunning visual feedback, making it a modern alternative to traditional assistants.

---

## ✨ Features

- 🎤 **Real-Time Voice Recognition**: Instant speech-to-text with live feedback.
- 🎨 **Animated Voice Visualizer**: Dynamic wave patterns and particle effects.
- 💬 **Dual Input Methods**: Supports voice commands and text input fallback.
- 🔄 **WebSocket Communication**: Real-time, bidirectional messaging.
- 📱 **Responsive Design**: Optimized for desktop, tablet, and mobile devices.
- 🚀 **Easy Deployment**: One-click deployment via Railway.
- 🎭 **Multiple Voice States**: Visual indicators for listening, speaking, and idle states.
- 📝 **Command History**: Persistent tracking of conversations.

---

## 🖼️ Screenshots

| **State**                | **Description**                          | **Image**                     |
|---------------------------|------------------------------------------|--------------------------------|
| Main Interface - Idle     | Subtle glow with rotating icon.          | (<img width="1920" height="1200" alt="Screenshot (593)" src="https://github.com/user-attachments/assets/d1bc18e1-dc57-491f-aff7-323381baed28" />
)  |
| Listening State           | Green animated rings expanding outward.  | (<img width="1920" height="1200" alt="Screenshot (594)" src="https://github.com/user-attachments/assets/ca1fb498-316f-428b-bae3-498f79483f3b" />
) |
| Command Input Interface   | Minimal text input box.                  | (<img width="1920" height="1200" alt="Screenshot (595)" src="https://github.com/user-attachments/assets/4c7ca3e3-cf15-45d5-a7b0-2c0647ae9350" />
) |


---

## 🛠️ Tech Stack

### Frontend
- **[React 18.2.0](https://reactjs.org/)** - Modern UI library with hooks.
- **[Framer Motion 10.16.16](https://www.framer.com/motion/)** - Advanced animations.
- **[Socket.IO Client 4.8.1](https://socket.io/)** - Real-time WebSocket communication.
- **CSS3** - Custom animations and responsive design.
- **Web Speech API** - Browser-native speech recognition.

### Backend
- **[Flask 3.0.3](https://flask.palletsprojects.com/)** - Lightweight Python web framework.
- **[Flask-SocketIO 5.3.6](https://socket.io/)** - WebSocket support.
- **[Eventlet 0.36.1](https://eventlet.net/)** - Async networking.
- **[Gunicorn 21.2.0](https://gunicorn.org/)** - Production WSGI server.
- **Python Speech Libraries** - Speech synthesis and recognition (e.g., `pyttsx3`, `vosk`).

### Deployment & Infrastructure
- **[Railway](https://railway.app/)** - Cloud platform for deployment. (Still in progress)
- **[GitHub](https://github.com/)** - Version control and CI/CD.
- **HTTPS/WSS** - Secure communication.

---

## 📁 Project Structure

```
vega-voice-assistant/
├── README.md
├── LICENSE
├── .gitignore
│
├── backend/
│   ├── app.py                 # Main Flask-SocketIO server
│   ├── requirements.txt       # Python dependencies
│   ├── Procfile              # Deployment configuration
│   ├── .env.example          # Environment variables template
│   │
│   ├── utils/
│   │   └── speech.py         # Speech recognition & synthesis
│   │
│   └── skills/
│       ├── basic.py          # Time, date, greetings
│       ├── entertainment.py  # Jokes, reminders
│       ├── web.py           # Wikipedia, Google search
│       ├── communication.py  # Email handling
│       └── system_control.py # Screenshots, system info
│
└── frontend/
    ├── package.json          # React dependencies
    ├── public/
    │   └── index.html        # HTML template
    │
    └── src/
        ├── App.js            # Main React component
        ├── App.css           # Component styling
        ├── index.js          # React entry point
        └── index.css         # Global styles
```

---

## 🚀 Getting Started

### Prerequisites

- **Node.js** 16+ and npm
- **Python** 3.9+ and pip
- **Git** for version control
- **Microphone** (optional for voice input)

### Local Development

1. **Clone the Repository**
   ```bash
   git clone https://github.com/DaRkAnon1mous/V.E.G.A---Virtual-Enabled-Genius-Assistant.git
   cd V.E.G.A---Virtual-Enabled-Genius-Assistant
   ```

2. **Setup Backend**
   ```bash
   cd backend
   python -m venv vega_env
   source vega_env/bin/activate  # On Windows: vega_env\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration (e.g., FLASK_SECRET_KEY)
   ```

4. **Start Backend Server**
   ```bash
   python app.py
   ```
   *Server runs on `http://localhost:5000`*

5. **Setup Frontend** (New Terminal)
   ```bash
   cd frontend
   npm install
   npm start
   ```
   *Frontend runs on `http://localhost:3000`*

6. **Test the Application**
   - Open `http://localhost:3000` in your browser.
   - Allow microphone permissions if prompted.
   - Use the microphone button or text input to test commands.
   - Verify WebSocket connection status.

---

## 🎯 Available Commands

### Basic Commands
- `"What time is it?"` - Get current time.
- `"What's the date today?"` - Get current date.
- `"Hello"` / `"Hi"` - Greeting interaction.
- `"Help"` - List available commands.
- `"Exit"` / `"Goodbye"` - End session.

### Information & Search
- `"Tell me about [topic]"` - Wikipedia search.
- `"Google search [query]"` - Web search.
- `"Wikipedia [topic]"` - Direct Wikipedia lookup.

### Entertainment
- `"Tell me a joke"` - Random joke.
- `"Remember [note]"` - Save a note.
- `"What do you remember?"` - Recall notes.

### System Control
- `"Take a screenshot"` - Capture screen.
- `"Show system status"` - CPU and battery info.
- `"Play music [song]"` - Music playback.
- `"Send email"` - Email composition.

### Advanced Commands
- `"Shutdown system"` - System shutdown.
- `"Restart system"` - System restart.
- `"Logout"` - User logout.

---

## 🎨 UI Features

### Voice Visualizer
- **Idle State**: Subtle glow with rotating icon.
- **Listening State**: Green animated rings.
- **Speaking State**: Blue sound wave bars.
- **Error State**: Red indicators with messages.

### Animations
- Smooth fade-in/slide effects.
- Hover scale and glow transformations.
- Floating particle system.
- Dynamic background waves.
- Seamless state transitions.

### Responsive Design
- **Desktop**: Dual-pane layout with large visualizer.
- **Tablet**: Stacked layout with medium visualizer.
- **Mobile**: Compact single-column design.
- **Touch-Friendly**
