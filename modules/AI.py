import discord
from discord.ext import commands
import json
import aiohttp
import random
import asyncio
import subprocess

class AI(commands.Cog, name="AI"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ai(self, ctx, *, prompt):
        url = 'http://127.0.0.1:8080/api'
        data = {
            "model": "openai:gpt-3.5-turbo",
            "prompt": prompt
        }
        headers = {
            'Content-Type': 'application/json'
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, data=json.dumps(data)) as response:
                result = await response.json()
                text_result = result.get("text", "")
                await ctx.send(f"```{text_result}```")
        
def setup(bot):
    bot.add_cog(AI(bot))
