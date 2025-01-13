# Streamlit Text-to-Speech App with Replicate API

This is a Streamlit web application that uses the Replicate API to generate speech from text.

## Features

*   Takes text input from the user.
*   Allows the user to select from different voices.
*   Provides a slider to adjust the speech speed.
*   Plays the generated audio in the browser.

## Deployment

This application needs to be deployed on a platform that can run Python code. Here's how to deploy it using **Streamlit Cloud** (recommended):

1. **Sign up for a Streamlit Cloud account:** Go to [https://streamlit.io/cloud](https://streamlit.io/cloud) and create an account.
2. **Create a new repository on GitHub:** Upload the following files to your GitHub repository:
    *   `app.py`
    *   `requirements.txt`
    *   `.streamlit/secrets.toml` (with your Replicate API token)
3. **Connect your GitHub repository to Streamlit Cloud:**
    *   In your Streamlit Cloud dashboard, click on "New app".
    *   Select "From GitHub".
    *   Choose the repository and branch where you uploaded the files.
    *   Specify `app.py` as the main file.
4. **Configure Secrets:** Streamlit Cloud will automatically detect the `secrets.toml` file. Ensure your Replicate API token is correctly entered there.
5. **Deploy your app!** Click the "Deploy!" button.

Alternatively, you can deploy to other platforms like Heroku or PythonAnywhere, but the specific steps will vary. Make sure to configure environment variables or secrets on those platforms to securely store your `REPLICATE_API_TOKEN`.

## Local Development (Optional)

If you want to run the app locally for development:

1. **Make sure you have Python installed.**
2. **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```
3. **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Set your Replicate API token as an environment variable:**
    ```bash
    export REPLICATE_API_TOKEN=YOUR_REPLICATE_API_TOKEN  # Linux/macOS
    set REPLICATE_API_TOKEN=YOUR_REPLICATE_API_TOKEN  # Windows (Command Prompt)
    # Or use a .env file
    ```
5. **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

## API Token Security

**Important:**  Treat your Replicate API token like a password. Do not hardcode it directly into your `app.py` file. Using Streamlit Secrets (via `.streamlit/secrets.toml`) or environment variables is the secure way to handle this.
