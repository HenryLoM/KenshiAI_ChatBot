from PyCharacterAI import Client
import asyncio
import os

# variables from chatbot's library
profile = "05036a2132aca13a0ce4a2ec486b56a9e9ec0a52"  # profile for work
character = "5KaYRcdwaEOOwBUre6c9IolYgoggr3xRHrx5Bt5yUR0"  # character for work
client = Client()

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

    async def async_get_chatbots_answer(self, prompt):
        message = prompt  # get a message
        await client.authenticate_with_token(profile)  # connect to the profile
        chat = await client.create_or_continue_chat(character)  # enter a chat
        text = await chat.send_message(message)  # get an answer
        return f"Kenshi: {text.text}"  # return an answer

    def get_chatbots_answer(self, prompt):
        return asyncio.run(self.async_get_chatbots_answer(prompt))

    def make_file(self, conversation):
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")  # make a variable of the desktop
        file_path = os.path.join(desktop_path, "chatbot_data.txt")  # make a way to the desktop
        with open(file_path, "w") as file:  # make the file
            for key, value in conversation.items():  # convert a conversation
                file.write(f"User: {key}\n{value}\n")  # fill the file

    async def async_new_chat(self):
        await client.authenticate_with_token(profile)  # connect to the profile
        await client.create_chat(character)  # make a chat

    def new_chat(self):
        return asyncio.run(self.async_new_chat())
