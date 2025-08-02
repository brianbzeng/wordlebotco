import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True 
client = discord.Client(intents=intents)

wordle_pattern = re.compile(r"Wordle\s+\d{1,4}\s+[1-6X]/6")

TARGET_CHANNEL_NAME = "wordlebotco"

@client.event
async def on_ready():
    print(f'✅ Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.name != TARGET_CHANNEL_NAME:
        return

    if wordle_pattern.search(message.content):
        print(f"Wordle result from {message.author.display_name}:")
        print(message.content)

client.run("MTM5NjY4NDI0MzA2ODkxNTgzMg.GXmOdv.XWQWs873XP9d9FCYNnlCvhyhdYGMAiIkcjU8ik")
