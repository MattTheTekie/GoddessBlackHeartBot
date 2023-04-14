import requests
import sys
import random
import re
import asyncio
import aiohttp
import discord
from discord.ext import commands
import xml.etree.ElementTree as ET

class Anime(commands.Cog, name="Anime"):
    '''Alles rund um Animes'''

    def __init__(self, bot):
        self.bot = bot

    async def cog_command_error(self, ctx, error):
        print('Error in {0.command.qualified_name}: {1}'.format(ctx, error))

    def checkRole(self, user, roleRec):
        ok = False
        for all in list(user.roles):
            if all.name == roleRec:
                ok = True
        return ok

    @commands.command()
    async def kawaii(self, ctx):
        try:
            user = ctx.message.mentions[0]
        except Exception:
            await ctx.send("Please specify a user.")
            return
        url = 'https://nekos.best/api/v2/neko'
        response = requests.get(url)
        image_data = response.json()
        image_url = image_data['results'][0]['url']
        embed = discord.Embed(title="{} Kawaii {}. Anime.".format(ctx.message.author.name, user.name))
        embed.set_image(url=image_url)
        await ctx.send(embed=embed)


    @commands.command()
    async def nsfw(self, ctx):
        try:
            user = ctx.message.mentions[0]
        except Exception:
            await ctx.send("Please specify a user.")
            return
        url = 'https://nekos.best/api/v2/waifu'
        response = requests.get(url)
        image_data = response.json()
        image_url = image_data['results'][0]['url']
        embed = discord.Embed(title="NSFW")
        embed.set_image(url=image_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=['wave', 'hi', 'ohaiyo'])
    async def hello(self, ctx):
        '''Nonsense gifs zum Hallo sagen'''
        gifs = ['https://cdn.discordapp.com/attachments/102817255661772800/219512763607678976/large_1.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219512898563735552/large.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219518948251664384/WgQWD.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219518717426532352/tumblr_lnttzfSUM41qgcvsy.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219519191290478592/tumblr_mf76erIF6s1qj96p1o1_500.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219519729604231168/giphy_3.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219519737971867649/63953d32c650703cded875ac601e765778ce90d0_hq.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219519738781368321/17201a4342e901e5f1bc2a03ad487219c0434c22_hq.gif']
        msg = f':wave: {random.choice(gifs)}'
        await ctx.send(msg)

    @commands.command(aliases=['nepu', 'topnep'])
    async def nep(self, ctx):
        '''Can't stop the Nep'''
        neps = ['https://cdn.discordapp.com/attachments/102817255661772800/219530759881359360/community_image_1421846157.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219535598187184128/tumblr_nv25gtvX911ubsb68o1_500.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219535698309545984/tumblr_mpub9tTuZl1rvrw2eo2_r1_500.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219535820430770176/dd9f3cc873f3e13fe098429388fc24242a545a21_hq.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219535828773371904/tumblr_nl62nrrPar1u0bcbmo1_500.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219535828995538944/dUBNqIH.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219535906942615553/b3886374588ec93849e1210449c4561fa699ff0d_hq.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219536353841381376/tumblr_nl9wb2qMFD1u3qei8o1_500.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219536345176080384/tumblr_njhahjh1DB1t0co30o1_500.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219536356223877120/tumblr_njkq53Roep1t0co30o1_500.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219536424121139210/tumblr_oalathnmFC1uskgfro1_400.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219536451807739904/tumblr_nfg22lqmZ31rjwa86o1_500.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219536686529380362/tumblr_o98bm76djb1vv3oz0o1_500.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219537181440475146/tumblr_mya4mdVhDv1rmk3cyo1_500.gif',
                'https://i.imgur.com/4xnJN9x.png',
                'https://i.imgur.com/bunWIWD.jpg']
        nepnep = ['topnep',
                  'Can\'t pep the nep',
                  'Flat is justice',
                  'nep nep nep nep nep nep nep nep nep nep nep',
                  'Nepgear > your waifu']
        msg = f'{random.choice(nepnep)} {random.choice(neps)}'
        await ctx.send(msg)

