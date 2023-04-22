import discord
from discord.ext import commands
import aiohttp

class AI2(commands.Cog, name="AI2"):
    def __init__(self, bot):
        self.bot = bot
        self.prompt_history = {}

    @commands.command()        
    async def ai2(self, ctx, *, prompt):
        user_id = ctx.author.id
        if user_id in self.prompt_history:
            prompt = self.prompt_history[user_id] + " " + prompt

        data = {
            "model": "openai:gpt-3.5-turbo",
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
                        for chunk in [output[i:i+2000] for i in range(0, len(output), 2000)]:
                            await ctx.send(f"```\n{chunk}\n```")
            except Exception as e:
                await ctx.send(f"An error occurred while processing your request: {e}")

def setup(bot):
    bot.add_cog(AI2(bot))
