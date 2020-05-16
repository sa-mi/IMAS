import discord
import random
import youtube_dl
from itertools import cycle
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions
import os

players = {}
client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("https://sa-mi.github.io/Sami/"))
    print("bot is online")


for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        client.load_extension('cogs.{}'.format(filename[:-3]))
        print("Loaded Cog: {}".format(filename[:-3]))


client.run('NzEwNzYxMDk0Njg3MzU5MDA3.Xr9zRQ.z8e5-4oTT6RJBCoWzzkRxwP_6RM')