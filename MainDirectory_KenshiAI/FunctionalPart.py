from characterai import PyCAI
import os

# variables from chatbot's library
client = PyCAI("e8fef74a7ca89d9ae65d2606591fb94b0c323b9c")  # profile for work
char = "IlJEFcRpD74cqg8mNMpM5iTXFF5EtUI66yWbT9we2Wo"  # character for work
chat = client.chat.get_chat(char)  # import a chat into the variable
participants = chat["participants"]
if not participants[0]["is_human"]:
    tgt = participants[0]["user"]["username"]
else:
    tgt = participants[1]["user"]["username"]

# class of our ChatBot
class ChatBot:

    def __init__(self):
        self.start_message = '''
╔═════════════════════════════════════════════════╗
║                  KenshiAI Demo                  ║
║Commands:                                        ║
║/new – end the current chat and make a new one   ║
║/save – save the current chat as a file          ║
║/info - give the information about this AI       ║
╚═════════════════════════════════════════════════╝
'''
        self.save_message = '''
╔══════════════════════════════════════════════════════╗
║File with all conversation was created on your desktop║
╚══════════════════════════════════════════════════════╝
'''
        self.info_message = '''
╔═══════════════════════════════════════════════════════════════╗
║Project was maden by Muhammad Gadisov                          ║
║Project's Github: https://github.com/HenryLoM/KenshiAI_ChatBot ║
║About AI: Kenshi was maden using unofficial "character ai" api.║
╚═══════════════════════════════════════════════════════════════╝
'''

    def get_chatbots_answer(self, prompt):
        message = prompt  # get a message
        data = client.chat.send_message(chat["external_id"], tgt, message)  # mix all our stuff
        text = data["replies"][0]["text"]  # get ready the text
        return f"Kenshi: {text}"  # return an answer

    def make_file(self, conversation):
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")  # make a variable of the desktop
        file_path = os.path.join(desktop_path, "chatbot_data.txt")  # make a way to the desktop
        with open(file_path, "w") as file:  # make the file
            for key, value in conversation.items():  # convert a conversation
                file.write(f"User: {key}\n{value}\n")  # fill the file
