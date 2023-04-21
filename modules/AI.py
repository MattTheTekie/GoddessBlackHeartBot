import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import json
from datetime import date, time, datetime, timedelta
import aiohttp
import random
import requests
import asyncio

class AI(commands.Cog, name="AI"):
    def __init__(self, bot):
        self.bot = bot

    async def preflight(self, ctx, prompt):
        async with aiohttp.ClientSession() as session:
            async with session.options('http://127.0.0.1:8080/api', headers={'Content-Type': 'application/json', 'Access-Control-Request-Method': 'POST', 'Access-Control-Request-Headers': 'Content-Type'}) as resp:
                if resp.status != 200:
                    await ctx.send(f"Preflight failed with status {resp.status}")
                    return False
                else:
                    return True

    @commands.command()
    async def ai(self, ctx, *, prompt):
        if not await self.preflight(ctx, prompt):
            return

        async with aiohttp.ClientSession() as session:
            data = {
                "model": "openai:gpt-3.5-turbo",
                "prompt": prompt
            }
            async with session.post('http://127.0.0.1:8080/api', json=data) as resp:
                if resp.status == 200:
                    result = await resp.json()
                    await ctx.send(f"```\n{result['text']}\n```")
                else:
                    await ctx.send(f"Command failed with status {resp.status}")

def setup(bot):
    bot.add_cog(AI(bot))
