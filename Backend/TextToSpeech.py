from gtts import gTTS
import pygame
import time



def text_to_speech(text, lang="en", slow=False):


        tts = gTTS(text=text, lang=lang, slow=slow)
        tts.save("Speak.mp3")

        # Initialize pygame mixer and play audio
        pygame.mixer.init()
        pygame.mixer.music.load("Speak.mp3")
        pygame.mixer.music.play()

        # Wait for playback to finish
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)









