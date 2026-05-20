import speech_recognition as sr
import subprocess
import webbrowser
from google import genai
from google.genai import errors
from dotenv import load_dotenv
from musicLibrary import music_dict
import time
import os

load_dotenv()
client = genai.Client()

def speak(text):
    subprocess.run(["say", text])


def generate_gemini_response(input_text):
    # Skip processing if speech-to-text captured nothing
    if not input_text.strip():
        return "I didn't catch that."
        
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Answer in maximum 2 short sentences only: {input_text}",
        )
        return response.text
    except errors.ClientError as e:
        if e.code == 429:
            print("Rate limit reached. Waiting 5 seconds...")
            speak("Rate limit reached. Please hold on.")
            time.sleep(5)
            return "System is resetting, please try again."
        else:
            print(f"API Error: {e}")
            return "I encountered an API error."
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return "An unexpected error occurred."



r = sr.Recognizer()
m = sr.Microphone()

assistant_active = False


try:
    print("Adjusting for ambient noise...")

    with m as source:
        r.adjust_for_ambient_noise(source)

    print(f"Energy threshold set to {r.energy_threshold}")

    while True:
        try:
            with m as source:
                print("Listening...")
                audio = r.listen(source)

            value = r.recognize_google(audio)

            print(f"You said: {value}")

            # Wake word
            if not assistant_active and "jarvis" in value.lower():
                assistant_active = True
                speak("Hii Boss. Jarvis activated")
                continue

            # Command mode
            if assistant_active:
                print(f"Command received: {value}")

                if "stop" in value.lower():
                    speak("Deactivating")
                    assistant_active = False
                    continue

                if "hello" in value.lower():
                    speak("Hello Naveen")

                elif "who are you" in value.lower():
                    speak("I am Jarvis, Your voice assistant. You can ask me whatever you want I will have a answer for that")

                elif "time" in value.lower():
                    speak("I cannot tell time yet")

                elif "open youtube" in value.lower():
                    webbrowser.open('https://www.youtube.com/')
                
                elif value.lower().startswith("play"):
                    parts = value.split(maxsplit=1)

                    if len(parts) > 1:
                        song_name = parts[1].lower()
                        
                        song_url = music_dict.get(song_name)
                        
                        if song_url:
                            webbrowser.open(song_url)
                        else:
                            speak(f"Sorry. '{song_name}' is not in your music library.")

                else:
                    response = generate_gemini_response(value)
                    speak(response)

        except sr.UnknownValueError:
            print("Didn't catch that")

        except sr.RequestError as e:
            print(f"Speech recognition error: {e}")

except KeyboardInterrupt:
    print("Exiting...")
