# Libraries
import os
import asyncio
import discord
from discord.ext import commands
from datetime import datetime
import pytz
import requests
from replit import db
# import requests #make http request api


bot = commands.Bot(command_prefix="!")

# client = discord.Client()
my_secret = os.environ['Token']  #secret from a file

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user.name}!')

@bot.command()
async def date(ctx):

  today = datetime.now()  # get time today
  eastern = pytz.timezone('US/Eastern')  # object
  today = today.astimezone(eastern)  # method(object)
  todayString = today.strftime("Date: %B %d %Y \nTime: %I:%M %p")

  await ctx.channel.send(todayString)

@bot.command()
async def meme(ctx):

  url = "https://mem-api.herokuapp.com/gimme"
  json_data = requests.get(url).json()
  link = json_data["postLink"]
  imgUrl = json_data["url"]
  
  await ctx.channel.send(imgUrl)
  await ctx.channel.send(link)


@bot.command()
async def sup(ctx):
  
  await ctx.channel.send(f"Sup {ctx.author.mention}")


@bot.command()
async def picS(ctx, picName, link):
  #save and image
  if ctx.content.startswith('!picS'):
    #!picS [picname] [piclink]
    #check if in db already
    try:
      db[picName]
      await ctx.channel.send("Image already saved!")

    except:
      db[picName] = link
      await ctx.channel.send("Image Saved!")

@bot.command()
async def picG(ctx, picName):
  #getPic
  if ctx.content.startswith('!picG'):
    try:
      await ctx.channel.send(picName)
      await ctx.channel.send(db[picName])
    except:
      await ctx.channel.send("pic does not exist")


# class MyClient(discord.Client):


#     # trigger each time a message is received
#     async def on_message(self, message):
#         print(f'Message from {message.author}: {message.content}')



bot.run(my_secret)  #to run the bot, param is the bot token/password
