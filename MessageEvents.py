from discord.ext import commands
import discord

class MessageEvents(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        content = message.content
        if content.startswith('.links'):
            embed = discord.Embed(title="Snapchat", description="samisam37", color=0x851ae6)
            embed.add_field(name="Youtube", value="https://www.youtube.com/channel/UC2AA0rKwz6dI40dFdvUaVzA",
                            inline=False)
            embed.add_field(name="Site", value="https://sa-mi.github.io/Sami/", inline=False)
            await message.channel.send(embed=embed)
        #else:
            #await self.client.process_commands(message)


def setup(client):
    client.add_cog(MessageEvents(client))
