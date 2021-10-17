import discord
import datetime
from discord.ext import commands
from datetime import datetime
from discord.ext.commands import cooldown, BucketType

time_before = datetime.now()
s1 = time_before.strftime("%H:%M:%S")

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command(aliases=["avatar"])
    async def pfp(self, ctx, member: discord.Member):
        member = ctx.author if not member else member

        embed = discord.Embed(title=f"{member.name}'s avatar")
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)
    
    
    @commands.command(name="uptime")
    async def uptime_(self, ctx):
      FMT = '%H:%M:%S'
      now = datetime.now()
      time_now = now.strftime(FMT)
      uptime = datetime.strptime(time_now, FMT) - datetime.strptime(s1, FMT)
      embed = discord.Embed(colour=0xc8dc6c)
      embed.add_field(name="Uptime", value=uptime)
      await ctx.send(embed=embed)
       
    @commands.command(aliases=['member'])
    @commands.cooldown(1, 10, BucketType.user)
    async def Members(self, ctx):
        counter, counter1, counter2, counter3 = 0, 0, 0, 0
        for member in ctx.guild.members:
            if member.status == discord.Status.offline:     counter +=1
            elif member.status == discord.Status.idle:    counter1 +=1
            elif member.status == discord.Status.do_not_disturb:    counter2 +=1
            elif member.status == discord.Status.online:    counter3 +=1
        embed = discord.Embed(
            title='Members? **({})**'.format(len(ctx.guild.members)),
            color=discord.Color.red(),
            description='**Member Statuses:**\n\n⚫ **Offline: {}\n\n🟢 Online: {}\n\n<:3488_Idle_oxzy:787764233416736808> Idle: {}\n\n 🔴 Do Not disturb: {}**'.format(counter, counter3, counter1, counter2)
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Utility(bot))
