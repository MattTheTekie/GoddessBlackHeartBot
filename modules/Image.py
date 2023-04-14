import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import random
import requests
import aiohttp
from discord.ext import commands
import json

class Danbooru(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

class Image(commands.Cog, name="Image"):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='danbooru', help='Search for an image on Danbooru.')
    async def danbooru_search(self, ctx, *tags):
        if not tags:
            await ctx.send('Please specify some tags to search for.')
            return
        async with aiohttp.ClientSession() as session:
            results = await self.danbooru.post_list(tags=tags, limit=50, session=session)
        if not results:
            await ctx.send('No results found.')
            return
        result = random.choice(results)
        await ctx.send(result['file_url'])

    @commands.command()
    async def neko(self, ctx):
        if ctx.message.channel.is_nsfw():
            url = 'https://nekos.life/api/v2/img/lewd'
        else:
            url = 'https://nekos.life/api/v2/img/neko'
        response = requests.get(url)
        image = response.json()
        embed = discord.Embed(title="From nekos.life")
        embed.set_image(url=image['url'])
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Image(bot))
