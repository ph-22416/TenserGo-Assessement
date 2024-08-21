# TenserGo-Assessement
Generate a Speech- to-Speech LLM Bot using technologies cv2, pyttsx3, speech_recognition, threading, time.

# Speech-to-Speech LLM Bot

This repository contains a Speech-to-Speech LLM bot that leverages computer vision, text-to-speech, and speech recognition to interact with users. The bot captures video and audio from the user, recognizes the spoken words, and responds by repeating the recognized words. The bot operates within a 3-second window to capture and process the input.

## Features

- **Speech Recognition:** The bot uses `speech_recognition` to capture and recognize spoken words from the user.
- **Text-to-Speech:** The recognized words are converted into speech using `pyttsx3`, enabling the bot to respond verbally.
- **Computer Vision:** The bot utilizes `cv2` (OpenCV) for capturing video from the user's camera, adding a visual aspect to the interaction.
- **Threading:** The application runs the speech recognition and video capture in parallel, ensuring a smooth user experience.

## Technologies Used
- **Python**: The core programming language used.
- **Streamlit**: For creating the UI in `app.py`.
- **OpenCV (`cv2`)**: For video capture and processing.
- **pyttsx3**: For text-to-speech conversion.
- **SpeechRecognition (`speech_recognition`)**: For capturing and recognizing speech.
- **Threading**: To run multiple tasks concurrently.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/ph-22416/speech-to-speech-llm-bot.git
    cd speech-to-speech-llm-bot
    ```
2. Install the required dependencies:
    ```bash
    pip install speechrecognition pyttsx3 opencv-python pyaudio numpy
    pip install streamlit
    ```
3. Run the application:
    ```bash
    streamlit run app.py
    ```

## How It Works
1. **UI Design (app.py)**: The user interface is created using Streamlit, where the speech recognition function is integrated and triggered.

2. **Speech Recognition (speech.py)**: The core logic for recognizing speech is implemented in `speech.py`. The function `recognize_speech()` captures the user's spoken words using `speech_recognition`. 

3. **Video Capture and Processing**: Using OpenCV (`cv2`), the bot opens a 3-second video window to capture the user's video input.

4. **Text-to-Speech Response**: After recognizing the speech, the bot responds with a verbal confirmation of what it recognized, using `pyttsx3` for text-to-speech conversion.

5. **Threading for Concurrency**: The bot uses threading to manage speech recognition and video capture concurrently, ensuring that the tasks run smoothly without blocking each other.

## Example
When the user speaks into their microphone, the bot will capture the video and audio, recognize the spoken words, and respond with:
> "You said: [recognized words]"
> and then response it. 

## Contact
For any questions or inquiries, please reach out via [email](priyanshichaudhary2015@gmail.com).
