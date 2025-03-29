# ChatSage: AI-Powered Discord Companion

This Discord Bot leverages the power of Hugging Face’s DeepSeek-V3-0324 model to interact with users in Discord servers. It listens to messages and responds with AI-generated content based on the input it receives.

## Features

- Responds to user messages with AI-generated content using DeepSeek-V3-0324.

- Customizable AI response settings for creativity and response quality.

- Easy to deploy and run on any server.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have a Discord account and have created a Discord bot.

- You have a Hugging Face account with an API token.

- You have Python 3.6+ installed on your machine.

## Installation

To install the necessary dependencies for this bot, follow these steps:

1. Clone the repository to your local machine:


```bash
git clone https://github.com/ramapriyanv/ChatSage-Discord-Bot
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Configuration

1. Set up your Hugging Face account and obtain your API token from Hugging Face Account Settings.

2. Create a .env file in the root directory of your project and add your Discord bot token and Hugging Face API token:

```plaintext
DISCORD_TOKEN=your_discord_bot_token
HF_API_TOKEN=your_huggingface_api_token
```

3. Update the `main.py` file with your specific model details if different from the defaults.

## Usage

To start the bot, run the following command in your terminal:

```bash
python main.py
```

The bot will log in to Discord and start listening for messages. When a message is received, it will generate a response using DeepSeek-V3-0324 and reply in the same channel.


## License

Distribute under the MIT License. See `LICENSE` for more information.
