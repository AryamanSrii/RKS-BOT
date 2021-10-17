import discord
from discord.ext import commands
from utils.decorators import command, cooldown
import aiohttp
import json
import decimal


class Quote(commands.Cog):
  def __init__(self,client):
    self.client = client

  @command("quote")  
  async def q(self,ctx):
    async with aiohttp.ClientSession() as r:
      async with r.get("https://api.quotable.io/random") as r:
        data = await r.json()

        embed = discord.Embed(title = "Quote for you", description = f'{data["content"]}', colour = discord.Colour.blue()) 
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/831424680728199178/853170079000559616/Untitled_design_1.gif?width=333&height=333')
   
    await ctx.send(embed = embed)


def setup(client):
    client.add_cog(Quote(client))