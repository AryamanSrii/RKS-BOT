import discord
from discord.ext import commands
from discord.ext import tasks
import logging
from discord.ext.commands import cooldown, BucketType
from discord.ext.commands import (CommandOnCooldown)
import requests
import asyncio
import discord.utils
import functools
from discord.utils import get
import discord, datetime, time
from discord.ext import commands
import math
import os
import keep_alive
import discord
import random
import json
from datetime import datetime
import utils
from discord.utils import find
import datetime
from datetime import datetime, timedelta
from platform import python_version
from time import time
import discord
from discord.ext import commands, tasks
from io import BytesIO
import datetime
from datetime import datetime
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option
from gtts import gTTS
import aiohttp
import asyncio
import json
import decimal
intents = discord.Intents.default()

from PIL import Image
from io import BytesIO

intents.members = True

client = commands.Bot(
    command_prefix=['r!','R!'],case_insensitive=True, intents=intents)
slash = SlashCommand(client, sync_commands=True)


@slash.slash(name="tts",
             description="Text to Audio",
             options=[
               create_option(
                 name="sentence",
                 description="Say Any sentence",
                 option_type=3,
                 required=True
               )
             ])
async def tts(ctx, sentence):
      myobj = gTTS(text=sentence, lang='en', slow=False)
      language = 'en'
      myobj.save("audio.mp3")
      await ctx.send(file=discord.File('audio.mp3'))

from io import BytesIO

@slash.slash(name="Stat",
             description="Command to check info for any coin.",
             options=[
               create_option(
                 name="coin",
                 description="Say Any Coin",
                 option_type=3,
                 required=True
               )
             ])
async def stat(ctx, coin):
  coin = coin
  try: 
      async with aiohttp.ClientSession() as r:
          async with r.get(f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={coin}") as r:
           data = await r.json()
           price = decimal.Decimal(data[0]["current_price"])
           high = decimal.Decimal(data[0]["high_24h"])
           low = decimal.Decimal(data[0]["low_24h"])
           pc =  decimal.Decimal(data[0]["price_change_24h"])

           embed = discord.Embed(title = f" Stats", description = f'Recent Stats of {coin}  ', colour = discord.Colour.blue()) 
           embed.add_field(name= '💸 Price', value = f"{round(price, 10)} $", inline = False)
           embed.add_field(name= '💷 Market Cap', value = f'{data[0]["market_cap"]}$', inline = False) 
           embed.add_field(name= '📈 High 24hrs', value = f"{round(high, 10)}$", inline = False) 
           embed.add_field(name= '📉 Low 24hrs ', value = f"{round(low, 10)}$", inline = False) 
           embed.add_field(name= 'Price Change', value = f"{round(pc, 10)}$", inline = False) 
           embed.add_field(name= 'Price Change %', value = f'{data[0]["price_change_percentage_24h"]}%', inline = True) 
           embed.add_field(name= 'Market Cap Change', value = f'{data[0] ["market_cap_change_24h"]}$', inline = True) 
           embed.add_field(name= 'Total Supply', value = f'{data[0]["total_supply"]}', inline = True) 
           await ctx.send(embed = embed)
  except:
           embed = discord.Embed(title = "⚠️ Coin Not Found", colour = discord.Colour.blue()) 
           embed.set_footer(text = "If You used Short forms like DOGE or BTC, please use their full names and try again")
           await ctx.send(embed=embed)
def time_encode(sec):
    time_type, newsec = 'seconds', int(sec)
    if sec > 60:
        newsec, time_type = round(sec / 60), 'minutes'
        if sec > 3600:
            newsec, time_type = round(sec / 3600), 'hours'
            if sec > 86400:
                newsec, time_type = round(sec / 86400), 'days'
                if sec > 2592000:
                    newsec, time_type = round(sec / 2592000), 'months'
                    if sec > 31536000:
                        newsec, time_type = round(sec / 31536000), 'years'
    if str(newsec) == '1': return str(str(newsec) + ' ' + time_type[:-1])
    return str(str(newsec) + ' ' + time_type)


for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'Cogs.{filename[:-3]}')


@client.command(hidden=True)
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'Cogs.{extension}')
    await ctx.send('Succesfully loaded module')


@client.command(hidden=True)
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'Cogs.{extension}')
    await ctx.send('Succesfully unloaded module')


@client.command(hidden=True)
@commands.is_owner()
async def reload(ctx, extension):
    client.reload_extension(f'Cogs.{extension}')
    await ctx.send('Succesfully reloaded module')


