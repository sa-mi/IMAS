from discord.ext import commands
import discord

class AnnounceCommand(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def announce(self, ctx, title, *, message):
        channel = self.client.get_channel(711167513320357938)
        embed = discord.Embed(title=title, colour=0x851ae6, inLine=True)
        embed.add_field(name="\u200b", value=message)
        await channel.send(content="@everyone", embed=embed)

def setup(client):
    client.add_cog(AnnounceCommand(client))