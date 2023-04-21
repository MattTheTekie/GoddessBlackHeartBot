import discord
from discord.ext import commands
import requests

class AI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ai(self, ctx, *, prompt: str):
        url = 'http://127.0.0.1:8080/api'
        headers = {'Content-Type': 'application/json'}
        data = {
            'model': 'openai:gpt-3.5-turbo',
            'prompt': prompt
        }
        response = requests.post(url, headers=headers, json=data)
        await ctx.send(response.json()['text'])

def setup(bot):
    bot.add_cog(AI(bot))
