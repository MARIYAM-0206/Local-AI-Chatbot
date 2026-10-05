# 🤖 Local AI Chatbot

A lightweight, privacy-focused AI chatbot that runs locally on your computer using **Flask, Ollama, and Qwen 2.5 1.5B**.

No cloud AI API is required for inference. Once the required software and model are installed, the chatbot can run without an internet connection.

---

## ✨ Features

- 🧠 Local AI inference with Qwen 2.5 1.5B
- 🔒 Private local processing
- 🌐 Clean responsive web interface
- 💬 Conversation context for follow-up questions
- ⚡ Lightweight Flask backend
- 🖥️ Runs on Windows
- ☁️ No cloud AI API required
- 📱 Responsive interface for different screen sizes

---

## 🏗️ Architecture

```text
┌──────────────────────┐
│      Web Browser     │
│   Chat Interface     │
└──────────┬───────────┘
           │
           │ HTTP
           ▼
┌──────────────────────┐
│    Flask Backend     │
│      app.py          │
└──────────┬───────────┘
           │
           │ Local API
           ▼
┌──────────────────────┐
│        Ollama        │
│   Local AI Runtime   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   Qwen 2.5 1.5B      │
│    Local LLM Model   │
└──────────────────────┘
🛠️ Tech Stack
Technology
Purpose
Python
Application logic
Flask
Web backend and API bridge
HTML
Interface structure
CSS
Interface styling
JavaScript
Chat interaction
Ollama
Local LLM runtime
Qwen 2.5 1.5B
Language model
Git
Version control
🔒 Privacy & Offline Capability
The chatbot uses a locally installed language model through Ollama.
After the software, dependencies, and Qwen model have been downloaded, AI inference can be performed without an internet connection.
This means user prompts do not need to be sent to a cloud AI provider for inference.
Note: Internet access is still required during initial installation, dependency setup, and model download.
⚙️ How It Works
The user enters a message in the web interface.
JavaScript sends the message to the Flask /chat endpoint.
Flask sends the request to the locally running Ollama API.
Ollama runs Qwen 2.5 1.5B locally.
The generated response is returned to Flask.
Flask sends the response back to the browser.
The interface displays the response.
🚀 Getting Started
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/local-ai-chatbot.git
cd local-ai-chatbot
2. Create a virtual environment
python -m venv venv
Activate it on Windows:
venv\Scripts\activate
3. Install dependencies
pip install flask requests
4. Install Ollama
Install Ollama for Windows from the official Ollama website.
Then download the model:
ollama pull qwen2.5:1.5b
5. Start Ollama
Make sure Ollama is running.
6. Start Flask
python app.py
7. Open the chatbot
Open:
http://127.0.0.1:5000
💻 System Requirements
The project is designed to work with relatively modest hardware.
The development setup used:
Windows 11
Python 3.13
8 GB RAM
Intel integrated graphics
Qwen 2.5 1.5B
Because the model runs on CPU in this setup, response generation can take some time.
📁 Project Structure
local-ai-chatbot/
│
├── app.py
├── README.md
├── .gitignore
│
└── templates/
    └── index.html
🔮 Future Improvements
Possible future improvements include:
Persistent chat history
Conversation export
Copy-response button
Multiple local model support
Model selection
Streaming responses
Improved performance
Docker deployment
More advanced chat controls
🎯 Project Goal
This project was built to explore how modern AI applications can be developed using local language models rather than relying entirely on cloud-based AI APIs.
It combines a simple web application with a locally hosted LLM to create a private and lightweight AI chat experience.
👩‍💻 Author
Mariyam
BCA Student | Exploring Cloud Computing, AI & Data Engineering
📄 License
This project is available for learning and portfolio purposes.
