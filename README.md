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
