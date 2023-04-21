
import discord
from discord.ext import commands
import aiohttp

class AI2(commands.Cog, name="AI2"):
    def __init__(self, bot):
        self.bot = bot
        self.prompt_history = {} # stores the prompt history for each user

    @commands.command()        
    async def ai2(self, ctx, *, prompt):
        # Retrieve prompt history for this user
        user_id = ctx.author.id
        if user_id in self.prompt_history:
            prompt = self.prompt_history[user_id] + " " + prompt
        
        data = {
            "model": "openai:text-davinci-002",
            "prompt": prompt
        }

        # Send typing indicator to indicate bot is processing request
        async with ctx.typing():
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post('http://127.0.0.1:8080/api', json=data) as response:
                        result = await response.json()
                        output = result['data']
                        prompt = result['prompt'] # Update prompt with previous messages sent
                        self.prompt_history[user_id] = prompt # Store prompt history for this user
                        await ctx.send(f"```\n{output}\n```")
            except Exception as e:
                await ctx.send(f"An error occurred while processing your request: {e}")

def setup(bot):
    bot.add_cog(AI2(bot))
