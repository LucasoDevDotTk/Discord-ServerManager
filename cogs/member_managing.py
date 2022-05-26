"""
MIT License

Copyright (c) 2021 lucaso60
Copyright (c) 2021 LEL Studios
Copyright (c) 2015-2021 Rapptz
Copyright (c) 2021-present Pycord Development

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import discord
from discord.ext import commands
from discord.commands import slash_command, Option


class member_managing(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @slash_command(name="kick")
    async def kick(self, ctx: commands.Context, member: Option(discord.Member), *, reason: str = None):
        if reason is None:
            reason = "No reason given."
        await member.kick(reason=reason)
        await ctx.send(f"Kicked {member} for {reason}")

    @slash_command(name="ban")
    async def ban(self, ctx: commands.Context, member: Option(discord.Member), *, reason: str = None):
        if reason is None:
            reason = "No reason given."
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member} for {reason}")

    @slash_command(name="unban")
    async def unban(self, ctx: commands.Context, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(
                    title="ServerManager - LOG", description=f"{ctx.author} unbanned {member}", color=discord.Color.green())
                await ctx.send(embed=embed)
                return

        embed = discord.Embed(title="ServerManager - ERROR",
                              description=f"{member} was not found!", color=discord.Color.red())
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(member_managing(bot))
