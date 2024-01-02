from FunctionalPart import ChatBot

# make the object ChatBot
bot = ChatBot()

# variables
total_messages = 0
conversation = []
first_prompt = None

# working part
while True:
    # Make GUI before any message
    if total_messages == 0:
        bot.gui()

    # Get user's prompt
    prompt = input('User – ')
    total_messages += 1
    conversation.append(prompt)

    # Save the first message as a name of the topic
    if total_messages == 1:
        first_prompt = prompt

    # Processing commands

    # Command /new
    if prompt.lower() == '/new':
        total_messages = 0
        bot.new_topic(first_prompt, conversation)
        conversation = []
    # Command /read
    elif prompt.lower() == '/read':
        bot.comeback()
    # Command /end
    elif prompt.lower() == '/end':
        bot.new_topic(first_prompt, conversation)
        bot.overall()
        break
    # Simple message
    else:
        answer = bot.chat_bots_answer(prompt)
        print(answer)
        conversation.append(answer)
