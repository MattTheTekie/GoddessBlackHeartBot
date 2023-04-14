import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import random
import requests
import aiohttp
from discord.ext import commands

class Image(commands.Cog, name="Image"):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def neko(self, ctx):
        if ctx.message.channel.is_nsfw():
            url = 'https://nekos.life/api/v2/img/lewd'
        else:
            url = 'https://nekos.life/api/v2/img/neko'
        response = requests.get(url)
        image = response.json()
        embed = discord.Embed(title="From nekos.life")
        embed.set_image(url=image['url'])
        await ctx.send(embed=embed)

    @commands.command()
    async def konachan(self, context, tags=None, rating=None):
        """Picks a random image from Konachan and displays it."""
        if context.message.channel.is_nsfw():
            if tags is None:
                temp = "?tags=-status%3Adeleted+-loli+-shota&limit=100"
            elif "safe".lower() in tags:
                temp = "?tags=-status%3Adeleted+-loli+-shota+rating:s&limit=100"
            elif "explicit".lower() in tags:
                temp = "?tags=-status%3Adeleted+-loli+-shota+rating:e&limit=100"
            elif "questionable".lower() in tags:
                temp = "?tags=-status%3Adeleted+-loli+-shota+rating:q&limit=100"
            elif "loli".lower() in tags:
                await context.send("We can't show this as it violates Discord ToS.")
                return
            elif "shota".lower() in tags:
                await context.send("We can't show this as it violates Discord ToS.")
                return
            else:
                if rating is None:
                    temp = "?tags=-status%3Adeleted+-loli+-shota+{}&limit=100".format(tags)
                elif "safe".lower() in rating:
                    temp = "?tags=-status%3Adeleted+-loli+-shota+{}+rating:s&limit=100".format(tags)
                elif "explicit".lower() in rating:
                    temp = "?tags=-status%3Adeleted+-loli+-shota+{}+rating:e&limit=100".format(tags)
                elif "questionable".lower() in rating:
                    temp = "?tags=-status%3Adeleted+-loli+-shota+{}+rating:q&limit=100".format(tags)
                else:
                    temp = "?tags=-status%3Adeleted+-loli+-shota+{}+{}&limit=100".format(tags, rating)
            async with aiohttp.ClientSession() as session:
                async with session.get('https://konachan.com/post/index.json{}'
                                               .format(temp)) as resp:
                    data = await resp.json()
                await session.close()
            try:
                selected = random.randint(0, len(data))
                url = data[selected]['file_url']
            except Exception:
                await context.send("We could not find any images with that tag.")
                return
        else:
            await context.send("You need to be in a NSFW channel to run this command.")
            return
        if context.message.guild is not None:
            color = context.message.guild.me.color
        else:
            color = discord.Colour.blurple()
        embed = discord.Embed(color=color, title="Image from Konachan!",
                              description="If you can't see the image, click the title.", url=url)
        embed.add_field(name="Known tags: ", value="`{}`".format(self.taglistlength(data[selected]['tags'])),
                        inline=False)
        embed.add_field(name="Original link: ",
                        value="[Click here](https://konachan.com/post/{})".format(data[selected]['id']),
                        inline=True)
        embed.set_image(url=url)
        embed.set_footer(text="Powered by Konachan.")
        await context.send(embed=embed)

    @commands.command()
    async def yandere(self, context, tags=None, rating=None):
        if context.message.channel.is_nsfw():
            if tags is None:
                temp = "?tags=-status%3Adeleted+-loli+-shota&limit=100"
            elif "safe".lower() in tags:
                temp = "?tags=-status%3Adeleted+-loli+-shota+rating:s&limit=100"
            elif "explicit".lower() in tags:
                temp = "?tags=-status%3Adeleted+-loli+-shota+rating:e&limit=100"
            elif "questionable".lower() in tags:
                temp = "?tags=-status%3Adeleted+-loli+-shota+rating:q&limit=100"
            elif "loli".lower() in tags:
                await context.send("We can't show this as it violates Discord ToS.")
                return
            elif "shota".lower() in tags:
                await context.send("We can't show this as it violates Discord ToS.")
                return
            else:
                if rating is None:
                    temp = "?tags=-status%3Adeleted+-loli+-shota+{}&limit=100".format(tags)
                elif "safe".lower() in rating:
                    temp = "?tags=-status%3Adeleted+-loli+-shota+{}+rating:s&limit=100".format(tags)
                elif "explicit".lower() in rating:
                    temp = "?tags=-status%3Adeleted+-loli+-shota+{}+rating:e&limit=100".format(tags)
                elif "questionable".lower() in rating:
                    temp = "?tags=-status%3Adeleted+-loli+-shota+{}+rating:q&limit=100".format(tags)
                else:
                    temp = "?tags=-status%3Adeleted+-loli+-shota+{}+{}&limit=100".format(tags, rating)
            async with aiohttp.ClientSession() as session:
                async with session.get('https://yande.re/post/index.json{}'
                                               .format(temp)) as resp:
                    data = await resp.json()
                await session.close()
            try:
                selected = random.randint(0, len(data))
                url = data[selected]['file_url']
            except Exception:
                await context.send("We could not find any images with that tag.")
                return
        else:
            await context.send("You need to be in a NSFW channel to run this command.")
            return
        if context.message.guild is not None:
            color = context.message.guild.me.color
        else:
            color = discord.Colour.blurple()
        embed = discord.Embed(color=color, title="Image from Yande.re!",
                              description="If you can't see the image, click the title.", url=url)
        embed.add_field(name="Known tags: ", value="`{}`".format(self.taglistlength(data[selected]['tags'])),
                        inline=False)
        embed.add_field(name="Original link: ",
                        value="[Click here](https://yande.re/post/{})".format(data[selected]['id']),
                        inline=True)
        embed.set_image(url=url)
        embed.set_footer(text="Powered by Yande.re.")
        await context.send(embed=embed)

    @staticmethod
    def rating(integer):
        if integer == 1:
            return "rating:s"
        elif integer == 2:
            return "rating:q"
        elif integer == 3:
            return "rating:e"

    @staticmethod
    def checktags(tagone, tagtwo):
        if "safe".lower() in tagone or "safe".lower() in tagtwo:
            return 1
        elif "questionable".lower() in tagone or "questionable".lower() in tagtwo:
            return 2
        elif "explicit".lower() in tagone or "explicit".lower() in tagtwo:
            return 3
        return 0

    @staticmethod
    def nololitag(tagone, tagtwo):
        if "loli".lower() in tagone or "loli".lower() in tagtwo:
            return False
        if "shota".lower() in tagone or "shota".lower() in tagtwo:
            return False
        return True

    @staticmethod
    def formatrating(tag):
        if "s" in tag:
            return "safe"
        elif "e" in tag:
            return "explicit"
        elif "q" in tag:
            return "questionable"

    @staticmethod
    def taglistlength(taglist):
        if len(taglist) >= 1024:
            return taglist[:1021] + "..."
        else:
            return taglist


def setup(bot):
    bot.add_cog(Image(bot))