class CogName(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(CogName(bot))



time_before = datetime.now()
s1 = time_before.strftime("%H:%M:%S")




@client.command()
async def delchannels(ctx):
    for c in ctx.guild.channels: # iterating through each guild channel
        await c.delete()
       
@client.event
async def on_guild_join(guild):
    channel = client.get_channel(842405025489879051)
    embed = discord.Embed(
        title="I Joined a new server",
        description=
        f"Name: {guild},\nMembers: {guild.member_count}\nid: {guild.id} \nOwner: {guild.owner}"
    )
    embed.set_thumbnail(url=guild.icon_url)
    embed.set_footer(text=f"{len(client.guilds)} servers.")
    await channel.send(embed=embed)


@client.event
async def on_guild_remove(guild):
    channel = client.get_channel(842405025489879051)
    embed = discord.Embed(
        title="I was removed from a server",
        description=
        f"Name: {guild},\nMembers: {guild.member_count}id: {guild.id}")
    embed.set_thumbnail(url=guild.icon_url)
    embed.set_footer(text=f"{len(client.guilds)} servers.")

    await channel.send(embed=embed)




class NewHelpName(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = discord.Embed(description=page, colour = discord.Colour.red(), title = ":bookmark_tabs: | Help Menu")
            emby.set_thumbnail(url = "https://cdn.discordapp.com/avatars/566193564502196235/b624ea7737776938c070f6693c91abc9?size=2048")
            emby.set_footer(text = "Check Bot Status at https://RKS.aryamansri.repl.co ")
            await destination.send(embed=emby)

client.help_command = NewHelpName()


@client.command()
async def hp(ctx):
    page1 = discord.Embed (
        title = 'Moderation',
        description = '```announcerole ban clearwarn find kick lock massban mute nickname prune unban unlock unmute warn warns```',
        colour = discord.Colour.blue()
    )
    page2 = discord.Embed (
        title = 'Chatbot',
        description = '`RKS`',
        colour = discord.Colour.blue()
    )
    page3 = discord.Embed (
        title = 'Information',
        description = '```sinfo, userinfo, info, dev_info```',
        colour = discord.Colour.blue()
    )
    page4 = discord.Embed (
        title = 'Utility',
        description = '```Uptime, snipe, pfp```',
        colour = discord.Colour.blue()
    )

    pages = [page1, page2, page3, page4]

    message = await client.send(embed = page1)

    await client.add_reaction(message, '⏮')
    await client.add_reaction(message, '◀')
    await client.add_reaction(message, '▶')
    await client.add_reaction(message, '⏭')

    i = 0
    emoji = ''

    while True:
        if emoji == '⏮':
            i = 0
            await client.edit_message(message, embed = pages[i])
        elif emoji == '◀':
            if i > 0:
                i -= 1
                await client.edit_message(message, embed = pages[i])
        elif emoji == '▶':
            if i < 2:
                i += 1
                await client.edit_message(message, embed = pages[i])
        elif emoji == '⏭':
            i = 2
            await client.edit_message(message, embed=pages[i])
        
        res = await client.wait_for_reaction(message = message, timeout = 30.0)
        if res == None:
            break
        if str(res[1]) != '<Bots name goes here>':  #Example: 'MyBot#1111'
            emoji = str(res[0].emoji)
            await client.remove_reaction(message, res[0].emoji, res[1])

    await client.clear_reactions(message)

def convert(time):
    pos = ["s", "m", "h", "d"]

    time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]

bannedword = ["pog"]
bannedw = ["flurpy"]


@client.event
async def on_message(msg):
    for word in bannedw:
        if word in msg.content:
            await msg.delete()
            user = msg.author
            await user.send(f"You have been banned for using a banned word")
            await user.ban(reason="Banned Words")
            await user.send(f"{user.mention} You were banned for using a banned word ")




    await client.process_commands(msg)



@client.event
async def on_message(msg):
    for word in bannedword:
        if word in msg.content:
            await msg.delete()
            user = msg.author
            await user.send(f"You have been Muted for using a banned word")
            role = discord.utils.get(msg.guild.roles, name="Muted")
            await user.add_roles(role) 
            await msg.send(f"{user} was Muted for using banned word")




    await client.process_commands(msg)



@client.command()
async def ViBeZ(ctx):
    user = ctx.author
    guild = ctx.guild
    role = ctx.guild.get_role(876480277545885786)
    await user.add_roles(role) 
    await ctx.author.send(f"{ctx.author.mention} Your Role has been added successfully. My master has sent you two words, the p one  is the blocked word and whenever you use your message will get deleted and you will get muted for 1h. use of f word will get you banned which works the same for n word ")




class MemberID(commands.Converter):
    async def convert(self, ctx, argument):
        try:
            m = await commands.MemberConverter().convert(ctx, argument)
        except commands.BadArgument:
            try:
                return int(argument, base=10)
            except ValueError:
                raise commands.BadArgument(
                    f"{argument} is not a valid member or member ID."
                ) from None
        else:
            return m.id



@client.command()
async def f(ctx):
    if ctx.channel.id == 847854125114851328:
        await ctx.send("hello")
    else:
        await ctx.send("this command only works in <#847854125114851328>")




@client.command()
async def embed(ctx, *, channel: discord.TextChannel):
    "Create a Embed of your choice"
    await ctx.send("Send me a title for the embed")

    def check(message):
        return (message.author == ctx.author and message.channel == ctx.channel
                and not message.author.bot)

    try:
        msg = await client.wait_for("message", timeout=60.0, check=check)

    except asyncio.TimeoutError:
        return await ctx.send("No title was provided time up")

    else:
        t = msg.content
        if t.content.lower() == "none":
            tit = ""
        else:
            tit = t

        await ctx.send("Now send me the text you want to be in the embed")

    try:
        msg = await client.wait_for("message", timeout=60.0, check=check)
    except asyncio.TimeoutError:
        return await ctx.send("No description was provided")
    else:
        desc = msg.content
        await ctx.send("all set")

    embed = discord.Embed(title=tit, description=desc, colour=0x00c8ff)
    if len(msg.attachments) > 0:
        embed.set_image(url=msg.attachments[0].url)

    await channel.send(embed=embed)



@client.command()
async def invite(ctx):
    embed = discord.Embed(
        title="Information about the bot", colour=discord.Colour.blue())
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/avatars/566193564502196235/b624ea7737776938c070f6693c91abc9?size=2048"
    )
    embed.add_field(
        name="Invite",
        value=
        "[Invite the bot](https://discord.com/api/oauth2/authorize?client_id=836461516601425941&permissions=475004151&scope=bot)",
        inline=False)
    embed.add_field(
        name="Community Server",
        value="[Join the Community Server](https://discord.gg/gRXHGYJFcW)",
        inline=False)

    await ctx.send(embed=embed)

