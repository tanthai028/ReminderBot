# Libraries
import os
from datetime import datetime, time, timedelta
from discord.ext import commands
import asyncio
import pytz


client = commands.Bot(command_prefix="!", help_command=None)
my_secret = os.environ['Token']  #secret from a file


# On ready
@client.event
async def on_ready():
  print(f"{client.user} is ready")


###########################################################################
""""""""""""""""""
 # REMINDER BOT #
""""""""""""""""""

async def called_once_a_day():  # Loops every day
  channel_id = 902026655231520769 # announcement channel
  await client.wait_until_ready()  # Make sure your guild cache is ready so the channel can be found via get_channel
  channel = client.get_channel(channel_id) # Note: It's more efficient to do bot.get_guild(guild_id).get_channel(channel_id) as there's less looping involved, but just get_channel still works fine
  message = "@everyone Coding in 10 minutes"
  await channel.send(message)

async def background_task():
  hour, minutes, pm, = 8, 50, True
  if pm: add = 12
  else: add = 0


  WHEN = time(hour + add, minutes, 0)  # 3:19 PM
  now = datetime.now()  # get time today
  eastern = pytz.timezone('US/Eastern')  # object
  now = now.astimezone(eastern)  # method(object)

  if now.time() > WHEN:  # Make sure loop doesn't start after {WHEN} as then it will send immediately the first time as negative seconds will make the sleep yield instantly

    tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
    seconds = (tomorrow - now).total_seconds()  # Seconds until tomorrow (midnight)
    await asyncio.sleep(seconds)   # Sleep until tomorrow and then the loop will start 

  while True:
    now = datetime.utcnow() # You can do now() or a specific timezone if that matters, but I'll leave it with utcnow
    target_time = datetime.combine(now.date(), WHEN)  # 8:50 PM today (In UTC)
    seconds_until_target = (target_time - now).total_seconds()
    await asyncio.sleep(seconds_until_target)  # Sleep until we hit the target time
    await called_once_a_day()  # Call the helper function that sends the message
    tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
    seconds = (tomorrow - now).total_seconds()  # Seconds until tomorrow (midnight)
    await asyncio.sleep(seconds)   # Sleep until tomorrow and then the loop will start a new iteration
  
extensions = ['cogs.CommandEvents','cogs.DatabaseCommands','cogs.MiscCommands','cogs.HelpCommands']


if __name__ == '__main__':
  client.loop.create_task(background_task())

  for ext in extensions:
    client.load_extension(ext)

client.run(my_secret)  #to run the bot, param is the bot token/password

