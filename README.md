# AI Prompt Enhancer Tool

A powerful web application that transforms simple prompts into professional, detailed, and optimized prompts using local AI (Ollama).

## Features

- Clean, modern UI with split-view design
- Real-time prompt enhancement using Ollama
- Copy to clipboard functionality
- Responsive design for all devices
- Error handling and status feedback

## Prerequisites

1. Python 3.8+
2. Ollama installed and running locally
3. Gemma2 model pulled in Ollama

## Setup Instructions

### 1. Install Ollama

Download and install from: https://ollama.ai

### 2. Pull the Gemma2 Model

```bash
ollama pull gemma2:2b
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

### 5. Access the App

Open your browser and navigate to: http://localhost:5000

## Usage

1. Enter your basic prompt in the left textarea
2. Click "Enhance Prompt" or press Ctrl+Enter
3. Wait for the AI to process (may take 10-30 seconds)
4. View the enhanced prompt on the right
5. Click "Copy to Clipboard" to use it elsewhere

## How It Works

- Backend: Flask handles requests and communicates with Ollama
- Frontend: Clean HTML/CSS/JS interface
- AI Model: Gemma2:2b running locally via Ollama
- Enhancement: AI applies prompt engineering best practices

## Troubleshooting

- **Cannot connect to Ollama**: Make sure Ollama is running (`ollama serve`)
- **Model not found**: Run `ollama pull gemma2:2b`
- **Timeout errors**: Increase timeout in app.py or use a smaller model

## Project Structure

```
.
├── app.py                 # Flask backend
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main HTML template
└── static/
    ├── style.css         # Styling
    └── script.js         # Frontend logic
```