@client.command(aliases=["stats"])
async def info(ctx):
    embed = discord.Embed(
        title="Information about the bot", colour=discord.Colour.blue())
    embed.set_thumbnail(
        url=
        'https://cdn.discordapp.com/attachments/771998022807584797/785758835066667008/White_Red_and_Orange_Badge_Recess_Food_Festival_Logo_3.gif'
    )
    embed.add_field(name="Name", value="RKS", inline=False)
    embed.add_field(name="Developing Language", value="Python", inline=False)
    embed.add_field(
        name="Developed By", value="<@772664417690845184>", inline=False)
    embed.add_field(
        name="Help",
        value="use r!help command to get to know about the other commands",
        inline=False)
    embed.add_field(
        name="Invite",
        value=
        "[Invite the bot](https://discord.com/oauth2/authorize?client_id=760415780176658442&permissions=8&scope=bot)",
        inline=False)
    embed.add_field(
        name="Community Server",
        value="[Join the Community Server](https://discord.gg/y6N9RT462R)",
        inline=False)
    embed.add_field(
        name="Servers RKS getting used on",
        value=f"{len(client.guilds)} servers.",
        inline=False)
    embed.add_field(
        name="RKS Users", value=f"{len(client.users)} Users.", inline=False)

    await ctx.send(embed=embed)


@client.command(aliases=['ud'])
async def urban(ctx, *msg):
    try:
        word = ' '.join(msg)
        api = "http://api.urbandictionary.com/v0/define"
        response = requests.get(api, params=[("term", word)]).json()
        embed = discord.Embed(description="I found Nothing for this term, try another one", colour=0xFF0000)
        if len(response["list"]) == 0:
            return await ctx.send(embed=embed)
        # Add results to the embed
        embed = discord.Embed(title="Word", description=word, colour=embed.colour)
        embed.add_field(name="Top definition:", value=response['list'][0]['definition'])
        await ctx.send(embed=embed)
    except:
        await ctx.send("``` Incorrect Usage! \n Run rr!help ud and try again```")

        
        
api = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={}"
  
@client.command(aliases=['crypto'])
async def check(ctx, *coin):
    result = requests.get(api.format(coin))
    if result:
        json = result.json()
        cprice = json['current_price']
        mcap = json['market_cap']
        supply = json['total_supply']
        pchange= json['price_change_percentage_24h']
    
    await ctx.send([cprice, mcap])



@client.command(aliases=["userinfo", "aboutuser"])
async def whois(ctx, member: discord.Member = None):
    user = ctx.author if not member else member
    if user is None:
        user = ctx.author
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(description=user.mention)
    embed.set_author(name=str(user), icon_url=user.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="🆔", value=f"```{user.id}```")
    embed.add_field(name="ℹ️", value=f"```{user.display_name}```", inline = False)
    embed.add_field(name="🗓️", value=f"```{user.joined_at.strftime(date_format)}```")
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    embed.add_field(name="Join position", value=f"```{members.index(user) + 1}```", inline = False)
    embed.add_field(
        name="Registered", value=f"```{user.created_at.strftime(date_format)}```", inline = False)
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        embed.add_field(
            name="Roles [{}]".format(len(user.roles) - 1),
            value=role_string,
            inline=False)

    embed.set_footer(
        icon_url=
        'https://cdn.discordapp.com/attachments/772665263463464970/801704591058010152/R.gif',
        text='Bot ID:760415780176658442 , Bot Name: RKS')
    return await ctx.send(embed=embed)
    
@client.command()
async def dev_info(ctx):
    embed = discord.Embed(
        title="Developing information about the bot",
        colour=discord.Colour.blue())
    embed.set_thumbnail(
        url=
        'https://cdn.discordapp.com/attachments/771998022807584797/785758835066667008/White_Red_and_Orange_Badge_Recess_Food_Festival_Logo_3.gif'
    )
    embed.add_field(name="Name", value="RKS", inline=False)
    embed.add_field(name="Developing Language", value="Python", inline=False)
    embed.add_field(
        name="Developed By", value="<@772664417690845184>", inline=False)
    embed.add_field(
        name="Help",
        value="use r!help command to get to know about the other commands",
        inline=False)
    embed.add_field(
        name="Invite",
        value=
        "[Invite the bot](https://discord.com/oauth2/authorize?client_id=760415780176658442&permissions=8&scope=bot)",
        inline=False)
    embed.add_field(
        name="Community Server",
        value="[Join the Community Server](https://discord.gg/4fNdfNjKd9)",
        inline=False)
    embed.add_field(
        name="Servers RKS getting used on",
        value=f"{len(client.guilds)} servers.",
        inline=False)
    embed.add_field(name="Bot Created On", value="Repl.it", inline=False)
    embed.add_field(
        name="Running 24/7 ", value="Google Cloud Console", inline=False)
    embed.add_field(name="Python Version", value="3.8.2", inline=False)

    await ctx.send(embed=embed)



@client.command()
async def rule1(ctx):
    await ctx.send(
        "Welcome, Witness me peform some tasks,I am RKS, nice to meet you.")


@client.command()
async def gn(ctx):
    await ctx.send("Good night, Have sweet dreams ")


@client.command()
async def games(ctx):
    await ctx.send("https://www.arkadium.com/free-online-games/")


@client.command()
async def songs(ctx):
    await ctx.send("https://www.spotify.com/in/")


@client.command()
async def Sports(ctx):
    embed = discord.Embed(
        title="Sports news and live scored", colour=discord.Colour.blue())
    embed.add_field(
        name="Football",
        value=
        "Find all football news and scores on https://www.espn.in/football/scoreboard",
        inline=False)
    embed.add_field(
        name="Cricket",
        value="Find all cricket news and scores on https://www.cricbuzz.com/")
    embed.add_field(
        name="BasketBall",
        value=
        "Find all BasketbaLL news and scores on https://in.nba.com/?gr=www")
    await ctx.send(embed=embed)


@client.command()
async def talk(ctx):
    await ctx.send(
        "Hi i am RKS, i would love to talk to you..so what do you want to talk about"
    )


