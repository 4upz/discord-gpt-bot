import discord
from dotenv import load_dotenv
from discord.ext import commands
from os import getenv
from gpt import GPT

# Load the .env file
load_dotenv() 

# OpenAPI config
gpt = GPT(getenv('OPENAI_KEY'))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}!')

@bot.event
async def on_message(message):
    if message.author != bot.user:
        keyword = gpt.containsKeyword(message.content)
        if bot.user in message.mentions:
            async with message.channel.typing():
                response = await gpt.reply(message.content)
                await message.reply(response)
        elif keyword is not None:
            async with message.channel.typing():
                context = f"\nThe user is not talking to you, but you are chiming in on the mention of {keyword}."
                response = await gpt.reply(message.content, context)
                await message.reply(response)
    await bot.process_commands(message)
    
bot.run(getenv('DISCORD_APP_TOKEN'))