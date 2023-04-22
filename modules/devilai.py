
import discord
from discord.ext import commands
import aiohttp


class devilai(commands.Cog, name="devilai"):
    def __init__(self, bot):
        self.bot = bot
        self.prompt_history = {}

    @commands.command()        
    async def devilai(self, ctx, *, prompt):
        user_id = ctx.author.id
        if user_id in self.prompt_history:
            prompt = self.prompt_history[user_id] + " " + prompt

        data = {
            "model": "openai:text-davinci-002",
            "prompt": prompt
        }

        async with ctx.typing():
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post('http://127.0.0.1:8080/api', json=data) as response:
                        result = await response.json()
                        output = result['data']
                        if 'prompt' in result:
                            prompt = result['prompt']
                            self.prompt_history[user_id] = prompt
                        await ctx.send(f"```\n{output}\n```")
            except Exception as e:
                await ctx.send(f"An error occurred while processing your request: {e}")

def setup(bot):
    bot.add_cog(devilai(bot))
