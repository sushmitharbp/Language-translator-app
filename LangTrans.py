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

source_lang = st.selectbox("Select Source Language", list(language.values()))
target_lang = st.selectbox("Select Target Language", list(language.values()))
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

            if st.button("🔊 Listen to Translation"):
                tts = gTTS(translated, lang=language_reverse[target_lang])
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                    tts.save(fp.name)
                    st.audio(fp.name, format="audio/mp3")
        except Exception as e:
            st.error(f"❌ Error during translation: {e}")
