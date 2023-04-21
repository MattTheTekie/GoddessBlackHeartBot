import discord
from discord.ext import commands
import aiohttp

class AI(commands.Cog, name="AI"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()        
    async def ai(self, ctx, *, prompt):
        data = {
            "model": "openai:gpt-3.5-turbo",
            "prompt": prompt
        }
        # Send typing indicator to indicate bot is processing request
        async with ctx.typing():
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post('http://127.0.0.1:8080/api', json=data) as response:
                        result = await response.json()
                        await ctx.send(f"```\n{result['data']}\n```")
            except Exception as e:
                await ctx.send(f"An error occurred while processing your request: {e}")

def setup(bot):
    bot.add_cog(AI(bot))
