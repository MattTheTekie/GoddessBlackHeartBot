import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import json
from datetime import date, time, datetime, timedelta
import aiohttp
import random
import requests
import asyncio
import subprocess
import openai

class AI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ai(self, ctx):
        await ctx.send("What would you like to say to the AI?")

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel

        user_input = await self.bot.wait_for('message', check=check)

        data = {
            'model': 'openai:gpt-3.5-turbo',
            'prompt': f'Human: {user_input.content}\nAI:',
            'temperature': 0.7,
            'max_tokens': 256,
            'stop': ['Human:', 'AI:']
        }

        async with aiohttp.ClientSession() as session:
            async with session.post('http://127.0.0.1:8080/api', json=data) as response:
                if response.status == 200:
                    result = await response.json()
                    if 'choices' in result:
                        text = result['choices'][0]['text']
                        await ctx.send(f"AI: {text}")
                    else:
                        await ctx.send("Sorry, I didn't get a response from the AI.")
                else:
                    await ctx.send(f"Command failed with status code {response.status}")

def setup(bot):
    bot.add_cog(AI(bot))