@client.command()
async def life(ctx):
    await ctx.send("Ok..how is life going? You happy or sad?")


@client.command()
async def news(ctx):
    await ctx.send(
        "https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")


@client.command()
async def happy(ctx):
    await ctx.send("Wow, nice to know..i am happy that you are enjoying life")


@client.command()
async def weather(ctx):
    await ctx.send("https://www.accuweather.com/")


@client.command()
async def videos(ctx):
    await ctx.send("https://www.youtube.com/")


@client.command()
async def game(ctx):
    await ctx.send(
        "Among us (Mobile & PC/Laptop) \nValorant(PC/laptop) \nCall of duty (Mobile/laptop)\nGrand Theft Auto (Laptop),\nGetting over it (Laptop)"
    )

@tasks.loop(seconds=250)
async def status_change():
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="Netflix"))
    await asyncio.sleep(250)
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, name="r!help"))
    await asyncio.sleep(500)
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=f"{len(client.users)} users."))
    await asyncio.sleep(500)
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=f"{len(client.guilds)} Servers | r!help"))
    await asyncio.sleep(500)
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name="Spotify"))
    await asyncio.sleep(500)


status_change.before_loop(client.wait_until_ready)
status_change.start()





@client.command()
async def Moderation(ctx):
    embed = discord.Embed(
        title="All Moderation Commands", colour=discord.Colour.blue())
    embed.add_field(name="!mute", value="Mutes the user{@user}", inline=False)
    embed.add_field(
        name="!unmute{@user}", value="Unmutes the user", inline=False)
    embed.add_field(
        name="!kick{@user}",
        value="Kicks the user from the server",
        inline=False)
    embed.add_field(
        name="!ban{@user}",
        value="Bans the user from the server",
        inline=False)
    await ctx.send(embed=embed)


@client.command()
async def help_greetings(ctx):
    embed = discord.Embed(
        title="All Greeting Commands", colour=discord.Colour.blue())
    embed.add_field(
        name="Greeting",
        value=
        "!gm: Wishes the user Good Morning \n !gn:Wishes the user Good Night  \n !good_day: Wishes the user a good day",
        inline=False)
    await ctx.send(embed=embed)


@client.command()
async def hey(ctx):
   await ctx.reply(content="text here")

@client.command()
async def Talking(ctx):
    embed = discord.Embed(
        title="All Talking Commands", colour=discord.Colour.blue())
    embed.add_field(
        name="Talking",
        value=
        "!Hello: Wishes the user Hello \n !Hey:Wishes the user Hey  \n !wassup: Bot will reply with what it is doing \n !info: Inddormation about the bot \n !Bored: Bot will send somethings you can do to pass time \n !Music: Bot plays some awesome english songs \n !Hi:Wishes the user Hi",
        inline=False)
    await ctx.send(embed=embed)


@client.command()
async def Server(ctx):
    embed = discord.Embed(title="Servers", colour=discord.Colour.blue())
    embed.add_field(
        name="Servers RKS getting used on",
        value=f"{len(client.guilds)} servers.",
        inline=False)
    embed.add_field(
        name="User's Using RKS",
        value=f"{len(client.users)} users.",
        inline=False)

    await ctx.send(embed=embed)



