import cv2
import pyttsx3
import speech_recognition as sr
import threading
import time

# Initialize TTS engine
engine = pyttsx3.init()

# Initialize variables
video_thread = None
stop_video = False

# Function to handle speech recognition
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"Recognized: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError:
            print("Sorry, there was an error with the speech recognition service.")
        return ""

# Function to generate speech from text
def generate_speech(text):
    engine.say(text)
    engine.runAndWait()

# Function to capture video
def capture_video():
    global stop_video
    cap = cv2.VideoCapture(0)
    while True:
        if stop_video:
            break
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Video Capture', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# Main function
def main():
    global video_thread, stop_video
    while True:
        # Start video capture in a separate thread
        stop_video = False
        video_thread = threading.Thread(target=capture_video)
        video_thread.start()
        
        # Recognize speech
        text = recognize_speech()
        
        # Wait for 3 seconds
        time.sleep(3)
        
        # Stop video capture
        stop_video = True
        video_thread.join()

        # Generate speech response
        response = "You said: " + text
        generate_speech(response)

if __name__ == "__main__":
    main()
