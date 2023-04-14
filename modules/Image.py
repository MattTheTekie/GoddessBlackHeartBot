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

    @commands.command(name="Jdanbooru")
    async def danbooru(self, ctx, *, tags):
        # Define API endpoint and request parameters
        api_url = "https://danbooru.donmai.us/posts.json"
        params = {
            "limit": 1,
            "tags": tags
        }
        
        # Send GET request to Danbooru API
        response = requests.get(api_url, params=params)
        
        # Check if response was successful
        if response.status_code == 200:
            # Parse JSON response
            data = json.loads(response.text)
            
            # Check if any posts were found
            if len(data) > 0:
                # Extract image URL from post data
                image_url = "https://danbooru.donmai.us" + data[0]["file_url"]
                
                # Send image to Discord server
                embed = discord.Embed()
                embed.set_image(url=image_url)
                await ctx.send(embed=embed)
            else:
                await ctx.send("No posts found with those tags.")
        else:
            await ctx.send("An error occurred while communicating with the Danbooru API.")
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

    @commands.command(name="danbooru")
    async def danbooru(self, ctx, *, tags):
        # Define API endpoint and request parameters
        api_url = "https://danbooru.donmai.us/posts.json"
        params = {
            "limit": 1,
            "tags": tags
        }
        
        # Send GET request to Danbooru API
        response = requests.get(api_url, params=params)
        
        # Check if response was successful
        if response.status_code == 200:
            # Parse JSON response
            data = json.loads(response.text)
            
            # Check if any posts were found
            if len(data) > 0:
                # Extract image URL from post data
                image_url = "https://danbooru.donmai.us" + data[0]["file_url"]
                
                # Send image to Discord server
                embed = discord.Embed()
                embed.set_image(url=image_url)
                await ctx.send(embed=embed)
            else:
                await ctx.send("No posts found with those tags.")
        else:
            await ctx.send("An error occurred while communicating with the Danbooru API.")

def setup(bot):
    bot.add_cog(Image(bot))
    bot.add_cog(Danbooru(bot))
