from discord.ext import commands
import discord

class CommandEvents(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please specify argument/amount ")
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Command not found")


def setup(client):
    client.add_cog(CommandEvents(client))