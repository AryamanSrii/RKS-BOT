import os
import random
import asyncio

import discord
from discord.ext import commands
from async_timeout import timeout


class Games(commands.Cog):
    """Play various Games"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['rockpaperscissors'])
    async def rps(self, ctx):
        """Play Rock, Paper, Scissors game"""

        def check_win(p, b):
            if p == '🌑':
                return False if b == '📄' else True
            elif p == '📄':
                return False if b == '✂' else True
            else:  # p=='✂'
                return False if b == '🌑' else True

        async with ctx.typing():
            reactions = ['🌑', '📄', '✂']
            game_message = await ctx.send(
                "**Rock Paper Scissors**\nChoose your shape:",
                delete_after=15.0)
            for reaction in reactions:
                await game_message.add_reaction(reaction)
            bot_emoji = random.choice(reactions)

        def check(reaction, user):
            return user != self.bot.user and user == ctx.author and (str(
                reaction.emoji) == '🌑' or '📄' or '✂')

        try:
            reaction, user = await self.bot.wait_for(
                'reaction_add', timeout=10.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send(f"Time's Up! :stopwatch:")
        else:
            await ctx.send(
                f"**:man_in_tuxedo_tone1:\t{reaction.emoji}\n:robot:\t{bot_emoji}**"
            )
            # if conds
            if str(reaction.emoji) == bot_emoji:
                await ctx.send("**It's a Tie :ribbon:**")
            elif check_win(str(reaction.emoji), bot_emoji):

                await ctx.send(
                    "**You win :sparkles:**"
                )
            
            else:
                await ctx.send("**I win :robot:**")

            
def setup(bot):
    bot.add_cog(Games(bot))