#    @commands.command(aliases=['headpat'])
#    async def pat(self, ctx, member: discord.Member = None):
#        '''/r/headpats Pat Pat Pat :3
#
#        Beispiel:
#        -----------
#
#        :pat @Der-Eddy#6508
#        '''
#        gifs = ['https://gfycat.com/PoisedWindingCaecilian',
#                'https://cdn.awwni.me/sou1.jpg',
#                'https://i.imgur.com/Nzxa95W.gifv',
#                'https://cdn.awwni.me/sk0x.png',
#                'https://i.imgur.com/N0UIRkk.png',
#                'https://cdn.awwni.me/r915.jpg',
#                'https://i.imgur.com/VRViMGf.gifv',
#                'https://i.imgur.com/73dNfOk.gifv',
#                'https://i.imgur.com/UXAKjRc.jpg',
#                'https://i.imgur.com/dzlDuNs.jpg',
#                'https://i.imgur.com/hPR7SOt.gif',
#                'https://i.imgur.com/IqGRUu4.gif',
#                'https://68.media.tumblr.com/f95f14437809dfec8057b2bd525e6b4a/tumblr_omvkl2SzeK1ql0375o1_500.gif',
#                'https://i.redd.it/0ffv8i3p1vrz.jpg',
#                'http://i.imgur.com/3dzA6OU.png',
#                'http://i.imgur.com/vkFKabZ.jpg',
#                'https://i.imgur.com/Lb4p20s.jpg',
#                'https://cdn.awwni.me/snot.jpg',
#                'https://i.imgur.com/5yEOa6u.jpg',
#                'https://i.redd.it/dc7oebkfsetz.jpg']
#
#        if member == ctx.me:
#            msg = f'Arigato {ctx.author.mention} <:Hiding:322410632517517324> \n{random.choice(gifs)}'
#            await ctx.send(msg)
#        elif member is not None:
#            msg = f'{ctx.author.mention} tätschelt dich {member.mention} :3 \n{random.choice(gifs)}'
#            await ctx.send(msg)

    @commands.command(aliases=['rate', 'waifu'])
    async def ratewaifu(self, ctx, *, waifuName: str):
        '''Rate my waifu

        Beispiel:
        -----------

        :ratewaifu Sagiri
        '''
        waifu = waifuName.lower()
        bestWaifus = ['kobeni', 'emilia', 'shinobu', 'karen', 'shouko', 'shoko',
                      'minori', 'chidori', 'sagiri', 'mashiro', 'last order',
                      'saki', 'makoto', 'yui', 'nep', 'nepgear', 'taiga']
        trashWaifus = ['shino', 'rikka']
        #this lists are highly biased, but who cares ¯\_(ツ)_/¯
        if waifu in bestWaifus:
            rating = 10
        elif waifu in trashWaifus:
            rating = 0
        else:
            rating = hash(waifu) % 10

        if waifu == 'emilia':
            emoji = '<:Emilia:230684388084416512>'
        elif waifu == 'shinobu':
            emoji = '<:Shinobu:303302053688770561>'
        elif waifu == 'mashiro':
            emoji = '<:mashiro:266233568626343936>'
        elif waifu == 'sagiri':
            emoji = '<:Sagiri:407630432319045634>'
        elif waifu == 'nep' or waifu == 'neptunia' or waifu == 'nepgear':
            emoji = '<:nep:261230988758220822>'
        elif rating < 2:
            emoji = ':put_litter_in_its_place:'
        elif rating < 5:
            emoji = '<:k3llyLUL:341946977266827264>'
        elif rating < 7:
            emoji = '<:k3llyTHINK:341946932639432704>'
        elif rating < 9:
            emojis = ['<:faeGasm:298772756412104704>', '<:naroGasm:341200647741243393>']
            emoji = random.choice(emojis)
        elif rating < 10:
            emojis = ['<:kanoLewd:230662559458525185>', '<:fowShy:230662561580843008>', '<:mendoLewd:230662561169801216>']
            emoji = random.choice(emojis)
        elif rating == 10:
            emojis = ['<:okhand:335170448666918923>', '<:nepnep:314906910061101057>', '<:gaku:249970768786489345>', '<:faeWant:313430419661914113>']
            emoji = random.choice(emojis)

        msg = f'{emoji} I rate **{waifuName}** a **{rating}/10**'
        await ctx.send(msg)

def setup(bot):
    bot.add_cog(Anime(bot))
