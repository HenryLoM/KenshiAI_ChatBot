# KenshiAI 🗡️

KenshiAI is a project aimed at developing a functional chatbot for use in various projects and systems. I plan to integrate it into my own operating system. While it is currently in its early stages and may be considered somewhat inexperienced, with patience and your assistance, this project has the potential to evolve into something great.

## Table of Contents 📋

- [Introduction](#introduction)
- [Features](#features)
- [Folder Structure](#folder-structure)
- [How to Use](#how-to-use)
- [Integration](#integration)
- [Contribution Guidelines](#contribution-guidelines)
- [License](#license)

## Introduction 🎩

Welcome to the KenshiAI repository! KenshiAI is designed to be a versatile chatbot suitable for integration into a wide range of systems. Though still in its early development, it has the potential to grow into a powerful assistant with your feedback and contributions.

## Features ✨

- **Modularity** – Easy to plug into various systems thanks to its modular architecture.
- **Customizability** – Fully customizable to match your project's requirements.
- **Compatibility** – Designed with cross-system compatibility in mind.

## Folder Structure 📁
```plaintext
MainDirectory_KenshiAI/
│
├── main.py                             # GUI logic and layout and entry point
├── FunctionalPart.py                   # Chatbot logic and conversation management
├── VoicePart.py                        # Voice functions
├── logPart.py                          # Logging system for debugging
├── messages.py                         # Variables with framed messages
├── requirements.py                     # Dependencies
│
├── Assets/                             # Folder containing AI avatars and assets
│   ├── KenshiAI_icon.png
│   ├── chat_memory.json
│   ├── instructions.txt
│   ├── recollection.txt
```

## How to Use 🛠️

1. Download [Ollama](https://ollama.com/download)
2. Run it in apart console window:
   ```bash
   ollama serve
   ```
3. Pull the LLM (you can do any, if you find it workable):
   ```bash
   ollama pull hf.co/IndexTeam/Index-1.9B-Character-GGUF:latest
   ```
4. Clone the repository or download the project files.
5. Navigate to the project directory:
   ```bash
   cd MainDirectory_KenshiAI
   ```
6. Install all dependencies:
   ```bash
   pip install -r requirements.txt
   ```
7. Run the application:
   ```bash
   python main.py
   ```

## Integrate with Your Project ⚙️
   - Integrate KenshiAI into your project by importing the necessary modules and functions.

   - Refer to the [Contribution Guidelines](CONTRIBUTING.md) for information on extending KenshiAI's functionality.

Feel free to reach out to us if you encounter any issues or have questions during the integration process.

## Contribution Guidelines ❤️‍🩹

We welcome contributions from the community. To contribute to KenshiAI, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Implement your feature and commit your changes: `git commit -m "Description of changes."`.
4. Push to your fork: `git push origin feature-name`.
5. Submit a pull request.

Make sure to follow our [Code of Conduct](CODE_OF_CONDUCT.md) and [Contribution Guidelines](CONTRIBUTING.md).

## License 📜

This project is licensed under the terms of the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.
