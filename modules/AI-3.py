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

class AI(commands.Cog, name="AI"):
    def __init__(self, bot):
        self.bot = bot
        self.openai_token = "pk-lqRPVysXvAPeooisGFSZkNLzVGamczCHbarsOnAoEVzlhpPt"

    @commands.command()
    async def ai(self, ctx, *, prompt: str):
        headers = {
            'Authorization': f'Bearer {self.openai_token}',
            'Content-Type': 'application/json'
        }
        data = {
            'model': 'text-davinci-002',
            'prompt': f'"{prompt}"\nAI:',
            'temperature': 0.7,
            'max_tokens': 256,
            'stop': ['Human:', 'AI:']
        }

        async with aiohttp.ClientSession() as session:
            user_input = await self.get_user_input(ctx)
            data['prompt'] = f'{prompt}\nUser: {user_input}\nAI:'
            
            async with ctx.typing():
                async with session.post('https://api.pawan.krd/v1/completions', headers=headers, json=data) as response:
                    if response.status == 200:
                        result = await response.json()
                        text = result['choices'][0]['text']
                        await ctx.send(f"```\n{text}\n```")
                    else:
                        await ctx.send(f"Command failed with status code {response.status}")

    async def get_user_input(self, ctx):
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        user_input_msg = await self.bot.wait_for('message', check=check)
        return user_input_msg.content

def setup(bot):
    bot.add_cog(AI(bot))
