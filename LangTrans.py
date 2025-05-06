import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import tempfile
import os

language = {
    "bn": "Bengali", "en": "English", "ko": "Korean", "fr": "French",
    "de": "German", "he": "Hebrew", "hi": "Hindi", "it": "Italian",
    "ja": "Japanese", "la": "Latin", "ms": "Malay", "ne": "Nepali",
    "ru": "Russian", "ar": "Arabic", "zh": "Chinese", "es": "Spanish"
}
language_reverse = {v: k for k, v in language.items()}

st.set_page_config(page_title="🈯 Language Translator", layout="centered")
st.title("🈯 Language Translator")

source_lang = st.selectbox("Select Source Language", ["Select Language"] + list(language.values()))
if source_lang != "Select Language":
    source_code = language_reverse[source_lang]

target_lang = st.selectbox("Select Target Language", ["Select Language"] + list(language.values()))
if target_lang != "Select Language":
    target_code = language_reverse[target_lang]

text_to_translate = st.text_area("Enter text to translate:")


if st.button("Translate"):
    if text_to_translate.strip() == "":
        st.error("⚠️ Please enter some text to translate.")
    else:
        try:
            translated = GoogleTranslator(
                source=language_reverse[source_lang],
                target=language_reverse[target_lang]
            ).translate(text_to_translate)

            st.success(f"Translated to {target_lang}:")
            st.write(f"**Input:** {text_to_translate}")
            st.write(f"**Translation:** {translated}")
            
        except Exception as e:
            st.error(f"❌ Error during translation: {e}")
