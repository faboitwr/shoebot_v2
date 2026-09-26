from discord.ext import commands
import discord

from app_run import app, init

bot_token = "" #to be filled by user
channel_ = 0 #to be filled by user

bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

init()

shoestate = app("shoebase.db")

@bot.event
async def on_ready():
    #print("Test.")
    channel = bot.get_channel(channel_)
    await channel.send(shoestate)
    await bot.close()

bot.run(bot_token)
