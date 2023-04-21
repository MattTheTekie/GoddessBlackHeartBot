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
        response_dict = response.json()
        text = response_dict.get('text')
        if text:
            await ctx.send(text)
        else:
            await ctx.send("Sorry, I couldn't generate a response.")
def setup(bot):
    bot.add_cog(AI(bot))
