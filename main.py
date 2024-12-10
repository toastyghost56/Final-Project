import discord
from discord.ext import commands
import os
import asyncio

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all()) 

bot_statuses = cycle(["Status One", "Hello from Toasty_ghost", "Status Code 123", "Join the Realm"])
@tasks.loop(seconds=30)
async def change_bot_status():
    await bot.change_presence(activity=discord.Game(next(bot_statuses)))

@bot.event
async def on_ready():
    print("Bot ready!")
    change_bot_status.start()

with open("token.txt") as file:
    token = file.read()

async def load():
    for filename in os.listdir("./Cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"Cogs.{filename[:-3]}")

async def FinalProject():
    async with bot:
        await load()
        await bot.start(token)

asyncio.run(FinalProject())
