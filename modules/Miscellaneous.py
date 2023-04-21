import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import json
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import aiohttp
import random
import requests
import asyncio
import subprocess

class Miscellaneous(commands.Cog, name="Miscellaneous"):

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def uptime(self, ctx):
        delta_uptime = datetime.utcnow() - self.bot.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        await ctx.send("I have been up for "f"{days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")

    @commands.command()
    async def winner(self, ctx):
        try:
            user = ctx.message.mentions[0]
        except Exception:
            memberlist = ctx.message.guild.members
            user = memberlist[random.randint(0, len(memberlist))]
        await ctx.send("Congratulations, You are the 999,999th visitor: Congratulations you WON!")

    @commands.command()
    async def loser(self, ctx):
        try:
            user = ctx.message.mentions[0]
        except Exception:
            memberlist = ctx.message.guild.members
            user = memberlist[random.randint(0, len(memberlist))]
        await ctx.send("Sorry, {}! You're a loser!".format(user.name))

    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    async def drumpf(self, ctx, user: discord.Member):
        if not ctx.message.channel.permissions_for(ctx.message.author.guild.me).manage_nicknames:
            await ctx.send(":x: I do not have permission to edit nicknames.")
            return
        try:            
        await user.edit(nick="Donald Drumpf")
        except discord.Forbidden:
            await ctx.send("I do not have permission to do that.")
            return
        await ctx.message.delete()
        await ctx.send("Someone has been turned into Donald Drumpf.")

    @commands.command()
    async def wegothim(self, ctx):
        embed = discord.Embed(color=discord.Colour.red(), title="WE GOT HIM!")
        embed.set_image(url="https://media1.tenor.com/images/4a08ff9d3f956dd814fc8ee1cfaac592/tenor.gif?itemid=10407619")
        await ctx.send(embed=embed)

    @commands.command()
    async def bowtourqueen(self, ctx):
        embed = discord.Embed(color=discord.Colour.red(), title="Bow To Your New Queen!")
        embed.set_image(url="https://i.imgur.com/t2LE30K.png")
        await ctx.send(embed=embed)

    @commands.command()
    async def degen(self, ctx):
        embed = discord.Embed(color=discord.Colour.red(), title="You Are All Degnerates Now!")
        embed.set_image(url="https://media1.tenor.com/images/eade076432e4650c25ed82a6368d5ba4/tenor.gif?itemid=15576648")
        await ctx.send(embed=embed)

    @commands.command()
    async def chrome(self, ctx):
        await ctx.send('The current version of Chrome is ' + self.bot.chrome_version)
        
def setup(bot):
    bot.add_cog(Miscellaneous(bot))
import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import json
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import aiohttp
import random
import requests
import asyncio
import subprocess


class Miscellaneous(commands.Cog, name="Miscellaneous"):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def uptime(self, ctx):
        delta_uptime = datetime.utcnow() - self.bot.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        await ctx.send(f"I have been up for {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")

    @commands.command()
    async def winner(self, ctx):
        try:
            user = ctx.message.mentions[0]
        except:
            memberlist = ctx.message.guild.members
            user = random.choice(memberlist)
        await ctx.send("Congratulations, You are the 999,999th visitor: Congratulations you WON!")

    @commands.command()
    async def loser(self, ctx):
        try:
            user = ctx.message.mentions[0]
        except:
            memberlist = ctx.message.guild.members
            user = random.choice(memberlist)
        await ctx.send(f"Sorry, {user.name}! You're a loser!")

    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    async def drumpf(self, ctx, user: discord.Member):
        if not ctx.message.channel.permissions_for(ctx.me).manage_nicknames:
            await ctx.send(":x: I do not have permission to edit nicknames.")
            return
        try:
            await user.edit(nick="Donald Drumpf")
        except discord.Forbidden:
            await ctx.send("I do not have permission to do that.")
            return
        await ctx.message.delete()
        await ctx.send("Someone has been turned into Donald Drumpf.")

    @commands.command()
    async def wegothim(self, ctx):
        embed = discord.Embed(color=discord.Color.red(), title="WE GOT HIM!")
        embed.set_image(url="https://media1.tenor.com/images/4a08ff9d3f956dd814fc8ee1cfaac592/tenor.gif?itemid=10407619")
        await ctx.send(embed=embed)

    @commands.command()
    async def bowtourqueen(self, ctx):
        embed = discord.Embed(color=discord.Color.red(), title="Bow To Your New Queen!")
        embed.set_image(url="https://i.imgur.com/t2LE30K.png")
        await ctx.send(embed=embed)

    @commands.command()
    async def degen(self, ctx):
        embed = discord.Embed(color=discord.Color.red(), title="You Are All Degenerates Now!")
        embed.set_image(url="https://media1.tenor.com/images/eade076432e4650c25ed82a6368d5ba4/tenor.gif?itemid=15576648")
        await ctx.send(embed=embed)

    @commands.command()
    async def chrome(self, ctx):
        await ctx.send('The current version of Chrome is ' + self.bot.chrome_version)


def setup(bot):
    bot.add_cog(Miscellaneous(bot))
