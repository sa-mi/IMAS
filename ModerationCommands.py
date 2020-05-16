from discord.ext import commands
import discord

class ModerationCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await ctx.send(f'Kicked {member} for {reason}')
        await member.kick(reason=reason)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await ctx.send(f'Banned {member} for {reason}')
        await member.ban(reason=reason)


def setup(client):
    client.add_cog(ModerationCommands(client))