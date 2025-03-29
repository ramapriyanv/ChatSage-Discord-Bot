import discord
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Discord intents setup
intents = discord.Intents.default()
intents.message_content = True  
client = discord.Client(intents=intents)

# Hugging Face API settings for DeepSeek-V3-0324 model
HF_API_TOKEN = os.getenv("HF_API_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/deepseek-ai/DeepSeek-V3-0324"
headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}

# Generation configuration
generation_config = {
    "max_length": 100,
    "temperature": 0.7,
    "top_p": 0.9,
    "top_k": 50,
}

def query_hf(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def generate(text):
    data = {
        "inputs": text,
        "parameters": generation_config,
    }
    result = query_hf(data)
    print("Inference API Response:", result)
    if isinstance(result, dict) and result.get("error"):
        return "Error: " + result["error"]
    return result[0]["generated_text"]

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    user_message = message.content
    bot_reply = generate(user_message)
    await message.channel.send(f"{message.author.mention} {bot_reply}")

client.run(os.getenv("DISCORD_TOKEN"))
