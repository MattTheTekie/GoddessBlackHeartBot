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
        self.character_name = None
        self.dialogue_history = []

    @commands.command()
    async def ai(self, ctx, *, prompt: str):
        headers = {
            'Authorization': f'Bearer {self.openai_token}',
            'Content-Type': 'application/json'
        }
        if self.character_name:
            data = {
                'model': 'text-davinci-002',
                'prompt': f'"{prompt}"\n{self.character_name}:',
                'temperature': 0.7,
                'max_tokens': 256,
                'stop': [f'{self.character_name}:', 'Human:', 'AI:']
            }
        else:
            data = {
                'model': 'text-davinci-002',
                'prompt': f'{prompt}\n',
                'temperature': 0.7,
                'max_tokens': 256,
                'stop': ['Human:', 'AI:']
            }

        async with aiohttp.ClientSession() as session:
            user_input = await self.get_user_input(ctx)
            if self.character_name:
                data['prompt'] = f'{prompt}\nUser: {user_input}\n{self.character_name}:'
            else:
                data['prompt'] = f'{prompt}\nUser: {user_input}'

            async with ctx.typing():
                async with session.post('https://api.pawan.krd/v1/completions', headers=headers, json=data) as response:
                    if response.status == 200:
                        result = await response.json()
                        text = result['choices'][0]['text']
                        self.dialogue_history.append(f"{self.character_name}: {prompt}\nUser: {user_input}\n{text}")
                        if len(self.dialogue_history) > 10: # keep only the last 10 messages in memory
                            self.dialogue_history.pop(0)
                        await ctx.send(f"```\n{text}\n```")
                    else:
                        await ctx.send(f"Command failed with status code {response.status}")

    @commands.command()
    async def set_character(self, ctx, *, character: str):
        self.character_name = character
        await ctx.send(f"Set anime character to {self.character_name}")

    @commands.command()
    async def dialogue_history(self, ctx):
        if len(self.dialogue_history) == 0:
            await ctx.send("No dialogue history yet.")
        else:
            all_messages = "\n\n".join(self.dialogue_history)
            await ctx.send(f"```\n{all_messages}\n```")

    async def get_user_input(self, ctx):
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        user_input_msg = await self.bot.wait_for('message', check=check)
        return user_input_msg.content

def setup(bot):
    bot.add_cog(AI(bot))
