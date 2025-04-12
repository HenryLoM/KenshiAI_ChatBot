# ========== ========== ========== ========== imports


# Libraries
import sys
import socket
import asyncio
import tkinter as tk
# Modules
from FunctionalPart import ChatBot
import VoicePart as Voice
import messages
import logPart


# ========== ========== ========== ========== primary stuff


bot = ChatBot(model="hf.co/IndexTeam/Index-1.9B-Character-GGUF",
              instructions_file="Assets/instructions.txt",
              recollection_file="Assets/recollection.txt")
loop = asyncio.get_event_loop()
isFirstMessage = True
isTalk = False


# ========== ========== ========== ========== functions


def check_connection(quiting: bool) -> int:
    """Checks the internet connection."""
    try:
        socket.create_connection(
            address=("www.google.com", 80))  # There can be a website we need to reach constantly
        return 1
    except (socket.gaierror, Exception):
        if quiting:
            logPart.show_up_log(message=f"No internet connection / The website unavailable", level=3)  # Logging
            sys.exit(1)
        return 0


def call_command(command: str, clear: bool = False) -> None:
    """Lets user call commands."""
    text_widget.config(state=tk.NORMAL)                           # Start the chat
    if clear:
        text_widget.delete(index1=1.0, index2=tk.END)             # Clear the entire content of the text_widget
    text_widget.tag_configure(tagName="center", justify='center')
    text_widget.insert(tk.END, command + "\n\n", "center")  # Show the AI message
    text_widget.config(state=tk.DISABLED)                         # Stop the chat for saving it from editing
    entry.delete(first=0, last=tk.END)                            # Clear the input field


def greetings():
    """Displays the first message if it is first indeed."""
    global isFirstMessage
    if isFirstMessage:
        isFirstMessage = False
        call_command(command=messages.start_message)  # Call the start message
        loop.create_task(bot.initialize())            # Prepare the chatbot


def turn_voice_button():
    """Turns on/off the voice."""
    global isTalk
    isTalk = not isTalk  # True becomes False, or False becomes True
    if isTalk:
        Voice.warning()


def send_message_button(event=None):
    """Sends the prompt to AI and returns the response, or activates a command."""
    prompt = entry.get()

    # Command /new
    if prompt == "/new":
        loop.run_until_complete(bot.delete_memory())              # Delete the memory of AI
        call_command(command=messages.start_message, clear=True)  # Display the start message

    # Command /end
    elif prompt == "/save":
        loop.run_until_complete(bot.save_memory())  # Save the memory of AI
        call_command(messages.save_message)         # Display the save message

    # Command /info
    elif prompt == "/info":
        call_command(messages.info_message)  # Display the info message

    # Regular message
    else:
        answer = loop.run_until_complete(bot.chat(prompt))
        # Update the widget of the window
        text_widget.config(state=tk.NORMAL)                     # Start the chat
        text_widget.insert(tk.END, f"User: {prompt}" + "\n\n")  # Display user message
        text_widget.insert(tk.END, answer + "\n\n")             # Display AI response
        text_widget.config(state=tk.DISABLED)                   # Stop chat to save it from editing
        entry.delete(first=0, last=tk.END)                      # Clear the input field
        # Voice settings
        if isTalk:
            Voice.start_talk(answer)

# ========== ========== ========== ========== window working


# Window
root = tk.Tk()
root.title("KenshiAI")
root.geometry("550x400")

# Chat
text_widget = tk.Text(root, wrap="word")
text_widget.pack(expand=True, fill="both")
text_widget.config(state=tk.DISABLED)
text_widget.configure(bg="#242424", fg="#ffffff", highlightbackground="#242424")  # change colors

# Input field
entry = tk.Entry(root)
entry.pack(side="bottom", fill="x", padx=(0, 50), pady=1)
entry.bind("<Return>", send_message_button)  # "Enter / Return" can be used for sending messages
entry.configure(bg="#242424", fg="#ffffff", insertbackground="#ffffff")  # change colors

# Button to send
button_s = tk.Button(root, text=">", width=2, height=1, pady=2, command=send_message_button)
button_s.place(relx=1, rely=1, anchor="se")
if not sys.platform.startswith("darwin"):  # MacOS have a bug that does not let change button's color
    button_s.configure(bg="#242424", fg="#ffffff")  # change colors

# Button to talk
button_t = tk.Button(root, text="Voice", width=2, height=1, pady=2, command=turn_voice_button)
button_t.place(relx=1, rely=0.92, anchor="se")
if not sys.platform.startswith("darwin"):  # MacOS have a bug that does not let change button's color
    button_t.configure(bg="#242424")       # Change colors on macOS

# Create the window
greetings()  # The first thing in the chat always is greetings
root.mainloop()
