import sys
import os
import random
import discord
import asyncio
import aiohttp
from discord.ext import commands
from clint.textui import progress
import requests
import subprocess

intents = discord.Intents(messages=True, guilds=True, members=True)
#intents = discord.Intents.default()
#intents = discord.Intents.members()
intents.typing = True
intents.presences = True

# Authorized User_ID's
#AJW_Admins = (219220084982415362, 318528448320634881, 217408285542842368, 617456938904453190, 310496481435975693, 542505944223973377, 253864655556968448, 530918840469684225)
# Authorized User IDs
AJW_Admins = (846112982772613171, 318528448320634881)

class Admin(commands.Cog, name="Admin"):
    '''Commands for the bot admin'''

    def __init__(self, bot):
        self.bot = bot

    async def cog_command_error(self, ctx, error):
        print(f'Error in {ctx.command.qualified_name}: {error}')

    @commands.command(aliases=['quit'], hidden=True)
    @commands.is_owner()
    async def shutdown(self, ctx):
        '''Turn me off :( (BOT OWNER ONLY)'''
        await ctx.send('**👌🏼** Bye!')
        await self.bot.logout()
        sys.exit(0)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def restart(self, ctx):
        '''Restart me (BOT OWNER ONLY)'''
        await ctx.send('**👌🏼** See you soon!')
        try:
            await self.bot.logout()
        except:
            pass
        finally:
            os.system("python38 GoddessBlackHeartBot.py")
        await ctx.send('**👌🏼** Restart Successful!')

    @commands.command()
    async def ls(self, ctx, path: str):
        '''Lists files from the specified path on the hard drive'''
        if ctx.author.id in AJW_Admins:
            await ctx.send(os.listdir(path))
        else:
            await ctx.send('❌ You are not authorized to use this command.')

    @commands.command()
    async def cat(self, ctx, file: str):
        '''Lists the contents of the specified file on the hard drive'''
        if ctx.author.id in AJW_Admins:
            with open(file, 'r') as f:
                f_contents = f.read()
                await ctx.send(f_contents)
        else:
            await ctx.send('❌ You are not authorized to use this command.')

    @commands.command()
    async def touch(self, ctx, text: str, file: str):
        '''Writes text to a file on the hard drive'''
        if ctx.author.id in AJW_Admins:
            with open(file, 'a+') as f:
                f_contents = f.write((text) + "\r\n")
        await ctx.send('✅ wrote test to file in **`{}`**'.format(file))

    @commands.command()
    @commands.is_owner()
    async def rm(self, ctx, file: str):
        if ctx.author.id in AJW_Admins:
            '''Removes Files from path on Hard Drive'''
            os.remove(file)
        await ctx.send('✅ removed **`{}`**'.format(file))

    @commands.command()
    @commands.is_owner()
    async def cmd(self, ctx, cmd: str):
        if ctx.author.id in AJW_Admins:
            '''Runs command from the computers command and directs the output to Discord'''
        # returns output as byte string
        returned_output = subprocess.check_output(cmd, shell=True)

        # using decode() function to convert byte string to string
        await ctx.send(f'```py\n{returned_output}\b```')
        await ctx.send('✅ command **`{}`** ran'.format(cmd))

    @commands.command()
    @commands.is_owner()
    async def sfuser(self, ctx, userid: str, path: str):
        if ctx.author.id in AJW_Admins:
            '''Sends Files in path to user from Hard Drive'''
            user = self.bot.get_user(int(userid))
        await user.send(file=discord.File(path))
        await ctx.send('✅ sent **`{}`** to **`<#{}>`**'.format(path, userid))

    @commands.command()
    @commands.is_owner()
    async def sfch(self, ctx, channelid: str, path: str):
        if ctx.author.id in AJW_Admins:
            '''Sends Files in path to channel from Hard Drive'''
            ch = self.bot.get_channel(int(channelid))
        await ch.send(file=discord.File(path))
        await ctx.send('✅ sent **`{}`** to **`<#{}>`**'.format(path, channelid))

    @commands.command(hidden=True)
    @commands.is_owner()
    async def botavatar(self, ctx, url: str):
        '''Set a new avatar (BOT OWNER ONLY)'''
        if ctx.author.id in AJW_Admins:
            tempBHFile = 'tempBH.png'
        r = requests.get(url)
        with open(tempBHFile, 'wb') as f:
                total_length = int(r.headers.get('content-length'))
                for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
                    if chunk:
                        f.write(chunk)
                        f.flush()
        with open('tempBH.png', 'rb') as f:
                await self.bot.user.edit(avatar=f.read())
        os.remove(tempBHFile)
        asyncio.sleep(2)
        await ctx.send('**👌🏼** My new avatar!\n %s' % self.bot.user.avatar_url)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def servericon(self, ctx, url: str):
        '''Set a new avatar (BOT OWNER ONLY)'''
        tempsvicon = 'tempsvicon.png'
        r = requests.get(url)
        with open('tempsvicon.png', 'wb') as f:
                total_length = int(r.headers.get('content-length'))
                for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
                    if chunk:
                        f.write(chunk)
                        f.flush()
        with open('tempsvicon.png', 'rb') as f:
                await ctx.guild.edit(icon=f.read())
        os.remove(tempsvicon)
        asyncio.sleep(2)
        await ctx.send('**👌🏼** New Server Icon set!') #\n %s' % self.bot.user.avatar_url)

    @commands.command(hidden=True, aliases=['game'])
    @commands.is_owner()
    async def changegame(self, ctx, status: str, gameType: str, *, gameName: str):
        if ctx.author.id in AJW_Admins:
            '''Changes the game currently playing (BOT OWNER ONLY)'''
        gameType = gameType.lower()
        if gameType == 'playing':
            type2 = discord.ActivityType.playing
        elif gameType == 'watching':
            type2 = discord.ActivityType.watching
        elif gameType == 'listening':
            type2 = discord.ActivityType.listening
        elif gameType == 'streaming':
            type2 = discord.ActivityType.streaming
        status = status.lower()
        if status == 'offline' or status == 'off' or status == 'invisible':
            discordStatus = discord.Status.invisible
        elif status == 'idle':
            discordStatus = discord.Status.idle
        elif status == 'dnd' or status == 'disturb':
            discordStatus = discord.Status.dnd
        else:
            discordStatus = discord.Status.online
        guildsCount = len(self.bot.guilds)
        memberCount = len(list(self.bot.get_all_members()))
        gameName = gameName.format(guilds = guildsCount, members = memberCount)
        await self.bot.change_presence(status=discordStatus, activity=discord.Activity(type=type2, name=gameName))
        await ctx.send(f'**👌🏼** Changed the status & game to: **{discordStatus}** {gameType} **{gameName}**')

    @commands.command(hidden=True)
    @commands.is_owner()
    async def changestatus(self, ctx, status: str):
        if ctx.author.id in AJW_Admins:
            '''Changes bot online status (BOT OWNER ONLY)'''
        status = status.lower()
        if status == 'offline' or status == 'off' or status == 'invisible':
            discordStatus = discord.Status.invisible
        elif status == 'idle':
            discordStatus = discord.Status.idle
        elif status == 'dnd' or status == 'disturb':
            discordStatus = discord.Status.dnd
        else:
            discordStatus = discord.Status.online
        await self.bot.change_presence(status=discordStatus)
        await ctx.send(f'**👌🏼** to another status: **{discordStatus}**')

    @commands.command(hidden=True)
    @commands.is_owner()
    async def name(self, ctx, name):
        if ctx.author.id in AJW_Admins:
            '''changes bot global name (BOT OWNER ONLY)'''
        await self.bot.user.edit(username=name)
        msg = f'👌🏼 change my name: **{name}**'
        await ctx.send(msg)

    @commands.command(hidden=True)
    async def servername(self, ctx, name):
        if ctx.author.id in AJW_Admins:
            '''changes server global name (BOT OWNER ONLY)'''
        await ctx.guild.edit(name=name)
        msg = f'👌🏼 change server name: **{name}**'
        await ctx.send(msg)

    @commands.command(hidden=True, aliases=['guilds'])
    @commands.is_owner()
    async def servers(self, ctx):
        if ctx.author.id in AJW_Admins:
            '''Lists the current connected guilds (BOT OWNER ONLY)'''
        msg = '```js\n'
        msg += '{!s:19s} | {!s:>5s} | {} | {}\n'.format('ID', 'Member', 'Name', 'Owner')
        for guild in self.bot.guilds:
            msg += '{!s:19s} | {!s:>5s}| {} | {}\n'.format(guild.id, guild.member_count, guild.name, guild.owner)
        msg += '```'
        await ctx.send(msg)


    @commands.command(hidden=True)
    @commands.is_owner()
    async def leaveserver(self, ctx, guildid: str):
        if ctx.author.id in AJW_Admins:
            '''Leaves a server (BOT OWNER ONLY)
        Example:
        -----------
        : leaveserver 102817255661772800
        '''
        if guildid == 'this':
            await ctx.guild.leave()
            return
        else:
            guild = self.bot.get_guild(int(guildid))
            if guild:
                await guild.leave()
                msg = "👌🏼 Exit from: **{}** **{}** successful!".format(guild.name, guild.id)
            else:
                msg = f":x: Couldn't find a matching guild for this ID!"
        await ctx.send(msg)


    @commands.command(hidden=True)
    @commands.is_owner()
    async def echo(self, ctx, channel: str, *message: str):
        if ctx.author.id in AJW_Admins:
            '''Outputs a message as a bot on a specific channel (BOT OWNER ONLY)'''
        ch = self.bot.get_channel(int(channel))
        msg = ' '.join(message)
        await ch.send(msg)
        await ctx.message.delete()

    @commands.command(hidden=True)
    async def discriminator(self, ctx, disc: str):
        '''Returns users with the respective discriminator'''

        discriminator = disc
        memberList = ''

        for guild in self.bot.guilds:
            for member in guild.members:
                if member.discriminator == discriminator and member.discriminator not in memberList:
                    memberList += f'{member}\n'

        if memberList:
            await ctx.send(memberList)
        else:
            await ctx.send(":x: Couldn't find anyone")
    @commands.command(hidden=True)
    @commands.is_owner()
    @commands.bot_has_permissions(manage_nicknames = True)
    async def nickname(self, ctx, *name):
        '''Changes the server nickname from the bot (BOT OWNER ONLY)'''
        nickname = ' '.join(name)
        await ctx.me.edit(nick=nickname)
        if nickname:
            msg = f'👌🏼 Change my server nickname: **{nickname}**'
        else:
            msg = f'👌🏼 Reset from my server nickname: **{ctx.me.name}**'
        await ctx.send(msg)

    @commands.command(hidden=True)
    @commands.bot_has_permissions(manage_nicknames = True)
    async def setnickname(self, ctx, member: discord.Member=None, *name):
        '''Changes a user's nickname (BOT OWNER ONLY)'''
        if member == None:
            member = ctx.author
        nickname = ' '.join(name)
        await member.edit(nick=nickname)
        if nickname:
            msg = f'👌🏼 Change nickname of {member} to: **{nickname}**'
        else:
            msg = f'👌🏼 Reset nickname for {member} on: **{member.name}**'
        await ctx.send(msg)

    @commands.command(hidden=True)
    async def serverimage(self, ctx, guildid: str):
        '''Grabs icon from a guild if possible (BOT OWNER ONLY)'''
        server = self.bot.get_guild(int(guildid))
        await ctx.send(server.icon_url)
        await ctx.send('✅ Server icon from **`{}`**'.format(guildid))

    @commands.command()
    @commands.is_owner()
    async def lschannels(self, ctx, guildid: str):
        logfile = 'channel.ids.txt'
        server = self.bot.get_guild(int(guildid))
        log = open(logfile,"w+")
        ids = server.channels
        log.write("" + str(ids)  + "\r\n")
        log.close()
        await ctx.send(file=discord.File(logfile))
        await ctx.send('✅ sent **`{}`** from **`{}`**'.format(logfile, server))

    @commands.command()
    @commands.is_owner()
    async def lsusers(self, ctx, guildid: str):
        logfile = 'user.ids.txt'
        server = self.bot.get_guild(int(guildid))
        log = open(logfile,"w+")
        ids = server.members
        log.write("" + str(ids)  + "\r\n")
        log.close()
        await ctx.send(file=discord.File(logfile))
        await ctx.send('✅ sent **`{}`** from **`{}`**'.format(logfile, server))

    @commands.command(hidden=True)
    @commands.bot_has_permissions(create_instant_invite = True)
    async def geninvite(self, ctx, channelid: str, userid: str):
        '''Generates an invite for a guild if possible (BOT OWNER ONLY)'''
        guild = self.bot.get_channel(int(channelid))
        user = self.bot.get_user(int(userid))
        invite = await guild.create_invite(unique=False)
        msg = f'Invite for **{guild.name}** ({guild.id})\n{invite.url}'
        await user.send(msg)

    @commands.command(hidden=True, aliases=['wichteln'])
    async def wichtel(self, ctx, *participants: str):
        '''Useful for the Community Wichtel Event 2018 (BOT OWNER ONLY)'''
        participantsList = list(participants)
        random.shuffle(participantsList)
        msg = 'Imp partners have been determined:\n```'
        for i, val in enumerate(participantsList):
            if i == len(participantsList) - 1:
                msg += f'{val.ljust(10)} ===> {participantsList[0]}\n'
            else:
                msg += f'{val.ljust(10)} ===> {participantsList[i + 1]}\n'

        msg += '```'
        await ctx.send(msg)

    @commands.command(hidden=True)
    async def test(self, ctx):
        '''Test Test Test'''
        await ctx.send('Test')

def setup(bot):
    bot.add_cog(Admin(bot))