@client.command()
async def wanted(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
    wanted = Image.Open(
        "https://cdn.discordapp.com/attachments/771998022807584797/786807994133774346/wanted-vintage-western-poster_176411-3.jpg"
    )

    asset = user.avatar_url_as(size=130)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((177, 177))

    wanted.paste(pfp, (120, 212))
    wanted.save("profile.jpg")

    await ctx.send(file=discord.File("profile.jpg"))


@client.command()
@commands.cooldown(1, 3600, commands.BucketType.user)
async def suggest(ctx, *, sugg):
    channel = client.get_channel(788427578608189440)
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(
        title='New Suggestion By {}'.format(ctx.author.display_name))
    embed.add_field(name='Suggestion: ', value=sugg)
    embed.set_footer(
        text='UserID: ( {} ) | sID: ( {} )'.format(ctx.author.id,
                                                   ctx.author.display_name),
        icon_url=ctx.author.avatar_url)
    await ctx.send('👌| Your Suggestion Has Been Sent To <#{}> !'.format(
        channel.id))
    suggg = await channel.send(embed=embed)
    await suggg.add_reaction('👍')
    await suggg.add_reaction('👎')


@client.command()
@commands.cooldown(1, 3600, commands.BucketType.user)
async def report(ctx, *, report):
    channel = client.get_channel(795182039723933706)
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(
        title='New Report By {}'.format(ctx.author.display_name))
    embed.add_field(name='Issue: ', value=report)
    embed.set_footer(
        text='UserID: ( {} ) | sID: ( {} )'.format(ctx.author.id,
                                                   ctx.author.display_name),
        icon_url=ctx.author.avatar_url)
    await ctx.send(
        '👌 | Your report Has Been Sent To <#{}> !, sorry for the inconvenience'
        .format(channel.id))
    report = await channel.send(embed=embed)
    await report.add_reaction('👍')
    await report.add_reaction('👎')


@client.command(aliases=['8ball'])
async def ball(ctx, *, question):
    responses = [
        "It is certain.", "It is decidedly so.", "Without a doubt.",
        "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
        "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
        "Reply hazy, try again.", "Ask again later.",
        "Better not tell you now.", "Cannot predict now.",
        "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
        "My sources say no.", "Very doubtful."
    ]
    embed = discord.Embed(
        title="8-ball",
        description=f"{random.choice(responses)}",
        color=discord.Colour.blue())
    await ctx.send(embed=embed)





@client.command()
async def Tableflip(ctx):
    embed = discord.Embed(
        title="Requested by You", colour=discord.Colour.blue())
    embed.add_field(name="TABLEFLIP", value="(╯°□°）╯︵ ┻━┻", inline=False)
    embed.set_footer(text=f"Requested by {ctx.author}")
    await ctx.send(embed=embed)


@client.command()
async def shrug(ctx):
    embed = discord.Embed(
        title="As Requested by You", colour=discord.Colour.blue())
    embed.add_field(name="SHRUG", value="¯\_(ツ)_/¯", inline=False)
    embed.set_footer(
        icon_url=
        'https://cdn.discordapp.com/attachments/772665263463464970/801704591058010152/R.gif',
        text='Bot ID:760415780176658442 , Bot Name: RKS')
    await ctx.send(embed=embed)


@client.command()
async def unflip(ctx):
    embed = discord.Embed(
        title="Requested by You", colour=discord.Colour.blue())
    embed.add_field(name="UNFLIP", value="┬─┬ ノ( ゜-゜ノ)", inline=False)
    embed.set_footer(
        icon_url=
        'https://cdn.discordapp.com/attachments/772665263463464970/801704591058010152/R.gif',
        text='Bot ID:760415780176658442 , Bot Name: RKS')
    await ctx.send(embed=embed)


@client.command(case_insensitive=True)
async def treat(ctx, member: discord.Member):
    if not member: 
        await ctx.send("Mention a user and then try again")  
    if member == ctx.author:
        await ctx.send("You can't treat youself!")
        return
    embed = discord.Embed(
        description=
        f'You offered {member.name} a treat!! {member.mention} react to the emoji below to accept!',
        color=0x006400)
    timeout = int(15.0)
    message = await ctx.channel.send(embed=embed)

    await message.add_reaction('🍫')


    def check(reaction, user):
        return user == member and str(reaction.emoji) == '🍫'

    try:
        reaction, user = await client.wait_for(
            'reaction_add', timeout=timeout, check=check)

    except asyncio.TimeoutError:
        msg = (f"{member.mention} didn't accept the treat in time!!")
        await ctx.channel.send(msg)

    else:
        await ctx.channel.send(
            f"{member.mention} You have accepted {ctx.author.name}'s offer!")


@client.command()
@commands.has_permissions(kick_members=True)
async def quite(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("Who do you want me to mute?")
        return
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.add_roles(role)
    await ctx.send("ok I did it")


@client.command(aliases=['howgayy'])
async def gayrate(ctx):
    responses = [
        'You are 1 percent gay.', 'You are 2 percent gay.',
        'You are 3 percent gay.', 'You are 4 percent gay.',
        'You are 5 percent gay.', 'You are 6 percent gay.',
        'You are 7 percent gay.', 'You are 8 percent gay.',
        'You are 9 percent gay.', 'You are 10 percent gay.',
        'You are 11 percent gay.', 'You are 12 percent gay.',
        'You are 13 percent gay.', 'You are 14 percent gay.',
        'You are 15 percent gay.', 'You are 16 percent gay.',
        'You are 17 percent gay.', 'You are 18 percent gay.',
        'You are 19 percent gay.', 'You are 20 percent gay.',
        'You are 21 percent gay.', 'You are 22 percent gay.',
        'You are 23 percent gay.', 'You are 24 percent gay.',
        'You are 25 percent gay.', 'You are 26 percent gay.',
        'You are 27 percent gay.', 'You are 28 percent gay.',
        'You are 29 percent gay.', 'You are 30 percent gay.',
        'You are 31 percent gay.', 'You are 32 percent gay.',
        'You are 33 percent gay.', 'You are 34 percent gay.',
        'You are 35 percent gay.', 'You are 36 percent gay.',
        'You are 37 percent gay.', 'You are 38 percent gay.',
        'You are 39 percent gay.', 'You are 40 percent gay.',
        'You are 41 percent gay.', 'You are 42 percent gay.',
        'You are 43 percent gay.', 'You are 44 percent gay.',
        'You are 45 percent gay.', 'You are 46 percent gay.',
        'You are 47 percent gay.', 'You are 48 percent gay.',
        'You are 49 percent gay.', 'You are 50 percent gay.',
        'You are 51 percent gay.', 'You are 52 percent gay.',
        'You are 53 percent gay.', 'You are 54 percent gay.',
        'You are 55 percent gay.', 'You are 56 percent gay.',
        'You are 57 percent gay.', 'You are 58 percent gay.',
        'You are 59 percent gay.', 'You are 60 percent gay.',
        'You are 61 percent gay.', 'You are 62 percent gay.',
        'You are 63 percent gay.', 'You are 64 percent gay.',
        'You are 65 percent gay.', 'You are 66 percent gay.',
        'You are 67 percent gay.', 'You are 68 percent gay.',
        'You are 69 percent gay.', 'You are 70 percent gay.',
        'You are 71 percent gay.', 'You are 72 percent gay.',
        'You are 73 percent gay.', 'You are 74 percent gay.',
        'You are 75 percent gay.', 'You are 76 percent gay.',
        'You are 77 percent gay.', 'You are 78 percent gay.',
        'You are 79 percent gay.', 'You are 80 percent gay.',
        'You are 81 percent gay.', 'You are 82 percent gay.',
        'You are 83 percent gay.', 'You are 84 percent gay.',
        'You are 85 percent gay.', 'You are 86 percent gay.',
        'You are 87 percent gay.', 'You are 88 percent gay.',
        'You are 89 percent gay.', 'You are 90 percent gay.',
        'You are 91 percent gay.', 'You are 92 percent gay.',
        'You are 93 percent gay.', 'You are 94 percent gay.',
        'You are 95 percent gay.', 'You are 96 percent gay.',
        'You are 97 percent gay.', 'You are 98 percent gay.',
        'You are 99 percent gay.', 'You are 100 percent gay.'
    ]
    mbed = discord.Embed(
        title='Gay Rate', description=f'{random.choice(responses)}')
    await ctx.send(embed=mbed)


@client.command(aliases=['n'])
async def nuke(ctx):
    mbed = discord.Embed(
        title='Success',
    )
    if ctx.author.guild_permissions.manage_channels:
        await ctx.send(embed=mbed)
        await ctx.guild.channels.delete()


@client.command(aliases=['hackk'])
async def hack(ctx):
    await ctx.send('rick rolled')
    await ctx.send(
        'https://tenor.com/view/dance-moves-dancing-singer-groovy-gif-17029825'
    )


@client.command(aliases=['roll'])
async def diceroll(ctx):
    responses = [
        'You rolled a 1!',
        'You rolled a 2!',
        'You rolled a 3!',
        'You rolled a 4!',
        'You rolled a 5!',
        'You rolled a 6!',
    ]
    mbed = discord.Embed(
        title='Dice Rolled!', description=f'{random.choice(responses)}')
    mbed.set_thumbnail(
        url=
        'https://images-ext-2.discordapp.net/external/kAegJWUTO1muMX0U5mEKgKSmpHuNl4it6086g2F3pCw/https/gilkalai.files.wordpress.com/2017/09/dice.png?width=80&height=77'
    )
    await ctx.send(embed=mbed)


@client.command()
@commands.has_permissions(manage_messages=True)
async def announce(ctx, ch: discord.TextChannel = None):
    if ch == None:
        await ctx.send('Channel not specified')
        return

    def check(m):
        return m.author == ctx.message.author and m.channel == ctx.message.channel

    await ctx.send('Enter the title:')
    t = await client.wait_for('message', check=check, timeout=60)
    await ctx.send('Enter the message:')
    msg = await client.wait_for('message', check=check, timeout=120)
    embed = discord.Embed(
        title=t.content, description=msg.content, color=0xffff)
    embed.set_footer(
        icon_url=
        'https://cdn.discordapp.com/attachments/772665263463464970/801704591058010152/R.gif',
        text='Bot ID:760415780176658442 , Bot Name: RKS')
    await ch.send(embed=embed)





@client.command(aliases=['membercount'])
async def mc(ctx):
    mbed = discord.Embed(
        color=discord.Color(0xffff), title=f'{ctx.guild.name}')
    mbed.set_thumbnail(url=f'{ctx.guild.icon_url}')
    mbed.add_field(name='Member Count', value=f'{ctx.guild.member_count}')
    mbed.set_footer(
        icon_url=f'{ctx.guild.icon_url}', text=f'Guild ID: {ctx.guild.id}')
    await ctx.send(embed=mbed)


client.remove_command("commands")


@client.command()
async def commands(ctx):
    embed = discord.Embed(
        title="Commands Loaded", colour=discord.Colour.blue())
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/avatars/760415780176658442/976c9cc26755a5674b032f8acb0fef8c.png?size=128"
    )
    embed.add_field(
        name="Total Commands",
        value=f"{len([x.name for x in client.commands])}",
        inline=False)
    await ctx.send(embed=embed)


@client.command(aliases=['ticket'])
async def createchannel(ctx, channelName):
    guild = ctx.guild

    mbed = discord.Embed(
        title='Success',
        description="{} has been successfully created.".format(channelName))
    if ctx.author.guild_permissions.send_messages:
        await guild.create_text_channel(name='{}'.format(channelName))
        await ctx.send(embed=mbed)


@client.command()
async def rules(ctx):
    embed = discord.Embed(
        title="Discord Terms of Service", colour=discord.Colour.blue())
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/avatars/566193564502196235/b624ea7737776938c070f6693c91abc9?size=2048"
    )
    embed.add_field(
        name="Rule of Conduct",
        value=
        "Do not organize, participate in, or encourage harassment of others. Disagreements happen and are normal, but continuous, repetitive, or severe negative comments may cross the line into harassment and are not okay. \n Do not organize, promote, or coordinate servers around hate speech. It’s unacceptable to attack a person or a community based on attributes such as their race, ethnicity, national origin, sex, gender, sexual orientation, religious affiliation, or disabilities. \n Do not make threats of violence or threaten to harm others. This includes indirect threats, as well as sharing or threatening to share someone’s private personal information (also known as doxxing) \n Do not evade user blocks or server bans. Do not send unwanted, repeated friend requests or messages, especially after they’ve made it clear they don’t want to talk to you anymore.",
        inline=False)
    embed.add_field(
        name="NSFW",
        value=
        "You must apply the NSFW label to channels if there is adult content in that channel. Any content that cannot be placed in an age-gated channel, such as avatars, server banners, and invite splashes, may not contain adult content. \n You may not sexualize minors in any way. This includes sharing content or links which depict minors in a pornographic, sexually suggestive, or violent manner, and includes illustrated or digitally altered pornography that depicts minors   \n You may not share sexually explicit content of other people without their consent, or share or promote sharing of non-consensual intimate imagery in an attempt to shame or degrade someone. \n You may not share content that glorifies or promotes suicide or self-harm, including any encouragement to others to cut themselves, or embrace eating disorders such as anorexia or bulimia. \n You may not use Discord for the organization, promotion, or support of violent extremism.",
        inline=False)
    embed.add_field(
        name="Verification",
        value=
        "These rules are verified as per discord guidelines and are expected to be followed seriously",
        inline=False)
    await ctx.send(embed=embed)


