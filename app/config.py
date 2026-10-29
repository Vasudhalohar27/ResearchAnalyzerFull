import os
from dotenv import load_dotenv

load_dotenv()

def get_setting(name, default=""):
    try:
        import streamlit as st
        value = st.secrets.get(name, None)
        if value is not None:
            return str(value)
    except Exception:
        pass

    return os.getenv(name, default)

GROQ_API_KEY = get_setting("GROQ_API_KEY").strip()
GROQ_MODEL = get_setting(
    "GROQ_MODEL",
    "openai/gpt-oss-20b"
).strip()

ENABLE_WEB_SEARCH = get_setting(
    "ENABLE_WEB_SEARCH",
    "true"
).lower() in {"1", "true", "yes"}