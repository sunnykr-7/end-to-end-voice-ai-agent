#  🎙️ End-to-End Voice AI Agent | Local Speech-to-Action System

## Overview
This project is a voice-controlled AI agent that:
- Converts audio to text
- Detects user intent using LLM
- Executes local tools
- Displays results via UI

Used local intent classification due to API quota limitations.

##  Why this project?

Voice interfaces are becoming a natural way to interact with AI systems.  
This project demonstrates how speech can be converted into real-world actions like file creation, code generation, and summarization using a fully local pipeline.

## Features
- Audio input (upload)
- Speech-to-text using Whisper
- Intent classification using LLM
- File creation and code generation
- Text summarization
- Streamlit UI

## Architecture

Audio → Whisper (STT) → Intent Detection → Tool Execution → Streamlit UI


## Tech Stack
- Python
- Streamlit
- Whisper (OpenAI)
- FFmpeg

## 📸 Demo Photo / Video

### Project Photo / Screenshots
https://drive.google.com/drive/u/1/folders/1dCXZYpz1C-x-ixuOJXnL7nzMbeXjlj2g


### 🎥 Demo Video (Complete Working Project Recorded Video)
https://drive.google.com/drive/u/1/folders/1twoSjvCeTvPjExt0ONvFmO3uBtu7SgTD



## Setup

```bash
pip install -r requirements.txt
streamlit run app.py
