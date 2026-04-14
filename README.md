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
[https://drive.google.com/drive/u/1/folders/1sAoGqqV5Uj-ySsSX5DtsKmwEvmDJ65eH](https://drive.google.com/drive/u/1/folders/1CxgYGBWeY3A4-PFWL9zcS8olErkllCN3)


### 🎥 Demo Video (Complete Working Project Recorded Video)
G Drive Link - https://drive.google.com/file/d/1AAZiJEptlmd7ngFi1V4z1fnFk7-j4u90/view?usp=drive_link



## Setup

```bash
pip install -r requirements.txt
streamlit run app.py
