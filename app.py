import streamlit as st
import os

from utils.stt import transcribe_audio
from utils.llm import classify_intent, summarize_text, generate_code
from utils.tools import create_file, write_code

# Page config
st.set_page_config(page_title="Voice AI Agent", layout="centered")

st.title("🎙️ Voice AI Agent")
st.divider()

# Ensure output folder exists
if not os.path.exists("output"):
    os.makedirs("output")

uploaded_file = st.file_uploader("Upload Audio", type=["wav", "mp3"])

if uploaded_file:
    file_path = f"temp_{uploaded_file.name}"

    # Save uploaded file
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.info("Transcribing...")

    # Step 1: Speech to Text
    text = transcribe_audio(file_path)

    st.subheader("📝 Transcribed Text")
    st.write(text)

    st.divider()
    st.info("Classifying intent...")

    # Step 2: Intent Detection
    data = classify_intent(text)

    intent = data.get("intent", "")
    filename = data.get("filename", "output.txt")
    content = data.get("content", "")

    st.subheader("🎯 Intent")
    st.write(intent)

    st.write(f"📁 File: {filename}")

    st.divider()

    action_result = ""

    # Step 3: Execute Action
    if intent == "create_file":
        action_result = create_file(filename)

    elif intent == "write_code":
        code = generate_code(text)
        action_result = write_code(filename, code)

        st.subheader("💻 Generated Code")
        st.code(code)

    elif intent == "summarize":
        summary = summarize_text(text)
        action_result = "Text summarized"

        st.subheader("📄 Summary")
        st.write(summary)

    else:
        action_result = "General chat response"
        st.write(content)

    st.divider()

    # Step 4: Show Action Result
    st.subheader("⚙️ Action Taken")
    st.write(action_result)

    # Success message
    st.success("✅ Task completed successfully!")