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

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

client = commands.Bot(command_prefix='!')

@client.command()
async def ai(ctx, *, prompt: str):
    url = 'http://100.110.158.36:8080/api'
    headers = {'Content-Type': 'application/json'}
    data = {
        'model': 'openai:gpt-3.5-turbo',
        'prompt': prompt
    }
    response = requests.post(url, headers=headers, json=data)
    await ctx.send(response.json()['text'])

def setup(bot):
    bot.add_cog(AI(bot))
