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
        self.character_mode = False
        self.character_name = ""

    @commands.command()
    @commands.before_invoke(get_user_input)
    async def ai(self, ctx, *, prompt: str):
        headers = {
            'Authorization': f'Bearer {self.openai_token}',
            'Content-Type': 'application/json'
        }

        data = {
            'model': 'text-davinci-003',
            'prompt': f'"{prompt}"\nAI:',
            'temperature': 0.7,
            'max_tokens': 256,
            'stop': ['Human:', 'AI:']
        }

        if self.character_mode:
            data['prompt'] = f'{prompt}\n{self.character_name}:'
        else:
            data['prompt'] = f'{prompt}\nAI:'

        async with aiohttp.ClientSession() as session:
            async with ctx.typing():
                user_input = await self.get_user_input(ctx)
                if self.character_mode:
                    data['prompt'] = f'{prompt}\n{self.character_name}: {user_input}\n{self.character_name}:'
                else:
                    data['prompt'] = f'{prompt}\nUser: {user_input}\nAI:'

                async with session.post('https://api.pawan.krd/v1/completions', headers=headers, json=data) as response:
                    if response.status == 200:
                        result = await response.json()
                        text = result['choices'][0]['text']
                        if self.character_mode:
                            await ctx.send(f"{self.character_name}: {text}")
                        else:
                            await ctx.send(f"```\n{text}\n```")
                    else:
                        await ctx.send(f"Command failed with status code {response.status}")

    async def get_user_input(self, ctx: commands.Context):
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        try:
            user_input_msg = await self.bot.wait_for('message', check=check, timeout=120.0)
            return user_input_msg.content
        except asyncio.TimeoutError:
            await ctx.send("Command timed out.")
            raise

    @commands.command()
    async def charactermode(self, ctx, *, name: str):
        self.character_mode = True
        self.character_name = name
        await ctx.send(f"Now in character mode as {name}.")
        await ctx.message.add_reaction('👌')

    @commands.command()
    async def normalmode(self, ctx):
        self.character_mode = False
        self.character_name = ""
        await ctx.send("Now in normal mode.")
        await ctx.message.add_reaction('👌')

def setup(bot):
    bot.add_cog(AI(bot))
