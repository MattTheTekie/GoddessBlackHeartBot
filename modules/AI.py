
import discord
from discord.ext import commands
import aiohttp

class AI(commands.Cog, name="AI"):
    def __init__(self, bot):
        self.bot = bot
        self.anime_character = None

    @commands.command()        
    async def ai(self, ctx, *, prompt):
        if prompt.lower().startswith("setch "):
            self.anime_character = prompt[14:]
            await ctx.send(f"AI model set to: {self.anime_character}")
            await self.update_bot_profile()
        else:
            data = {
                "model": self.get_ai_model(),
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

    def get_ai_model(self):
        if self.anime_character:
            return f"openai:gpt-3.5-{self.anime_character.lower().replace(' ', '-')}"
        else:
            return "openai:gpt-3.5-turbo"

    async def update_bot_profile(self):
        if self.anime_character:
            username = self.anime_character
            await self.bot.user.edit(username=username)

    @commands.Cog.listener()
    async def on_ready(self):
        await self.update_bot_profile()

def setup(bot):
    bot.add_cog(AI(bot))
