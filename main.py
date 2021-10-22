# Libraries
import os
# import asyncio
from discord.ext import commands
import discord
from datetime import datetime
import pytz
import requests
from replit import db



bot = commands.Bot(command_prefix="!")

my_secret = os.environ['Token']  #secret from a file

@bot.event
async def on_ready():
  print(f'Logged on as {bot.user.name}!')

# @bot.event
# async def on_message(message):
#    print(f'Message from {message.author}: {message.content}')


@bot.command()
async def date(ctx):

  today = datetime.now()  # get time today
  eastern = pytz.timezone('US/Eastern')  # object
  today = today.astimezone(eastern)  # method(object)
  todayString = today.strftime("Date: %B %d %Y \nTime: %I:%M %p")

  await ctx.channel.send(todayString)

@bot.command()
async def meme(ctx):
  url = "https://meme-api.herokuapp.com/gimme"
  response = requests.get(url)
  json = response.json()
  link = json["postLink"]
  imgUrl = json["url"]
  
  await ctx.channel.send(imgUrl)
  await ctx.channel.send(link)


@bot.command()
async def sup(ctx):
  await ctx.channel.send(f"Sup {ctx.author.mention}")


@bot.command()
async def createDB(ctx, picName, link):
  #save and image
  try:
    db[picName]
    await ctx.channel.send("Image already saved!")

  except:
    db[picName] = link
    await ctx.channel.send("Image Saved!")

@bot.command()
async def getDB(ctx, picName):
  #getPic

  try:
    await ctx.channel.send(picName)
    await ctx.channel.send(db[picName])
  except:
    await ctx.channel.send("pic does not exist")

@bot.command()
async def remove(ctx, key):

  del db[key]
  list()
  await ctx.channel.send(f"Removed {key}")

@bot.command()
async def list(ctx):
  
  for key in db:
    values = db[key]
    await ctx.channel.send(f"{key}: {values}")


  
bot.run(my_secret)  #to run the bot, param is the bot token/password

