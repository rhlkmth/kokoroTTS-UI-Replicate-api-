import streamlit as st
import replicate
import os

# --- Page Configuration ---
st.set_page_config(
    page_title="Streamlit TTS with Replicate",
    page_icon="🗣️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Get API Token from Streamlit Secrets (Recommended for Deployment) ---
REPLICATE_API_TOKEN = st.secrets.get("REPLICATE_API_TOKEN")

if not REPLICATE_API_TOKEN:
    st.error("Please set the `REPLICATE_API_TOKEN` secret in your Streamlit app's settings.")
    st.stop()

replicate_client = replicate.Client(api_token=REPLICATE_API_TOKEN)

# --- Sidebar ---
with st.sidebar:
    st.title("Replicate TTS App")
    st.markdown(
        "This app uses the [Replicate API](https://replicate.com/) to generate speech from text using the [jaaari/kokoro-82m](https://replicate.com/jaaari/kokoro-82m) model."
    )
    st.markdown("---")
    st.header("Model Parameters")
    selected_voice = st.selectbox(
        "Select Voice",
        ["af_bella", "en_us_jesse", "en_us_mickey", "ja_kokoro", "zh_mandarin"],
        index=0,
    )
    speech_speed = st.slider(
        "Speech Speed", min_value=0.1, max_value=5.0, value=0.95, step=0.05
    )
    st.markdown("---")
    st.markdown(
        "**Deployment Note:** This app needs to be deployed on a platform that can run Python code (e.g., Streamlit Cloud)."
    )
    st.markdown(
        "Set your Replicate API token as a **secret** in your deployment platform's settings (e.g., Streamlit Secrets)."
    )

# --- Main Section ---
st.title("Text to Speech Generator")

text_input = st.text_area(
    "Enter text to synthesize:",
    height=300,
    placeholder="Type your text here...",
)

if st.button("Generate Speech"):
    if not text_input:
        st.warning("Please enter some text to generate speech.")
    else:
        with st.spinner("Generating speech..."):
            try:
                input = {
                    "text": text_input,
                    "speed": speech_speed,
                    "voice": selected_voice,
                }
                output = replicate_client.run(
                    "jaaari/kokoro-82m:dfdf537ba482b029e0a761699e6f55e9162cfd159270bfe0e44857caa5f275a6",
                    input=input,
                )

                if output:
                    # Fetch the audio data from the URL
                    import requests
                    audio_response = requests.get(output)
                    audio_data = audio_response.content
                    st.audio(audio_data, format="audio/wav")
                    st.success("Speech generated successfully!")
                else:
                    st.error("Failed to generate speech. Output was empty.")

            except Exception as e:
                st.error(f"An error occurred: {e}")

# --- Footer ---
st.markdown("---")
st.caption("Powered by Replicate and Streamlit")
