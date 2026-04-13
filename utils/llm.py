def classify_intent(text):
    text_lower = text.lower()

    # CREATE FILE
    if "create" in text_lower and "file" in text_lower:
        return {
            "intent": "create_file",
            "filename": "output.txt",
            "content": ""
        }

    # WRITE CODE
    elif ("write" in text_lower and "code" in text_lower) or "python" in text_lower:
        return {
            "intent": "write_code",
            "filename": "code.py",
            "content": text
        }

    # SUMMARIZE
    elif "summarize" in text_lower or "summary" in text_lower:
        return {
            "intent": "summarize",
            "filename": "",
            "content": text
        }

    # DEFAULT
    else:
        return {
            "intent": "chat",
            "filename": "",
            "content": text
        }


def generate_code(text):
    return f"""# Generated Code
# Task: {text}

def example():
    print("Hello from AI Agent")
"""


def summarize_text(text):
    return f"Summary: {text[:100]}..."