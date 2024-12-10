import discord
from discord.ext import commands, tasks
import os
import asyncio
from itertools import cycle
import logging 

logging.basicConfig(level=logging.INFO)

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

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello there, {ctx.author.mention}!")

@bot.command(aliases = ["gm", "morning"])
async def goodmorning(ctx):
    await ctx.send(f"Good morning, {ctx.author.mention}!")

@bot.command()
async def sendembed(ctx):
    embeded_msg = discord.Embed(title="The Realm of Toast", description="The place for all toast worldwide!", color=discord.Color.blurple())
    embeded_msg.set_author(name="Footer text", icon_url=ctx.author.avatar)
    embeded_msg.set_thumbnail(url=ctx.author.avatar)
    embeded_msg.add_field(name="A field of bread", value="Toasted Bread", inline=False)
    embeded_msg.set_image(url=ctx.guild.icon)
    embeded_msg.set_footer(text="Footer text", icon_url=ctx.author.avatar)
    await ctx.send(embed=embeded_msg)

@bot.command()
async def ping(ctx):
    ping_embed = discord.Embed(title="Ping", description="Latency in ms", color=discord.Color.dark_green())
    ping_embed.add_field(name=f"{bot.user.name}'s Latency (ms):", value=f"{round(bot.latency*1000)}ms", inline=False)
    ping_embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
    await ctx.send(embed=ping_embed)




bot.run(token)

