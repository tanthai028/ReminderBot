from discord.ext import commands
import discord
import requests
from datetime import datetime
import pytz

class MiscCommands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="clear", description="Purge messages")
  async def clear_command(self, ctx, amount = 2):
    amount = int(amount)
    await ctx.channel.purge(limit=amount)
    
  # GET MEME
  @commands.command(name="meme", aliases=['reddit','r','m'], description="Get latest memes from reddit")
  async def meme_command(self, ctx, subreddit = "", count = ""):
    # Request json from api
    await ctx.channel.purge(limit=1)

    url = "https://meme-api.herokuapp.com/gimme/" + subreddit + "/" + count
    json = requests.get(url).json()

    # Get data from json
    title_string = json["title"]
    author = json["author"]
    link = json["postLink"]
    imgUrl = json["url"]
    footer = json["subreddit"]

    # print(title_string, title_string.capitalize())

    # Create embed
    embed = discord.Embed(
      title = title_string.capitalize(),
      description = link,
      color = discord.Color.blue()
    )

    # Reddit logo
    thumbnail = "https://external-preview.redd.it/iDdntscPf-nfWKqzHRGFmhVxZm4hZgaKe5oyFws-yzA.png?auto=webp&s=38648ef0dc2c3fce76d5e1d8639234d8da0152b2"

    embed.set_footer(text="Subreddit: " + footer)
    embed.set_image(url=imgUrl)
    embed.set_thumbnail(url=thumbnail)
    embed.set_author(name=author)

    # Send embed
    await ctx.send(embed=embed)

  # SUP
  @commands.command(name='hello',aliases=['hi','sup'])
  async def hello_command(self, ctx):
    await ctx.channel.send(f"Sup {ctx.author.mention}")
  
  @commands.command(name='date')
  async def getDate(self, ctx):

    today = datetime.now()  # get time today
    eastern = pytz.timezone('US/Eastern')  # object
    today = today.astimezone(eastern)  # method(object)
    todayString = today.strftime("%B %d %Y")
    timeString = today.strftime("%I:%M %p")

    embed = discord.Embed(
      title = "Today",
      color = discord.Color.green()
    )

    embed.add_field(name='Date', value=todayString, inline=False)
    embed.add_field(name='Time', value=timeString)

    await ctx.send(embed=embed)
  

def setup(bot):
  
  bot.add_cog(MiscCommands(bot))
  