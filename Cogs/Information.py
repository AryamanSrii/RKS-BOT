import discord
from discord.ext import commands


class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
       
    @commands.command()
    async def sinfo(self,ctx):
          name = str(ctx.guild.name)
          description = str(ctx.guild.description)
          guild = ctx.guild
          owner = str(ctx.guild.owner)
          id = str(ctx.guild.id)
          region = str(ctx.guild.region)
          memberCount = str(ctx.guild.member_count)
          icon = str(ctx.guild.icon_url)
          total_text_channels = len(guild.text_channels)
          total_voice_channels = len(guild.voice_channels)
          total_channels = total_text_channels + total_voice_channels
          role_count = len(ctx.guild.roles)
          list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]

          embed2 = discord.Embed(
          timestamp=ctx.message.created_at, color=ctx.author.color)
          embed2.add_field(name='Name', value=f"```{ctx.guild.name}```", inline=True)
          embed2.add_field(name='Owner', value=f"```{ctx.guild.owner}```", inline=True)
          embed2.add_field(
          name='Verification Level',
          value=f"```{ctx.guild.verification_level}```",
          inline=True)
          embed2.add_field(
          name='Highest role', value=f"```{ctx.guild.roles[-2]}```", inline=True)
          embed2.add_field(name="Server ID", value=f"```{id}```", inline=True)
          embed2.add_field(name="Region", value=f"```{region}```", inline=True)
          embed2.add_field(
          name="Text Channels: ", value = f"```{total_channels}```", inline=True)
          embed2.add_field(
          name="Voice Channels: ", value = f"```{total_voice_channels}```", inline=True)

          embed2.add_field(
          name='Number of roles', value=f"```{str(role_count)}```", inline=True)
          embed2.add_field(
          name='Number Of Members', value=f"```{ctx.guild.member_count}```", inline=True)
          embed2.add_field(
          name='Created At:',
          value=f" ```{ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S')}```",
          inline=True)
          embed2.set_thumbnail(url=ctx.guild.icon_url)
          embed2.set_author(name=f"{ctx.guild.name} Information")

          await ctx.send(embed=embed2)


def setup(bot):
    bot.add_cog(Information(bot))