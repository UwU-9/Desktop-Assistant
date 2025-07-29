import speech_recognition as sr


r = sr.Recognizer()
r.pause_threshold = 2
def listen():
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time up")

        try:
            print("Text: " +  r.recognize_google(audio_text))
        except Exception as e:
            print("Sorry, I didn't understand.")
            print("Error:", e)

listen()
