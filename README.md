# V.E.G.A - Voice-Enabled Genius Assistant

<div align="center">

![VEGA Logo](https://img.shields.io/badge/V.E.G.A-Voice%20Assistant-blue?style=for-the-badge&logo=react&logoColor=white)

**A Modern Voice Assistant with Real-time Speech Recognition and Animated UI**

[![React](https://img.shields.io/badge/React-18.2.0-61DAFB?style=flat&logo=react&logoColor=white)](https://reactjs.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.3-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Socket.IO](https://img.shields.io/badge/Socket.IO-5.3.6-010101?style=flat&logo=socket.io&logoColor=white)](https://socket.io/)
[![Framer Motion](https://img.shields.io/badge/Framer%20Motion-10.16.16-0055FF?style=flat&logo=framer&logoColor=white)](https://www.framer.com/motion/)
[![Railway](https://img.shields.io/badge/Deploy-Railway-0B0D0E?style=flat&logo=railway&logoColor=white)](https://railway.app/)

</div>

## 🌟 Overview

VEGA (Voice-Enabled Genius Assistant) is a sophisticated voice assistant featuring real-time speech recognition, animated UI components, and a powerful command processing system. Built with React frontend and Flask-SocketIO backend, it provides seamless voice interactions with stunning visual feedback.

### ✨ Key Features

- **🎤 Real-time Voice Recognition** - Live speech-to-text with instant feedback
- **🎨 Animated Voice Visualizer** - Dynamic wave patterns and particle effects
- **💬 Dual Input Methods** - Voice commands + text input fallback
- **🔄 WebSocket Communication** - Real-time bidirectional messaging
- **📱 Responsive Design** - Works on desktop, tablet, and mobile
- **🚀 Easy Deployment** - Single-click Railway deployment
- **🎭 Multiple Voice States** - Listening, speaking, idle with visual indicators
- **📝 Command History** - Persistent conversation tracking

## 🖼️ Screenshots

### Main Interface - Idle State
<!-- Add screenshot here -->
*VEGA's main interface showing the animated voice visualizer in idle state*

### Listening State
<!-- Add screenshot here -->
*Green animated rings indicate VEGA is actively listening for commands*

### Speaking State
<!-- Add screenshot here -->
*Blue sound wave bars animate while VEGA responds to user queries*

### Command Input Interface
<!-- Add screenshot here -->
*Minimal command input box for text-based interactions*

### Mobile Responsive View
<!-- Add screenshot here -->
*VEGA's interface optimized for mobile devices*

### Railway Deployment Dashboard
<!-- Add screenshot here -->
*Railway project showing both frontend and backend services*

## 🛠️ Tech Stack

### Frontend
- **React 18.2.0** - Modern UI library with hooks
- **Framer Motion 10.16.16** - Advanced animation library
- **Socket.IO Client 4.8.1** - Real-time WebSocket communication
- **Modern CSS3** - Custom animations and responsive design
- **Web Speech API** - Browser-native speech recognition

### Backend
- **Flask 3.0.3** - Lightweight Python web framework
- **Flask-SocketIO 5.3.6** - WebSocket support for Flask
- **Eventlet 0.36.1** - Async networking library
- **Gunicorn 21.2.0** - Production WSGI server
- **Python Speech Libraries** - Speech synthesis and recognition

### Deployment & Infrastructure
- **Railway** - Cloud platform for full-stack deployment
- **GitHub** - Version control and CI/CD integration
- **HTTPS/WSS** - Secure communication protocols

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
│   ├── Procfile              # Railway deployment config
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

## 🚀 Quick Start

### Prerequisites

- **Node.js** 16+ and npm
- **Python** 3.9+ and pip
- **Git** for version control
- **Microphone** for voice input (optional)

### Local Development

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/vega-voice-assistant.git
   cd vega-voice-assistant
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
   # Edit .env with your configuration
   ```

4. **Start Backend Server**
   ```bash
   python app.py
   ```
   Server runs on `http://localhost:5000`

5. **Setup Frontend** (New Terminal)
   ```bash
   cd frontend
   npm install
   npm start
   ```
   Frontend runs on `http://localhost:3000`

6. **Test the Application**
   - Open `http://localhost:3000` in your browser
   - Allow microphone permissions when prompted
   - Click the microphone button or type commands
   - Verify WebSocket connection indicator shows "Connected"

## 🎯 Available Commands

### Basic Commands
- **"What time is it?"** - Get current time
- **"What's the date today?"** - Get current date
- **"Hello"** / **"Hi"** - Greeting interaction
- **"Help"** - Show available commands
- **"Exit"** / **"Goodbye"** - End session

### Information & Search
- **"Tell me about [topic]"** - Wikipedia search
- **"Google search [query]"** - Web search
- **"Wikipedia [topic]"** - Direct Wikipedia lookup

### Entertainment
- **"Tell me a joke"** - Random joke
- **"Remember [note]"** - Save a note
- **"What do you remember?"** - Recall saved notes

### System Control
- **"Take a screenshot"** - Capture screen
- **"Show system status"** - CPU and battery info
- **"Play music [song]"** - Music playback
- **"Send email"** - Email composition

### Advanced Commands
- **"Shutdown system"** - System shutdown
- **"Restart system"** - System restart
- **"Logout"** - User logout

## 🎨 UI Features

### Voice Visualizer
- **Idle State**: Subtle glow with rotating icon
- **Listening State**: Green animated rings expanding outward
- **Speaking State**: Blue sound wave bars with pulsing animation
- **Error State**: Red indicators with error messaging

### Animations
- **Entrance Animations**: Smooth fade-in and slide effects
- **Hover Effects**: Scale and glow transformations
- **Particle System**: Floating elements for visual depth
- **Background Waves**: Dynamic gradient animations
- **State Transitions**: Seamless visual state changes

### Responsive Design
- **Desktop**: Full dual-pane layout with large visualizer
- **Tablet**: Stacked layout with medium visualizer
- **Mobile**: Compact single-column design
- **Touch-Friendly**: Large buttons and touch targets

## 🔧 Configuration

### Environment Variables

#### Backend (.env)
```bash
# Required
FLASK_SECRET_KEY=your-secret-key-here
FRONTEND_ORIGIN=http://localhost:3000

# Optional API Keys
GOOGLE_API_KEY=your-google-api-key
EMAIL_PASSWORD=your-email-password
```

#### Frontend (Railway/Vercel)
```bash
REACT_APP_BACKEND_URL=https://your-backend-domain.com
```

### Speech Recognition Settings
```python
# In utils/speech.py
MICROPHONE_TIMEOUT = 5      # Seconds to wait for speech
PHRASE_TIME_LIMIT = 10      # Max recording duration
ENERGY_THRESHOLD = 300      # Microphone sensitivity
```

### UI Customization
```css
/* In src/App.css */
:root {
  --primary-color: #3b82f6;    /* Blue theme */
  --secondary-color: #06b6d4;  /* Cyan accent */
  --success-color: #22c55e;    /* Green for listening */
  --error-color: #ef4444;      /* Red for errors */
  --background-gradient: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
}
```

## 🚀 Deployment Guide

### Railway Deployment (Recommended)

#### Method 1: Monorepo (Two Services)

1. **Prepare Repository**
   ```bash
   git add .
   git commit -m "Prepare for Railway deployment"
   git push origin main
   ```

2. **Create Railway Project**
   - Go to [Railway](https://railway.app)
   - Connect GitHub account
   - Create "New Project" → "Deploy from GitHub"

3. **Deploy Backend Service**
   - Select your repository
   - Set **Root Directory**: `backend`
   - Railway auto-detects Python and uses Procfile
   - Note the generated domain (e.g., `backend-production-xxxx.up.railway.app`)

4. **Configure Backend Environment**
   ```
   FLASK_SECRET_KEY=your-secret-key
   FRONTEND_ORIGIN=https://your-frontend-domain.com
   ```

5. **Deploy Frontend Service**
   - Add new service to same project
   - Set **Root Directory**: `frontend`
   - Railway auto-detects React
   - Note the generated domain

6. **Update Frontend Environment**
   ```
   REACT_APP_BACKEND_URL=https://your-backend-domain.com
   ```

7. **Update Backend CORS**
   - Set `FRONTEND_ORIGIN` to actual frontend domain
   - Redeploy backend service

#### Method 2: Single Service (Flask serves React)

1. **Modify Backend Structure**
   ```python
   # In app.py, add static file serving
   @app.route('/', defaults={'path': ''})
   @app.route('/<path:path>')
   def serve_spa(path):
       if path != "" and os.path.exists(app.static_folder + '/' + path):
           return send_from_directory(app.static_folder, path)
       return send_from_directory(app.static_folder, 'index.html')
   ```

2. **Build and Copy Frontend**
   ```bash
   cd frontend
   npm run build
   cp -r build/* ../backend/static/
   ```

3. **Deploy Single Service**
   - Deploy with root directory as `backend`
   - No CORS configuration needed

### Alternative Deployment Options

#### Vercel + Railway
- **Frontend**: Deploy React to Vercel (automatic)
- **Backend**: Deploy Flask-SocketIO to Railway
- Configure CORS between domains

#### Heroku
- Add `runtime.txt` with Python version
- Use similar Procfile configuration
- Configure Heroku environment variables

#### Docker Deployment
```dockerfile
# Dockerfile in project root
FROM node:18 as frontend-build
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm ci
COPY frontend/ ./
RUN npm run build

FROM python:3.11-slim
WORKDIR /app
COPY backend/requirements.txt ./
RUN pip install -r requirements.txt
COPY backend/ ./
COPY --from=frontend-build /app/frontend/build ./static
EXPOSE 5000
CMD ["gunicorn", "-k", "eventlet", "-w", "1", "-b", "0.0.0.0:5000", "app:app"]
```

## 🧪 Testing

### Frontend Tests
```bash
cd frontend
npm test
```

### Backend Tests
```bash
cd backend
python -m pytest tests/
```

### WebSocket Testing
```bash
# Use wscat for WebSocket testing
npm install -g wscat
wscat -c ws://localhost:5000/socket.io/?EIO=4&transport=websocket
```

### Voice Recognition Testing
1. Ensure microphone permissions are granted
2. Test with various command phrases
3. Verify confidence scoring in console logs
4. Test fallback to text input

## 🔍 Troubleshooting

### Common Issues

#### WebSocket Connection Failed
```
Error: WebSocket connection failed
```
**Solutions:**
- Verify CORS configuration in backend
- Check `FRONTEND_ORIGIN` environment variable
- Ensure Eventlet worker is used in production
- Confirm HTTPS/WSS protocols in production

#### Microphone Not Working
```
Error: Microphone access denied
```
**Solutions:**
- Allow microphone permissions in browser
- Use HTTPS for production (required for mic access)
- Test with different browsers
- Check microphone settings in OS

#### Build Failures
```
Error: Cannot resolve dependency
```
**Solutions:**
- Clear node_modules: `rm -rf node_modules package-lock.json && npm install`
- Update dependencies: `npm update`
- Check Node.js version compatibility
- Verify all dependencies are installed

#### Railway Deployment Issues
```
Error: Service failed to deploy
```
**Solutions:**
- Check Railway logs in dashboard
- Verify Procfile syntax
- Confirm requirements.txt is complete
- Check environment variables are set
- Ensure root directory is configured correctly

### Debug Mode

#### Backend Debug
```bash
export FLASK_DEBUG=1
python app.py
```

#### Frontend Debug
```bash
REACT_APP_DEBUG=true npm start
```

#### WebSocket Debug
```javascript
// In frontend App.js
const socket = io(BACKEND_URL, {
  debug: true,
  transports: ['websocket', 'polling']
});
```

### Performance Optimization

#### Backend
- Use single Eventlet worker for WebSockets
- Enable gzip compression for API responses
- Implement request rate limiting
- Add Redis for session storage (optional)

#### Frontend
- Optimize bundle size with code splitting
- Use React.memo for expensive components
- Implement virtual scrolling for large chat histories
- Compress images and assets

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the Repository**
   ```bash
   git fork https://github.com/yourusername/vega-voice-assistant.git
   ```

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/amazing-new-feature
   ```

3. **Make Changes**
   - Follow existing code style
   - Add tests for new functionality
   - Update documentation as needed

4. **Test Changes**
   ```bash
   npm test
   python -m pytest
   ```

5. **Submit Pull Request**
   - Describe changes clearly
   - Include screenshots if UI changes
   - Reference related issues

### Development Guidelines

- **Code Style**: Use ESLint for JavaScript, PEP 8 for Python
- **Commits**: Use conventional commit messages
- **Testing**: Maintain test coverage above 80%
- **Documentation**: Update README for new features

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

### Technologies
- **Flask-SocketIO** - Real-time WebSocket communication
- **Framer Motion** - Advanced React animations
- **Web Speech API** - Browser speech recognition
- **Railway** - Seamless deployment platform

### Inspiration
- Modern voice assistants (Siri, Alexa, Google Assistant)
- Sci-fi voice interfaces and holographic displays
- Real-time communication applications

### Community
- React community for excellent documentation and examples
- Flask-SocketIO maintainers for WebSocket implementation
- Railway team for developer-friendly deployment tools

## 📞 Support

### Get Help
- **Issues**: [GitHub Issues](https://github.com/yourusername/vega-voice-assistant/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/vega-voice-assistant/discussions)
- **Email**: support@vega-assistant.com (if available)

### Documentation
- **API Documentation**: Available in `/docs` directory
- **Deployment Guide**: See deployment section above
- **Video Tutorials**: Coming soon

### Community
- **Discord**: Join our community server (link TBD)
- **Twitter**: Follow [@VEGAAssistant](https://twitter.com/vegaassistant) for updates

---

<div align="center">

**Made with ❤️ by [Your Name]**

⭐ **Star this repo if you find it helpful!** ⭐

</div>