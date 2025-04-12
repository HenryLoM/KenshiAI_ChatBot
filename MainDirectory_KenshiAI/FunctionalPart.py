# ========== ========== ========== ========== imports


# Libraries
import json
import logging
import aiofiles
from ollama import AsyncClient
# Modules
import logPart
import messages


# ========== ========== ========== ========== primary stuff


MEMORY_FILE = "Assets/chat_memory.json"  # File to store chat history
MAX_MESSAGES = 100                       # Maximum messages before trimming
TRIM_AMOUNT = 10                         # Number of messages to remove when trimming
logging.getLogger("httpcore").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)


# ========== ========== ========== ========== class and functions


class ChatBot:
    def __init__(self, model: str, instructions_file: str, recollection_file: str):
        self.model = model
        self.instructions_path = instructions_file
        self.recollection_file_path = recollection_file
        self.instructions = ""
        self.recollection = ""
        self.chat_history = []
        self.ollama = AsyncClient()

# ========== memory working

    async def save_memory(self) -> None:
        """Saves chat history to a file in JSON format asynchronously."""
        async with aiofiles.open(file=MEMORY_FILE, mode='w', encoding='utf-8') as file:
            await file.write(json.dumps(self.chat_history, ensure_ascii=False, indent=2))

    async def load_memory(self, prepared_file: json = MEMORY_FILE) -> None:
        """Loads chat history from a file if available, otherwise returns an empty list."""
        try:
            async with aiofiles.open(file=prepared_file, mode='r', encoding='utf-8') as file:
                content = await file.read()
                self.chat_history = json.loads(content)
                await self.save_memory()
        except (FileNotFoundError, json.JSONDecodeError):
            self.chat_history = []

    async def delete_memory(self) -> None:
        """Simply makes the chat_history constant empty."""
        self.chat_history = []
        await self.save_memory()

    async def trim_memory(self) -> None:
        """Trims older messages when exceeding the limit while keeping the most recent ones."""
        if len(self.chat_history) > MAX_MESSAGES:
            self.chat_history = self.chat_history[-MAX_MESSAGES:]

# ========== chat working

    async def chat(self, prompt: str, system_log: str = "") -> str:
        """Sends a prompt to the model while preserving chat history."""
        try:
            to_send = self.chat_history + [
                {"role": "system", "content": "Follow the instructions to respond correctly:\n\n" + self.instructions},
                {"role": "system", "content": "Your recollection:\n\n" + self.recollection},
                {"role": "system", "content": "System log/context:\n\n" + system_log},
                {"role": "user", "content": prompt}
            ]
            response = await self.ollama.chat(model=self.model, messages=to_send)
            message = response.get(key='message', default={}).get('content', 'No response')

            self.chat_history.append({"role": "user", "content": prompt})
            self.chat_history.append({"role": "assistant", "content": message})
            await self.trim_memory()
            await self.save_memory()

            return message
        except Exception as e:
            logPart.show_up_log(message=f"{str(e)}", level=3)  # Logging

    async def initialize(self) -> None:
        """Initializes chatbot by loading instructions and chat history."""
        self.instructions = await self.load_file(self.instructions_path)
        self.recollection = await self.load_file(self.recollection_file_path)
        await self.load_memory()

# ========== misc working

    async def load_file(self, filename: str) -> str:
        """Loads content from a given file asynchronously."""
        try:
            async with aiofiles.open(filename, mode='r', encoding='utf-8') as file:
                return await file.read()
        except FileNotFoundError:
            return ""

    async def change_recollection(self, definition: str) -> None:
        """Overwrites the recollection.txt file with the new memo details."""
        try:
            async with aiofiles.open(self.recollection_file_path, mode="w", encoding="utf-8") as file:
                await file.write(definition)
            logPart.show_up_log(message=f"Recollection updated", level=1)  # Logging
        except Exception as e:
            logPart.show_up_log(message=f"{str(e)}", level=3)  # Logging

    async def refresh_delete_last_response(self, refresh: bool) -> str:
        """Deletes the last AI response and/or regenerates a new one."""
        try:
            # Ensure there are at least two messages (last AI response and corresponding user input)
            if len(self.chat_history) < 2 or self.chat_history[-1]["role"] != "assistant":
                logPart.show_up_log(message="No AI response to work with.", level=2)
                return messages.no_ai_response

            # Remove last AI response
            last_user_input = self.chat_history[-2]["content"]
            self.chat_history = self.chat_history[:-2]  # Remove last user input and AI response
            await self.save_memory()

            # if refresh is True - generate new response using the same user input
            if refresh:
                logPart.show_up_log(message="Last message refreshed", level=1)  # Logging
                return await self.chat(last_user_input)
            else:
                logPart.show_up_log(message="Last messages deleted", level=1)  # Logging
                return ""

        except Exception as e:
            logPart.show_up_log(message=f"{str(e)}", level=3)
            return messages.error_refreshing_response