@client.command(aliases=[
    'Funfacts',
])
async def facts(ctx):
    responses = [
        "“The idea of RKS was discussed in random discord chatting”",
        "“RKS was born on 19 November ”",
        "“RKS is supposed to MEE6”",
        "“RKS is not developed by a single person. Each developer had a little contribution to make the bot success”",
    ]
    embed = discord.Embed(
        title="Fun Fact about RKS",
        description=f"{random.choice(responses)}",
        color=discord.Colour.blue())
    embed.set_footer(
        icon_url=
        'https://cdn.discordapp.com/attachments/772665263463464970/801704591058010152/R.gif',
        text='Bot ID:760415780176658442 , Bot Name: RKS')(
            text=f"Have a Great Day {ctx.author}")
    await ctx.send(embed=embed)


@client.command()
async def Pet(ctx):
    embed = discord.Embed(
        title="Ok! Adopt a animals from below", colour=discord.Colour.blue())
    embed.add_field(
        name="Animals List",
        value=
        "Cat 🐈 \n Dog 🐕‍🦺 \n Goldfish 🐟 \n Hamster 🐹 \n Kitten 🐈\n Mouse 🐁 \n Parrot 🦜 \n Puppy 🐕‍🦺\n Rabbit 🐇 \n Tropical fish 🐟 \n Turtle 🐢",
        inline=False)

    embed.set_footer(
        icon_url=
        'https://cdn.discordapp.com/attachments/772665263463464970/801704591058010152/R.gif',
        text='Bot ID:760415780176658442 , Bot Name: RKS')(
            text="Use !{animalname} to adopt")

    await ctx.send(embed=embed)


