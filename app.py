import streamlit as st
import cv2
import pyttsx3
import speech_recognition as sr
from PIL import Image

# Initialize TTS engine
engine = pyttsx3.init()

# Initialize Streamlit session state
if 'stop_video' not in st.session_state:
    st.session_state.stop_video = False

# Function to handle speech recognition
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            st.write(f"Recognized: {text}")
            return text
        except sr.UnknownValueError:
            st.write("Sorry, I did not understand that.")
        except sr.RequestError:
            st.write("Sorry, there was an error with the speech recognition service.")
        return ""

# Function to generate speech from text
def generate_speech(text):
    engine.say(text)
    engine.runAndWait()

# Function to capture and display a video frame
def capture_video_frame():
    url="http://192.168.29.128:8080/video"
    cap = cv2.VideoCapture(url)
    ret, frame = cap.read()
    cap.release()
    if ret:
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb)
        st.image(img, caption="Captured Video Frame", use_column_width=True)
    else:
        st.write("Failed to capture video frame.")

# Streamlit UI
st.title("Speech-to-Speech LLM Bot")

if st.button("Start"):
    capture_video_frame()
    
    # Recognize speech
    text = recognize_speech()

    # Generate and display speech response
    if text:
        response = "You said: " + text
        generate_speech(response)
        st.write(f"Response: {response}")
    else:
        st.write("No speech recognized.")

# Stop Button
if st.button("Stop"):
    st.session_state.stop_video = True
    st.write("Video capture stopped.")
