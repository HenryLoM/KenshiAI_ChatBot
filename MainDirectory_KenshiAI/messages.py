start_message = """
╔═════════════════════════════════════════════════╗
║                  KenshiAI Demo                  ║
║ Main commands:                                  ║
║ /new  – end the current chat and make a new one ║
║ /save – save the current chat as a file         ║
║ /info - give the information about this AI      ║
║ /help - give the list of all commands           ║
╚═════════════════════════════════════════════════╝
"""
save_message = """
╔════════════════════════════════════════════════════════╗
║ File with all conversation was created on your desktop ║
╚════════════════════════════════════════════════════════╝
"""
info_message = """
╔══════════════════════════════════════════════════════════════════════╗
║ Project was made by Muhammad Gadisov                                 ║
║ Project's Github: https://github.com/HenryLoM/KenshiAI_ChatBot       ║
║ About AI: Kenshi was made using ollama and LLM by IndexTeam          ║
║ Used LLM: https://huggingface.co/IndexTeam/Index-1.9B-Character-GGUF ║
╚══════════════════════════════════════════════════════════════════════╝
"""
help_message = """
╔═════════════════════════════════════════════════╗
║ /new  – end the current chat and make a new one ║
║ /save – save the current chat as a file         ║
║ /del  – deletes the last AI response            ║
║ /ref  – refreshes the last AI response          ║
║ /info - give the information about this AI      ║
║ /help - give the list of all commands           ║
╚═════════════════════════════════════════════════╝
"""
wrong_message = """
╔══════════════════════════════════════════════════╗
║ ! Wrong command: type /help for available ones ! ║
╚══════════════════════════════════════════════════╝
"""
no_ai_response = """
╔═════════════════════════════════╗
║ ! No AI response to work with ! ║
╚═════════════════════════════════╝
"""
error_refreshing_response = """
╔═══════════════════════════════╗
║ ! Error refreshing response ! ║
╚═══════════════════════════════╝
"""