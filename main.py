from server import server
import os
import discord
from discord.ext import commands
from config import*
import importlib
import tweepy

# TODO

# Change scuffed string splice to .endswith in help command Eh nvm fuck it
# Make tic tac toe + W/L stats

client = commands.Bot(command_prefix = ">" and "B)")
client.remove_command("help") #fuck youuuu
server()
#TWITTER
auth = tweepy.OAuthHandler(
os.environ.get("twittersecret"), os.environ.get("twitterkey"))
auth.set_access_token(os.environ.get("twitteraccesstoken"),os.environ.get("twitteraccesssecret"))
api = tweepy.API(auth)

@client.event
async def on_ready():
  print(client.user)
  activity = randomPresence()
  await client.change_presence(activity = activity)

  #371432894675288074 - Julie
  #325092229825953793 - Jacob
	#352210254219444224 - Kaz

@client.event
async def on_message(ctx):
  if ctx.content.startswith(">") or ctx.content.startswith("B)"):
    #Now its time to get funky (funky)
    await checkCommand(ctx, client = client)
  
  nameDict = {
    "julie" : 413491484403433503,
    "jacob" : 413492455745519618,
    "wong" : 697285429057028126,
    "judas" : 413491799588470784,
    "kaz" : 706639067399454740,
    "ethan" : 706588156086190170,
    "kaleb" : 716503417358516257,
    "<o/" : 541287206925631498,
		"\o>" : 541287206925631498,
		" dab" : 541287206925631498,
		"quack" : 706640821373501443
  }

  names = ["julie","jacob","wong","judas","kaz","ethan","kaleb"," dab", "<o/", "\o>", "quack"]
	#everybody clap your hands (hands)
  try:	
    if ctx.guild.name == "Equality 3":
      for i in names:
      	if i in ctx.content.lower():
        	id = nameDict.get(i)
        	emoji = await ctx.guild.fetch_emoji(id)
        	await ctx.add_reaction(emoji)
  except:
    print("!")

  masterList = []

	#appo - 587741556551843860

  if ctx.content.startswith("B) evaluate") and ctx.channel.id == 587741556551843860:
    messages = await ctx.channel.history(limit=10000).flatten()

    for i in messages:
      if i.content[::-1][1:13] == "pihsnoitaler" and i.content[:11].lower() == "are you the" and i.channel.id == 587741556551843860:
        masterList.append(i.content)
      else:
        continue
    print(masterList)
    file1 = open("concepts.txt", "w")
    file1.write("Concepts:\n\n")	
    for i in masterList:
      file1 = open("concepts.txt", "a")
      file1.write(i+"\n\n")
      file1.close()

    await ctx.channel.send(file = discord.File("concepts.txt"))
    os.remove("concepts.txt")

  if ctx.channel.id == 587741556551843860:
    global api
    api.update_status(ctx.author.name + ": " + ctx.clean_content)

  await client.process_commands(ctx)

#Special commands that can't be stored as separate files

whiteList = ["Jacob!","Roger"]
@client.command()
async def close(ctx):
  if ctx.message.author.name in whiteList:
    await client.logout()
  else:
    await ctx.channel.send("Hey, you can't do that.")

@client.event #COMMAND MESSAGES
async def on_command(ctx):
  print("{}:\n{}".format(str(ctx.message.author), ctx.message.content))

@client.event #Syntax police
async def on_command_error(ctx, error):
  print(error)
  t = parseMessage(ctx.message.content)
  if str(error) != 'Command "{}" is not found'.format(t.getFromIndex(0)[1::]):
    module = importlib.import_module("commands."+t.getFromIndex(0)[1::])
    await ctx.channel.send(content = "", embed=errorEmbed(ctx.message.content, module.info.get("name")))

@client.event #Bullying Roger
async def on_member_update(before, after):
  if str(before) == "Proletariat Bot#3382" and str(before.status) == "online" and str(after.status) == "offline":
    channel = client.get_channel(536529708490293248)
    await channel.send("Proletariat Bot went offline lmao")

client.run(os.environ.get("botToken"))