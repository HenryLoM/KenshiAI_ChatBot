# ========== ========== ========== ========== imports


# Libraries
import sys
import socket
import asyncio
from datetime import datetime
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


def display_message(message: str) -> None:
    """Lets user display commands' messages."""
    text_widget.config(state=tk.NORMAL)                            # Start the chat
    text_widget.tag_configure(tagName="center", justify='center')  # Center the displaying text
    text_widget.insert(tk.END, message + "\n\n", "center")   # Show the system message
    text_widget.see(tk.END)                                        # Scroll to the bottom
    text_widget.config(state=tk.DISABLED)                          # Stop the chat for saving it from editing
    entry.delete(first=0, last=tk.END)                             # Clear the input field


def call_command(command: str) -> None:
    """Lets user call commands."""
    text_widget.config(state=tk.NORMAL)  # Start the chat
    if command == "/new":
        loop.run_until_complete(bot.delete_memory())          # Delete the memory of AI
        text_widget.delete(index1=1.0, index2=tk.END)         # Clear the entire content of the text_widget
    elif command == "/save":
        loop.run_until_complete(bot.save_memory())            # Save the memory of AI
    elif command == "/del":
        loop.run_until_complete(bot.delete_last_response())   # Delete the last response
        text_widget.delete(index1="end-6l", index2="end-1l")  # Delete last messages of user and AI
    elif command == "/ref":
        text_widget.delete(index1="end-3l", index2="end-1l")  # Delete the last message of AI from the screen
        answer = loop.run_until_complete(bot.delete_last_response(refresh=True))  # and from the memory, refreshing it
        text_widget.see(tk.END)                               # Scroll to the bottom
        if not answer:
            answer = messages.no_ai_response
        text_widget.insert(index=tk.END, chars=f"Kenshi: {answer}" + "\n\n")  # Display AI response
        text_widget.see(tk.END)                                               # Scroll to the bottom
    else:
        logPart.show_up_log(message=f"Wrong command tried to get processed", level=3)  # Logging
    text_widget.config(state=tk.DISABLED)


def greetings():
    """Displays the first message if it is first indeed."""
    global isFirstMessage
    if isFirstMessage:
        isFirstMessage = False
        display_message(message=messages.start_message)  # Call the start message
        loop.create_task(bot.initialize())               # Prepare the chatbot


def open_recollection_popup():
    """Opens a popup to edit and save text to recollection.txt."""
    popup = tk.Toplevel(root)
    popup.title("Edit AI's recollection")
    popup.geometry("300x200")
    popup.configure(bg="#242424")

    # Editing field
    text_field = tk.Text(popup, wrap="word", height=10, bg="#242424", fg="#ffffff", insertbackground="#ffffff")
    text_field.pack(expand=True, fill="both", padx=10, pady=5)

    # Load existing content
    try:
        with open("Assets/recollection.txt", "r", encoding="utf-8") as file:
            content = file.read()
            text_field.insert(index="1.0", chars=content)
    except FileNotFoundError:
        text_field.insert(index="1.0", chars="")

    # Save edited content
    def save_text():
        user_text = text_field.get(index1="1.0", index2=tk.END).strip()
        with open("Assets/recollection.txt", "w", encoding="utf-8") as r_file:
            r_file.write(user_text + "\n")
        popup.destroy()

    # Save button
    save_button = tk.Button(popup, text="Save", width=4, height=1, pady=2, command=save_text)
    if not sys.platform.startswith("darwin"):              # macOS button fix
        save_button.configure(bg="#242424", fg="#ffffff")
    save_button.pack(pady=2)


def turn_voice_button():
    """Turns on/off the voice."""
    global isTalk
    isTalk = not isTalk  # True becomes False, or False becomes True
    if isTalk:
        Voice.warning()


def send_message_button(event=None):
    """Sends the prompt to AI and returns the response, or activates a command."""
    prompt = entry.get()

    # Command
    if prompt.startswith("/"):
        if prompt == "/new":
            call_command(command="/new")
            display_message(message=messages.start_message)  # Display the start message back
        elif prompt == "/save":
            display_message(message=messages.save_message)   # Display the save message
        elif prompt == "/del":
            call_command(command="/del")
        elif prompt == "/ref":
            call_command(command="/ref")
        elif prompt == "/info":
            display_message(message=messages.info_message)   # Display the info message
        elif prompt == "/help":
            display_message(message=messages.help_message)   # Display the help message
        else:
            display_message(message=messages.wrong_message)  # Display the wrong message

    # Regular message
    else:
        # Make the log message for AI
        current_time = datetime.now().strftime("%I:%M %p")  # HH:MM AM/PM
        system_log = f"(Log: Current time is {current_time})"

        # Make the answer
        answer = loop.run_until_complete(bot.chat(prompt=prompt, system_log=system_log))
        if not answer:
            answer = messages.no_ai_response

        # Update the widget of the window
        text_widget.config(state=tk.NORMAL)                                   # Start the chat
        text_widget.insert(index=tk.END, chars=f"User: {prompt}" + "\n\n")    # Display user message
        text_widget.insert(index=tk.END, chars=f"Kenshi: {answer}" + "\n\n")  # Display AI response
        text_widget.see(tk.END)                                               # Scroll to the bottom
        text_widget.config(state=tk.DISABLED)                                 # Stop chat to save it from editing
        entry.delete(first=0, last=tk.END)                                    # Clear the input field
        # Voice settings
        if isTalk:
            Voice.start_talk(answer)


# ========== ========== ========== ========== window working


# Window
root = tk.Tk()
root.title("KenshiAI")
root.geometry("520x350")

# Chat
text_widget = tk.Text(master=root, wrap="word")
text_widget.pack(expand=True, fill="both")
text_widget.config(state=tk.DISABLED)
text_widget.configure(bg="#242424", fg="#ffffff", highlightbackground="#242424")  # Change colors

# Input field
entry = tk.Entry(master=root)
entry.pack(side="bottom", fill="x", padx=(0, 50), pady=1)
entry.bind("<Return>", send_message_button)                              # "Enter / Return" calls sending of messages
entry.configure(bg="#242424", fg="#ffffff", insertbackground="#ffffff")  # Change colors

# Button to send
button_s = tk.Button(master=root, text=">", width=2, height=1, pady=2, command=send_message_button)
button_s.place(relx=1, rely=1, anchor="se")
if not sys.platform.startswith("darwin"):           # MacOS have a bug that does not let change button's color
    button_s.configure(bg="#242424", fg="#ffffff")  # Change colors on macOS

# Button to talk
button_t = tk.Button(master=root, text="Voice", width=2, height=1, pady=2, command=turn_voice_button)
button_t.place(relx=1, rely=1, y=-30, anchor="se")
if not sys.platform.startswith("darwin"):  # MacOS have a bug that does not let change button's color
    button_t.configure(bg="#242424")       # Change colors on macOS

# Button to change the recollection of AI
button_m = tk.Button(master=root, text="Memory", width=2, height=1, pady=2, command=open_recollection_popup)
button_m.place(relx=1, rely=1, y=-60, anchor="se")
if not sys.platform.startswith("darwin"):  # MacOS have a bug that does not let change button's color
    button_t.configure(bg="#242424")       # Change colors on macOS

# Create the window
greetings()  # The first thing in the chat always is greetings
root.mainloop()
