from characterai import PyCAI

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
        self.save_message = "File with all conversation was created on your desktop"
        self.start_message = f'''
╔════════════════════════════════════════════════╗
║                  KenshiAI Demo                 ║
║Commands:                                       ║
║/new – end the current chat and make a new one  ║
║/save – save the current chat as a file         ║
╚════════════════════════════════════════════════╝
'''

    def get_chatbots_answer(self, prompt):
        message = prompt  # get a message
        data = client.chat.send_message(chat["external_id"], tgt, message)  # mix all our stuff
        text = data["replies"][0]["text"]  # get ready the text
        return f"Kenshi: {text}"  # return an answer

    def make_file(self, conversation):
        with open("chatbot's_data", "w") as file:  # make the file
            for key, value in conversation.items():  # convert a conversation
                file.write(f"User: {key}\n{value}\n")  # fill the file