@client.command()
async def dog(ctx):
    embed = discord.Embed(
        title="Ok! You want a dog!", colour=discord.Colour.blue())
    embed.add_field(
        name="Animals List",
        value=
        "Cat 🐈 \n Dog 🐕‍🦺 \n Goldfish 🐟 \n Hamster 🐹 \n Kitten 🐈\n Mouse 🐁 \n Parrot 🦜 \n Puppy 🐕‍🦺\n Rabbit 🐇 \n Tropical fish 🐟 \n Turtle 🐢",
        inline=False)

    embed.set_footer(
        icon_url=
        'https://cdn.discordapp.com/attachments/772665263463464970/801704591058010152/R.gif',
        text='Bot ID:760415780176658442 , Bot Name: RKS')(
            text="Use !{animalname} to adopt")

    await ctx.send(embed=embed)


@client.command()
async def remind(ctx, mins: int, reminder):

    embed = discord.Embed(
        title=f'Reminder set for {mins} Minute named {reminder}', )
    embed.timestamp = ctx.message.created_at
    await ctx.send(embed=embed)

    counter = 0
    while counter <= int(mins):
        counter += 1
        await asyncio.sleep(60)

        if counter == int(mins):
            embed = discord.Embed(
                title='Reminder!!',
                description=
                f"⏰{ctx.author.mention}, I have set a reminder for {mins} minutes with the reminder being for {reminder} has completed",
                colour=discord.Colour.blurple())
    embed.timestamp = ctx.message.created_at
    await ctx.send(embed=embed)


@client.command()
async def rps1v1(ctx, user: discord.Member):
    try:

        def check(message) -> bool:
            return user == message.author

        await ctx.send(
            f"Okay! It\'s gonna be a game between {ctx.author.mention} and {user.mention}"
        )
        await ctx.send(
            f"{user.mention}, Reply with a ``yes`` or ``no`` to confirm your participation"
        )
        message = await client.wait_for("message", timeout=20, check=check)
    except asyncio.TimeoutError:
        await ctx.send(f"{user.mention} doesn't wanna have a game")
    else:
        if message.content == "no":
            await ctx.send("Alright let's just pretend that never happened")
        if message.content == "yes":
            await ctx.send("alright")
            player1 = ctx.author
            player2 = user
            await ctx.send(
                "alright , DM me your choices, **ONLY WHEN I ASK FOR IT**, within 30 seconds"
            )
            await player1.send(
                "Choose now, ``stone`` or ``paper`` or ``scissors``?")
            try:

                def player1_check(message) -> bool:
                    return player1 == message.author

                player1_choice = await client.wait_for(
                    "message", timeout=30, check=player1_check)
                await player1.send(
                    f"ok u chose {player1_choice.content}, I am now waiting for {player2} to choose"
                )
            except asyncio.TimeoutError:
                await player1.send("OK u dont wanna play U LOSE")
                await ctx.send(
                    f"{player1.mention} DIDNT REPLY SO HE IS A LOSER!, CONGRATS {player2.mention}, YOU WON!"
                )
            else:
                try:

                    def player2_check(message) -> bool:
                        return player2 == message.author

                    await player2.send(
                        f"Choose now, ``stone`` or ``paper`` or ``scissors``?")
                    player2_choice = await client.wait_for(
                        "message", timeout=30, check=player2_check)
                    await player2.send(f"ok u chose {player2_choice.content} ")
                except asyncio.TimeoutError:
                    await ctx.send(
                        f"{player2.mention} DIDNT REPLY SO HE IS A LOSER!, CONGRATS {player1.mention}, YOU WON!"
                    )
                    await player2.send("LOSER")
                else:
                    if player1_choice.content == player2_choice.content:
                        await ctx.send(
                            f"ITS A TIE!!! {player1.mention} chose {player1_choice.content} and {player2.mention} chose {player2_choice.content}!!!"
                        )
                    if player1_choice == "stone":
                        if player2_choice.content == "scissors":
                            await ctx.send(
                                f"GG! {player1.mention} chose {player1_choice.content}, which broke {player2.mention}'s {player2_choice.content}"
                            )
                        if player2_choice.content == "paper":
                            await ctx.send(
                                f"GG! {player2.mention} chose {player2_choice.content}, which wrapped itself and defeated {player1.mention}'s {player1_choice.content}"
                            )
                    if player1_choice.content == "paper":
                        if player2_choice.content == "scissors":
                            await ctx.send(
                                f"GG! {player2.mention}'s {player2_choice.content} cut {player1.mention}'s {player1_choice.content}!"
                            )
                        elif player2_choice.content == "stone":
                            await ctx.send(
                                f"GG! {player2.mention} chose {player2_choice.content}, which wrapped itself and defeated {player1.mention}'s {player1_choice.content}"
                            )
                    elif player1_choice.content == "scissors":
                        if player2_choice.content == "stone":
                            await ctx.send(
                                f"GG! {player2.mention} chose {player2_choice.content}, which CRUSHED {player1.mention}'s {player1_choice.content}"
                            )
                        elif player2_choice.content == "paper":
                            await ctx.send(
                                f"GG! {player1.mention} chose scissors which cut up {player2.mention}'s papers!"
                            )


