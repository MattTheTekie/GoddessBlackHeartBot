import discord
from discord.ext import commands
import random
import requests
import aiohttp
from lxml import html
import json
from io import BytesIO, StringIO

class Fun(commands.Cog, name="Fun"):

    def __init__(self, bot):
        self.bot = bot
#        self.quotes = json.loads(open('quotes.json', 'r', encoding='utf-8').read())
        self.quotes = json.loads(open('quotes.json', 'r').read())

#    @commands.command()
#    async def meme(self, meme):
#        await meme.send("This feature has not been implemented yet.")

    @commands.command(aliases=['ask'], name='8ball')
    async def _8ball(self, ctx, *, question):
        responses = [['Yes, definitely.', 'Of course! Bill Cipher would agree!', 'Did an iDroid program me?',
                      'The answer is simple: 25-5-19',
                      'My answer is the opposite of "no."', 'Absolutely, you weirdo!',
                      'I vote yes. What about you?',
                      '**Yes.**', 'BHV', 'Sure. Why not?'],
                     ['Reply hazy, try again later.', 'I am unable to answer this right now.',
                      'You\'ll have to ask again later.', 'I don\'t know. I just want to watch \"Saturday Night Live.\"',
                      'I do not know. Perhaps Donald Trump can answer this.',
                      'I am certain there is not an answer for this.', 'Why are you asking me about this?',
                      'Hold on. I\'m playing \"Doki Doki Literature Club\" right now.',
                      'Go ask the man living ***IN A VAN DOWN BY THE RIVER!!!***', '```I AM ERROR```'],
                     ['Absolutely not.',
                      'Here\'s my answer: What\'s at the beginning of \"Never\" and what comes after that?',
                      'Keep wishing. Maybe you will get "yes" for an answer.', 'That\'s a definitive no.', '**No.**',
                      'The answer to that question is also the answer to you surviving a fall from 10,000 feet.',
                      'Pffft. Of course not.']]
        await ctx.send(random.choice(random.choice(responses)))

    @commands.command()
    async def kiss(self, ctx):
        try:
            user = ctx.message.mentions[0]
        except Exception:
            await ctx.send("Please specify a user.")
            return
        url = 'https://nekos.life/api/v2/img/kiss'
        response = requests.get(url)
        image = response.json()
        embed = discord.Embed(title="{} kissed {}. How comforting.".format(ctx.message.author.name, user.name))
        embed.set_image(url=image['url'])
        await ctx.send(embed=embed)

    @commands.command()
    async def hug(self, ctx):
        try:
            user = ctx.message.mentions[0]
        except Exception:
            await ctx.send("Please specify a user.")
            return
        url = 'https://nekos.life/api/v2/img/hug'
        response = requests.get(url)
        image = response.json()
        embed = discord.Embed(title="{} hugged {}. How comforting.".format(ctx.message.author.name, user.name))
        embed.set_image(url=image['url'])
        await ctx.send(embed=embed)
        
    @commands.command()
    async def tickle(self, ctx):
        try:
            user = ctx.message.mentions[0]
        except Exception:
            await ctx.send("Please specify a user.")
            return
        url = 'https://nekos.life/api/v2/img/tickle'
        response = requests.get(url)
        image = response.json()
        embed = discord.Embed(title="{} tickled {}. How comforting.".format(ctx.message.author.name, user.name))
        embed.set_image(url=image['url'])
        await ctx.send(embed=embed)

    @commands.command()
    async def poke(self, ctx):
    try:
        user = ctx.message.mentions[0]
    except Exception:
        await ctx.send("Please specify a user.")
        return
    url = 'https://nekos.best/api/v2/poke'
    response = requests.get(url)
    image_data = response.json()
    image_url = image_data['results'][0]['url']
    embed = discord.Embed(title="{} poked {}. How comforting.".format(ctx.message.author.name, user.name))
    embed.set_image(url=image_url)
    await ctx.send(embed=embed)

    @commands.command()
    async def slap(self, ctx):
        try:
            user = ctx.message.mentions[0]
        except Exception:
            await ctx.send("Please specify a user.")
            return
        url = 'https://nekos.life/api/v2/img/slap'
        response = requests.get(url)
        image = response.json()
        embed = discord.Embed(title="{} slapped {}. How comforting.".format(ctx.message.author.name, user.name))
        embed.set_image(url=image['url'])
        await ctx.send(embed=embed)

    @commands.command()
    async def cuddle(self, ctx):
        try:
            user = ctx.message.mentions[0]
        except Exception:
            await ctx.send("Please specify a user.")
            return
        url = 'https://nekos.life/api/v2/img/cuddle'
        response = requests.get(url)
        image = response.json()
        embed = discord.Embed(title="{} cuddled {}. How comforting.".format(ctx.message.author.name, user.name))
        embed.set_image(url=image['url'])
        await ctx.send(embed=embed)

    @commands.command()
    async def pat(self, ctx):
        try:
            user = ctx.message.mentions[0]
        except Exception:
            await ctx.send("Please specify a user.")
            return
        url = 'https://nekos.life/api/v2/img/pat'
        response = requests.get(url)
        image = response.json()
        embed = discord.Embed(title="{} patted {}. How comforting.".format(ctx.message.author.name, user.name))
        embed.set_image(url=image['url'])
        await ctx.send(embed=embed)

    @commands.command()
    async def urban(self, ctx, *, term):
        if not ctx.message.channel.is_nsfw():
            await ctx.send("Due to the fact that some definitions are not appropriate, this command can only be used in NSFW channels.")
            return
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get('http://api.urbandictionary.com/v0/define?term={}'.format(term)) as entry:
                    entry = await entry.json()
                    entry = entry.get('list')[0]
        except Exception:
            await ctx.send("That term could not be found on Urban Dictionary.")
            return
        word = entry.get('word')
        definition = str(entry.get("definition"))
        example = str(entry.get("example"))
        link = str(entry.get("permalink"))
        author = str(entry.get("author"))
        thumbsup = str(entry.get("thumbs_up"))
        thumbsdown = str(entry.get("thumbs_down"))
        embed = discord.Embed(color=discord.Colour.lighter_grey(), title="{}".format(word), url=link,
                              description=definition)
        if len(example) == 0:
            embed.add_field(name="Example: ", value="There's no example for this term.", inline=False)
        elif len(example) >= 1024:
            example = example[:1021]
            embed.add_field(name="Example: ", value=example + "...", inline=False)
        else:
            embed.add_field(name="Example: ", value=example, inline=False)
        embed.add_field(name=":thumbsup: ", value=thumbsup + " liked this.")
        embed.add_field(name=":thumbsdown: ", value=thumbsdown + " disliked this.")
        embed.set_footer(text="{} wrote this definition on Urban Dictionary.".format(author))
        await ctx.send(embed=embed)

    @commands.command()
    async def randomfact(self, ctx):
        """async with aiohttp.ClientSession() as session:
            async with session.get('https://www.cs.cmu.edu/~bingbin/index.html') as entry:
                tree = await html.fromstring(entry.content)"""
        page = requests.get('https://www.cs.cmu.edu/~bingbin/index.html')
        tree = html.fromstring(page.content)
        facts = tree.xpath('//p/text()')
        await ctx.send(facts[random.randint(0, len(facts))])

    @commands.command()
    async def randomquote(self, ctx):
        quote = self.quotes[str(random.randint(0, 46))]
#        await ctx.send(quote.encode("utf-8"))
        await ctx.send(quote)

    def getImage(self, url):
        response = requests.get(url)
        image = response.json()
        image = image.get('url')
        return image

#    @commands.command(pass_context=True, aliases=['achievement', 'ach'])
#    async def mc(self, ctx, *, txt:str):
#    """Generate a Minecraft Achievement"""
#    api = "https://skinmc.net/en/achievement/{0}/Achievement+Get%21/{1}".format(ctx.message.author.name, txt.replace(" ", "+"))
#    b = await self.bot.bytes_download(api)
#    i = 0
#    while sys.getsizeof(b) == 88 and i != 10:
#        b = await self.bot.bytes_download(api)
#        if sys.getsizeof(b) != 0:
#            i = 10
#        else:
#            i += 1
#    if i == 10 and sys.getsizeof(b) == 88:
#        await ctx.send("Minecraft Achievement Generator API is bad, pls try again")
#        return
#    await ctx.send(file=discord.File(fp=io.BytesIO(b), filename='achievement.png'))

def setup(bot):
    bot.add_cog(Fun(bot))
