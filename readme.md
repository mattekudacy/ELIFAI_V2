# ELIFAI Documentation

Welcome to the official documentation for ELIFAI, your intelligent virtual assistant powered by GPT-4 Turbo!

## Overview

ELIFAI is an interactive and educational project designed to provide users with informative and playful responses to a variety of questions. It was inspired from the ELI5(Explain like I'm 5) subreddit. This project was submitted as a prototype for the **lablab: NextGen GPT AI Hackathon** This document also serves as a comprehensive guide to help users understand the features, architecture, and usage of ELIFAI.

## Features

### 1. Question & Answer

Ask ELIFAI anything, from science and technology to general knowledge, and receive responses tailored to your inquiries.

### 2. Educational Emojis

ELIFAI leverages emojis and images to deliver answers in a playful and engaging manner, making it especially suitable for a younger audience.

### 3. Real-time Chat Interface

Engage with ELIFAI through an interactive chat interface, receiving answers in real-time and fostering an immersive user experience.

### 4. Disclaimer

**Please Note:** ELIFAI's responses are generated based on predefined models and should not be considered as professional advice. Users are encouraged to use their discretion and verify information independently if needed.

## How to Use

1. **Select Option:** Choose "ELIFAI" from the sidebar to start interacting with chatbot.
2. **Ask Questions:** Engage with ELIFAI by typing your questions into the chat input box.
3. **Explore Answers:** Receive responses in the chat interface, incorporating informative and entertaining content.

## Project Structure

### 1. Dependencies

ELIFAI mainly relies on the following dependencies:
- `streamlit`: The primary framework for building the user interface.
- `clarifai-grpc`: Used for making API calls to Clarifai for natural language processing.

### 2. API Integration

ELIFAI integrates with Clarifai's to access the OpenAI models avaialble in the platform.

### 3. Session Management

User chat history is managed using Streamlit's session state, providing a seamless and personalized experience across interactions.

## Usage

Before you proceed, make sure you have a Clarifiai account to access the GPT-4 Model and other environment variables.

1. Clone the reposority
```bash
git clone https://github.com/mattekudacy/ELIFAI_V2.git
```

2. Install the requirements.

```bash
pip install requirements.txt
```

3. Create your <code>secrets.toml</code> file and put the following:
```python
#for text generation
PAT = 'your-pat-key'
USER_ID = 'your-user-id'
APP_ID = 'your-app-id'
MODEL_ID = 'gpt-4-turbo'
MODEL_VERSION_ID = 'model-version-id'

#for image generation
DAPP_ID = st.secrets.DAPP_ID
DMODEL_ID =  st.secrets.DMODEL_ID
DMODEL_VERSION_ID = st.secrets.DMODEL_VERSION_ID
```
- To see your PAT key, navigate to Profile -> Security -> Personal Access Token->
- For the other details, simply find the GPT-4 and DALL-E 3 model in the "Community" section, and click the "Use Model" button. The first few lines will reveal the USER_ID, APP_ID, MODEL_ID, and MODEL_VERSION_ID.

4. Run the streamlit app
```bash
streamlit run app.py
```
Access the application in your browser at http://localhost:8501.

## Contributing
If you are interested in contributing to ELIFAI, please feel free to submit your PR's.

## License
ELIFAI is licensed under the MIT License.

## Acknowledgements
Special thanks to the lablab.ai for hosting the NextGen GPT Hackathon, you made it possible for me to explore OpenAI models. And also to Streamlit and Clarifai communities for their support and contribution to open-source projects.

Enjoy your journey with ELIFAI, and happy exploring!
