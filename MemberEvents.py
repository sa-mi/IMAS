from discord.ext import commands
import discord

class MemberEvents(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined, welcome!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left, bye!')


def setup(client):
    client.add_cog(MemberEvents(client))