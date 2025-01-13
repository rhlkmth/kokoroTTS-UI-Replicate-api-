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

# --- Sidebar ---
with st.sidebar:
    st.title("Replicate TTS App")
    st.markdown(
        "This app uses the [Replicate API](https://replicate.com/) to generate speech from text using the [jaaari/kokoro-82m](https://replicate.com/jaaari/kokoro-82m) model."
    )
    st.markdown("---")
    st.header("Model Parameters")
    available_voices = [
        'af',  # Default voice is a 50-50 mix of Bella & Sarah
        'af_bella', 'af_sarah', 'am_adam', 'am_michael',
        'bf_emma', 'bf_isabella', 'bm_george', 'bm_lewis',
        'af_nicole', 'af_sky',
    ]
    selected_voice = st.selectbox(
        "Select Voice",
        available_voices,
        index=0,
    )
    speech_speed = st.slider(
        "Speech Speed", min_value=0.1, max_value=5.0, value=0.95, step=0.05
    )
    st.markdown("---")
    st.markdown(
        "**Enter your Replicate API Token below:** This token is needed to authenticate with the Replicate API."
    )
    replicate_api_token_input = st.text_input(
        "Replicate API Token",
        type="password",
        placeholder="r8_...",
        help="Find your API token at https://replicate.com/account/api_tokens",
    )

# --- Main Section ---
st.title("Text to Speech Generator")

text_input = st.text_area(
    "Enter text to synthesize:",
    height=300,
    placeholder="Type your text here...",
)

if st.button("Generate Speech"):
    if not replicate_api_token_input:
        st.error("Please enter your Replicate API Token in the sidebar.")
    elif not text_input:
        st.warning("Please enter some text to generate speech.")
    else:
        with st.spinner("Generating speech..."):
            try:
                client = replicate.Client(api_token=replicate_api_token_input)
                input = {
                    "text": text_input,
                    "speed": speech_speed,
                    "voice": selected_voice,
                }
                output = client.run(
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
