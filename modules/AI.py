import discord
from discord.ext import commands
import aiohttp

class AI(commands.Cog, name="AI"):
    def __init__(self, bot):
        self.bot = bot
        self.anime_character = None

    @commands.command()
    async def setch(self, ctx, *, anime_character=None):
        if anime_character:
            self.anime_character = anime_character
            await ctx.send(f"AI model set to: {self.anime_character}")
            await ctx.message.add_reaction('👌')
        else:
            self.anime_character = None
            await ctx.send("Session state of the AI model has been reset.")
            await ctx.message.add_reaction('👌')

    @commands.command()
    async def ai(self, ctx, *, prompt):
        data = {
            "model": self.get_ai_model(),
            "prompt": prompt,
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

    def get_ai_model(self):
        if self.anime_character:
            return "openai:text-davinci-003"
        else:
            return "openai:text-davinci-002"

def setup(bot):
    bot.add_cog(AI(bot))
