from server import server
import os
from discord.ext import commands
import config

client = commands.Bot(command_prefix = ">")
server()

@client.event
async def on_ready():
  print(client.user)
  activity = config.randomPresence()
  await client.change_presence(activity = activity)

@client.event
async def on_message(ctx):
  if ctx.content.startswith(">"):
    #Now its time to get funky (funky)
    await config.checkCommand(ctx)

@client.event #COMMAND MESSAGES
async def on_command(ctx):
  print("{}:\n{}".format(str(ctx.author), ctx.content))
  
@client.event #Syntax police
async def on_command_error(ctx, error):
  print(error)
  t = config.parseMessage(ctx.message.content)
  if str(error) != 'Command "{}" is not found'.format(t.getFromIndex(0)[1::]):
    global helpDict
    await ctx.send(content = "", embed=config.errorEmbed(ctx.message.content,str((helpDict.get(t.getFromIndex(0)[1::])[1][0]))))

@client.event #Bullying Roger
async def on_member_update(before, after):
  if str(before) == "Proletariat Bot#3382" and str(before.status) == "online" and str(after.status) == "offline":
    channel = client.get_channel(536529708490293248)
    await channel.send("Proletariat Bot went offline lmao")
  
client.run(os.environ.get("botToken"))