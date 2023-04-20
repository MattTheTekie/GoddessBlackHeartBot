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

class AI(commands.Cog, name="AI"):

    def __init__(self, bot):
        self.bot = bot
        
#    @commands.command()        
#    async def ai(self, ctx: str, *message: str):
#        cmd = '''curl -s --location \'https://api.pawan.krd/v1/completions\' --header \'Authorization: Bearer pk-lqRPVysXvAPeooisGFSZkNLzVGamczCHbarsOnAoEVzlhpPt\' --header \'Content-Type: application/json\' --data \'{
#    "model": "gpt-3.5-turbo",
#    "prompt": "message"\\nAI:",
#    "temperature": 0.7,
#    "max_tokens": 256,
#    "stop": [
#        "Human:",
#        "AI:"
#    ]
#}\' | grep -o \'"text":"[^"]*"\''''
#        try:
#            result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
#            await ctx.send(f"```\n{result}\n```")
#        except subprocess.CalledProcessError as exc:
#            await ctx.send(f"Command failed with exit code {exc.returncode}: ```\n{exc.output}\n```")
#            await ctx.send(msg)

#    @commands.command()
#    async def ai(self, ctx, *, message:str):
#    #async def on_message(self, message):
#        if message.author == self.user:
#            return
#            response = self.openai_response(message.content)
#            await message.channel.send(response)
#             
#            def openai_response(self, message: str) -> str:
#                openai.api_key = "pk-lqRPVysXvAPeooisGFSZkNLzVGamczCHbarsOnAoEVzlhpPt"
#                response = openai.Completion.create(
#                model="text-davinci-003",
#                    prompt=message,
#                    temperature=0,
#                    max_tokens=2000,
#                    top_p=1,
#                    frequency_penalty=0,
#                    presence_penalty=0,
#                )
#                if response.get("choices"):
#                   return response.get("choices")[0]["text"]

    # Set up the OpenAI API client
    openai.api_key = pk-lqRPVysXvAPeooisGFSZkNLzVGamczCHbarsOnAoEVzlhpPt

    @bot.event
    async def on_message(message):
    # Only respond to messages from other users, not from the bot itself
    if message.author == self.bot.user:
        return
    
        # Use the OpenAI API to generate a response to the message
        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{message.content}",
        max_tokens=2048,
        temperature=0.5,
        )
        # Send the response as a message
        await message.channel.send(response.choices[0].text)

def setup(bot):
    bot.add_cog(AI(bot))
