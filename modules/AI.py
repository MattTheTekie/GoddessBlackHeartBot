import discord
from discord.ext import commands
import aiohttp

class AI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ai(self, ctx):
        await ctx.send("Please enter your prompt:")
        prompt = await self.get_user_input(ctx)

        headers = {
            'Content-Type': 'application/json'
        }

        data = {
            'model': 'openai:gpt-3.5-turbo',
            'prompt': f'Human: {prompt}\nAI:',
            'temperature': 0.7,
            'max_tokens': 256,
            'stop': ['Human:', 'AI:']
        }

        async with aiohttp.ClientSession() as session:
            async with ctx.typing():
                async with session.post('http://127.0.0.1:8080/api', headers=headers, json=data) as response:
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
