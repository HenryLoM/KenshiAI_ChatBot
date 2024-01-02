class ChatBot:

    def __init__(self):
        self.topics = []
        self.conversations = []

    def gui(self):
        print(f'''
_ _ _ _ _ {self.topics} _ _ _ _ _
          ChatBot Demo          
Management:
/new – end this chat and make a new
/end – stop using ChatBot
/read - comeback to the topic to read a conversation you made before'
_ _ _ _ _ _ _ _ _ _ _ _''')

    def chat_bots_answer(self, prompt):
        return 'ChatBot – *answer of chatbot*'  # here must be chatbot's functionality to answer

    def new_topic(self, name, conv):
        self.topics.append(name)
        self.conversations.append(conv)

    def overall(self):
        print()
        print('_ _ _ _ _ All topics you made _ _ _ _ _')
        for i in range(len(self.topics)):
            print(i + 1, "–", self.topics[i])

    def comeback(self):
        if not self.topics:
            print("You can't use /read because it's your first conversation")
        else:
            print()
            print('_ _ _ _ _ Give the number of a necessary one _ _ _ _ _')
            for i in range(len(self.topics)):
                print(i + 1, "–", self.topics[i])
            while True:
                try:
                    select = int(input()) - 1
                    if 0 <= select < len(self.topics):
                        break  # to stop the cycle if all is good
                    else:
                        print("Invalid number. Please enter a valid number.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            print(f'_ _ _ Chat #{select + 1}: {self.topics[select]}')
            conversation = self.conversations[select]
            for i in range(0, len(conversation), 2):
                print(f"User – {conversation[i]}")
                if i + 1 < len(conversation):
                    print(f"ChatBot – {conversation[i + 1]}")
            print('_ _ _')
            print("_ _ _ _ _ It's read mode only, you still in the last topic and can continue _ _ _ _ _")
