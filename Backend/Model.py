import  Automation
import Chatbot
import SpeechToText as st

user_input = st.listen()

if "open" in user_input.lower():

    Automation.handle_open_command(user_input)
else:
    Chatbot.respond(user_input)
