# Voice-Controlled Local AI Agent

## Overview
This project is a voice-controlled AI agent that:
- Converts audio to text
- Detects user intent using LLM
- Executes local tools
- Displays results via UI

Used local intent classification due to API quota limitations.

## Features
- Audio input (upload)
- Speech-to-text using Whisper
- Intent classification using LLM
- File creation and code generation
- Text summarization
- Streamlit UI

## Tech Stack
- Python
- Streamlit
- Whisper (OpenAI)
- FFmpeg

## Setup

```bash
pip install -r requirements.txt
streamlit run app.py