import discord
from discord.ext import commands

from config import settings

intents = discord.Intents.default()
intents.presences = True
intents.members = True 
intents.message_content = True

bot = commands.Bot(command_prefix=config['prefix'], intents = intents)

@bot.event
async def on_ready():
    print('Bot connected successfully!')