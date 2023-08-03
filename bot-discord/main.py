import os
import discord 
from discord.ext import commands
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

my_secret = os.environ['DISCORD_TOKEN']

@bot.command()
async def inverse(ctx, message):
  await ctx.send(message[::-1])

keep_alive()
bot.run(my_secret)