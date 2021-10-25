from discord.ext import commands
from replit import db
from datetime import datetime
import discord
import pytz

class DatabaseCommands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

    
  # CREATE DB KEY, VALUES
  @commands.command(name='create', aliases=['save', 'add'])
  async def createDB(self, ctx, picName, link):
    try:
      db[picName]
      await ctx.channel.send("Image already saved!")

    except:
      today =  datetime.now()
      eastern = pytz.timezone('US/Eastern')  # object
      today = today.astimezone(eastern)  # method(object)
      todayString = today.strftime("%B %d %Y")

      db[picName] = {
        "date": str(todayString),
        "link": str(link)
      }
      await ctx.channel.send("Image Saved!")

  
  # REQUEST DB
  @commands.command(name='get')
  async def getDB(self, ctx, key):
    try:
      await ctx.channel.send(key)
      await ctx.channel.send(db[key])

    except:
      await ctx.channel.send("pic does not exist")

  # REMOVE DB KEY
  @commands.command(name='delete', aliases=['del', 'rem','remove'])
  async def removeKey(self, ctx, key):

    del db[key]
    await ctx.channel.send(f"Removed {key}")

  # Search DB KEY
  @commands.command(name='find', aliases=['search'])
  async def searchDB(self, ctx, prefix):

    matches = db.prefix(prefix)
  
    await ctx.channel.send(matches)

  # LIST DB
  @commands.command(name='list')
  async def listDB(self, ctx):

    if not db:
      await ctx.channel.send("Nothing in the database")
      return

    embed = discord.Embed(
      title = "Python Database",
      color = discord.Color.red()
    )
    
    
    for key in db:
      print(db[key])
      value='\n'.join([f"{values.capitalize()}: {db[key][values]}" for values in db[key]])
      embed.add_field(name=key.capitalize(), value=value, inline=False)


    await ctx.send(embed=embed)


def setup(bot):
  bot.add_cog(DatabaseCommands(bot))