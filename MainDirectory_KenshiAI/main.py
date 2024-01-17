import tkinter as tk
import sys
import socket

# check the internet connection
try:
    socket.create_connection(("www.google.com", 80))
except:
    sys.stderr.write("_ _ You have no the internet connection _ _")
    sys.exit(1)

# make the object ChatBot
from FunctionalPart import ChatBot
import VoicePart as Voice
bot = ChatBot()

# variables
isFirstMessage = True
isTalk = False
conversation = {}

# – – – – – – – – – – – – – – – – – – functions – – – – – – – – – – – – – – – – – –
def call_command(command, clear=False):
    text_widget.config(state=tk.NORMAL)  # start chat
    if clear:
        text_widget.delete(1.0, tk.END)  # clear the entire content of the text_widget
    text_widget.tag_configure("center", justify='center')
    text_widget.insert(tk.END, command + "\n\n", "center")  # show chatbot's message
    text_widget.config(state=tk.DISABLED)  # stop chat for saving it of editing
    entry.delete(0, tk.END)  # clear the input place

def greetings():
    global isFirstMessage
    if isFirstMessage:
        isFirstMessage = False
        call_command(bot.start_message)  # call the start message

def turn_voice_button():
    global isTalk
    isTalk = not isTalk
    if isTalk:
        Voice.warning()

def send_message_button(event=None):
    prompt = entry.get()

    # command /new
    if prompt == "/new":
        conversation.clear()
        call_command(bot.start_message, True)  # call the start message

    # command /end
    elif prompt == "/save":
        bot.make_file(conversation)
        call_command(bot.save_message)  # call the save message

    # command /info
    elif prompt == "/info":
        # update the widget of the window
        call_command(bot.info_message)  # call the info message

    # simple message
    else:
        answer = bot.get_chatbots_answer(prompt)
        conversation[prompt] = answer
        # update the widget of the window
        text_widget.config(state=tk.NORMAL)  # start chat
        text_widget.insert(tk.END, f"User: {prompt}" + "\n\n")  # show user's message
        text_widget.insert(tk.END, answer + "\n\n")  # show Kenshi's message
        text_widget.config(state=tk.DISABLED)  # stop chat for saving it of editing
        entry.delete(0, tk.END)  # clear the input place
        # voice settings
        if isTalk:
            Voice.start_talk(answer)

# – – – – – – – – – – – – – – – – – – window – – – – – – – – – – – – – – – – – –

# make the window
root = tk.Tk()
root.title("KenshiAI")
root.geometry("500x350")

# chat
text_widget = tk.Text(root, wrap="word")
text_widget.pack(expand=True, fill="both")
text_widget.config(state=tk.DISABLED)
text_widget.configure(bg="#242424", fg="#ffffff", highlightbackground="#242424")  # change colors

# input place
entry = tk.Entry(root)
entry.pack(side="bottom", fill="x", padx=(0, 50), pady=1)
entry.bind("<Return>", send_message_button)  # "Enter / Return" can be used for sending messages
entry.configure(bg="#242424", fg="#ffffff")  # change colors

# button to send
button_s = tk.Button(root, text=">", width=2, height=1, pady=2, command=send_message_button)
button_s.place(relx=1, rely=1, anchor="se")
if not sys.platform.startswith("darwin"):  # MacOS have a bug that does not let change button's color
    button_s.configure(bg="#242424", fg="#ffffff")  # change colors

# button to talk
button_t = tk.Button(root, text="Voice", width=2, height=1, pady=2, command=turn_voice_button)
button_t.place(relx=1, rely=0.92, anchor="se")
if not sys.platform.startswith("darwin"):  # MacOS have a bug that does not let change button's color
    button_t.configure(bg="#242424")  # change colors

# create the window
greetings()  # the first thing in the chat is greetings
root.mainloop()
