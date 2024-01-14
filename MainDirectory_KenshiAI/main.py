from FunctionalPart import ChatBot
import tkinter as tk
import platform

# make the object ChatBot
bot = ChatBot()

# variables
first_message = True
conversation = {}

# functions
def greetings():
    global first_message
    if first_message:
        first_message = False
        text_widget.config(state=tk.NORMAL)  # start chat
        text_widget.tag_configure("center", justify='center')
        text_widget.insert(tk.END, bot.start_message + "\n\n", "center")  # show chatbot's message
        text_widget.config(state=tk.DISABLED)  # stop chat for saving it of editing

def on_button_click(event=None):
    global conversation
    prompt = entry.get()

    # Command /new
    if prompt == "/new":
        conversation.clear()
        # update the widget of the window
        text_widget.config(state=tk.NORMAL)  # start chat
        text_widget.delete(1.0, tk.END)  # Clear the entire content of the text_widget
        text_widget.insert(tk.END, bot.start_message + "\n\n")  # show chatbot's message
        text_widget.config(state=tk.DISABLED)  # stop chat for saving it of editing
        entry.delete(0, tk.END)  # clear the input place

    # Command /end
    elif prompt == "/save":
        bot.make_file(conversation)
        # update the widget of the window
        text_widget.config(state=tk.NORMAL)  # start chat
        text_widget.insert(tk.END, bot.save_message + "\n\n")  # show chatbot's message
        text_widget.config(state=tk.DISABLED)  # stop chat for saving it of editing
        entry.delete(0, tk.END)  # clear the input place

    # Simple message
    else:
        answer = bot.get_chatbots_answer(prompt)
        conversation[prompt] = answer
        # update the widget of the window
        text_widget.config(state=tk.NORMAL)  # start chat
        text_widget.insert(tk.END, f"User: {prompt}" + "\n\n")  # show user's message
        text_widget.insert(tk.END, answer + "\n\n")  # show chatbot's message
        text_widget.config(state=tk.DISABLED)  # stop chat for saving it of editing
        entry.delete(0, tk.END)  # clear the input place

# make the window
root = tk.Tk()
root.title("KenshiAI")
root.geometry("500x350")

# chat
text_widget = tk.Text(root, wrap="word")
text_widget.pack(expand=True, fill="both")
text_widget.config(state=tk.DISABLED)
text_widget.configure(bg="#242424", fg="#ffffff", highlightbackground="#242424")  # change colors
greetings()

# input place
entry = tk.Entry(root)
entry.pack(side="bottom", fill="x", padx=(0, 50), pady=1)
entry.bind("<Return>", on_button_click)  # "Enter / Return" can be used for sending messages
entry.configure(bg="#242424", fg="#ffffff")  # change colors

# button
button = tk.Button(root, text=">", width=2, height=1, pady=2, command=on_button_click)
button.place(relx=1, rely=1, anchor="se")
if platform.system() != "Darwin":  # MacOS have a bug that does not let change button's color
    button.configure(bg="#242424", fg="#ffffff")  # change colors

# create the window
root.mainloop()