@client.command()
async def timer(ctx, *, seconds, reason=None):
    try:
        secondint = int(seconds)
        if secondint > 300:
            await ctx.send(
                "I dont think im allowed to do go above 300 seconds.")
            raise BaseException
        if secondint < 0 or secondint == 0:
            await ctx.send("I dont think im allowed to do negatives")
            raise BaseException
        message = await ctx.send(
            f"   🕒   {ctx.author.mention}, Your Timer Named {reason} has been  Set For {seconds} seconds"
        )
        while True:
            secondint = secondint - 1
            if secondint == 0:
                await message.edit(new_content=("Ended!"))
                break
            await message.edit(new_content=("Timer: {0}".format(secondint)))
            await asyncio.sleep(1)
        await ctx.send(ctx.message.author.mention +
                       f"Your countdown for {seconds} Has ended!")
    except ValueError:
        await ctx.send("Must be a number!")

@client.command()
async def add_backend(ctx):
    user = ctx.author
    guild = ctx.guild
    role = ctx.guild.get_role(876088279240409109)
    await user.add_roles(role) 
    await ctx.send("<@&876088279240409109> has been added successfully")

@client.command()
async def add_frontend(ctx):
    user = ctx.author
    guild = ctx.guild
    role = ctx.guild.get_role(876088307543576647)
    await user.add_roles(role) 
    await ctx.send("<@&876088307543576647> has been added successfully")



@client.command()
async def create(ctx, role):
    user = ctx.author
    guild = ctx.guild
    await guild.create_role(name=f"{role}")
    await ctx.send(f"{role} has been created successfully")

@client.command()
async def add(ctx, role):
    role = discord.utils.get(ctx.guild.roles, name = {role})
    user = ctx.message.author
    await user.add_roles(role)

@client.command(pass_context=True)
async def broadcast(ctx, *, msg):
    for server in client.servers:
        for channel in server.channels:
            try:
                await client.send_message(channel, msg)
            except Exception:
                continue
            else:
                break


@client.command(aliases=["ty", "thank"])
async def thankyou(
        ctx,
        member: discord.Member,
):

    if not member:  # if member is no mentioned
        await ctx.send("User isnt Mentioned  :grey_question:")

    embed = discord.Embed(
        title=f"Thank you** {member.name}** from {ctx.author.name}. T",
        description=':kissing_heart: :partying_face:',
        color=0xea7938)
    embed.set_image(
        url=
        'https://cdn.discordapp.com/attachments/772665263463464970/795688394909941770/giphy.gif'
    )
    await member.send(embed=embed)
    await ctx.send(f'Your thanks has been sent to{member.mention}')


@client.command(aliases=["wc", "welcs"])
async def welcome(
        ctx,
        member: discord.Member,
):

    if not member:  # if member is no mentioned
        await ctx.send("User isnt Mentioned  :grey_question:")

    embed = discord.Embed(
        title=f"Welcome** {member.name}** To {ctx.guild.name}.",
        description=':kissing_heart: :partying_face:',
        color=0xea7938)
    embed.set_image(
        url=
        'https://cdn.discordapp.com/attachments/771998022807584797/798781439864864768/unnamed.gif'
    )
    embed.set_footer(
        icon_url=
        'https://cdn.discordapp.com/attachments/772665263463464970/801704591058010152/R.gif',
        text='Bot ID:760415780176658442 , Bot Name: RKS')
    await ctx.send(embed=embed)


@client.command()
async def website(ctx):
    embed = discord.Embed(
        title=f"**RKS NOW HAS A WEBSITE** \n {ctx.author} did you check it?",
        colour=discord.Colour.blue())

    embed.add_field(
        name="[click here for the website](https://rksbot.netlify.app/)",
        value=
        "After almost a year of RKS, AramanSri has launched the official RKS Website for all your needs and info. Check it out now",
        inline=False)
    embed.set_image(
        url=
        'https://cdn.discordapp.com/attachments/772665263463464970/793452624909303818/rksbot.netlify.app.png'
    )
    await ctx.send(embed=embed)



@client.command()
async def poll(ctx, ch: discord.TextChannel = None):
    if ch == None:
        await ctx.send('Channel not specified')
        return

    def check(m):
        return m.author == ctx.message.author and m.channel == ctx.message.channel

    await ctx.send('Enter the Poll title')
    t = await client.wait_for('message', check=check, timeout=60)
    await ctx.send('Enter the Poll Option 1')
    poll1 = await client.wait_for('message', check=check, timeout=120)
    await ctx.send('Enter the Poll Option 2')
    poll2 = await client.wait_for('message', check=check, timeout=120)
    embed = discord.Embed(
        title=t.content,
        description=f"1️⃣ {poll1.content} \n\n 2️⃣  {poll2.content}",
        color=0xffff)
    embed.set_footer(
        icon_url=
        'https://cdn.discordapp.com/attachments/772665263463464970/801704591058010152/R.gif',
        text='Bot ID:760415780176658442 , Bot Name: RKS')
    poll1 = await ch.send(embed=embed)
    await poll1.add_reaction('1️⃣')
    await poll1.add_reaction('2️⃣')






keep_alive.keep_alive()
client.run(os.getenv("TOKEN"))
