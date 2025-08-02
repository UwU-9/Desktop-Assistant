import webbrowser
import SpeechToText as st
import TextToSpeech as TTS


def handle_open_command(command):
    # Map spoken commands to URLs
    sites = {
        "youtube": "https://www.youtube.com/",
        "google": "https://www.google.com/",
        "github": "https://www.github.com/"
    }

    # Get the user's spoken command


    # Proceed only if something was recognized
    if command is not None:
        command = command.lower()  # Normalize for matching

        if "open" in command:
            for site_name, url in sites.items():
                if f"open {site_name}" in command:
                    print(f"Opening {site_name}...")
                    TTS.text_to_speech(f"Opening {site_name}")
                    webbrowser.open(url)
                    break
            else:
                print("No recognized site found in the command.")
                TTS.text_to_speech("Site not found")
        else:
            print("The command does not contain 'open'.")
            TTS.text_to_speech("Please say a command starting with open")
    else:
        print("Sorry, I didn't catch that.")
        TTS.text_to_speech("Sorry, I didn't catch that")



