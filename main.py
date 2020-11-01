from server import server
import os
import discord
from discord.ext import commands
from config import*
import importlib
import tweepy
import time

# TODO

# Make tic tac toe + W/L stats

client = commands.Bot(command_prefix = ">" and "B)")
client.remove_command("help") 
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

@client.event
async def on_message(ctx):
  if ctx.content.startswith(">") or ctx.content.startswith("B)"):
    #Now its time to get funky (funky)
    try:
    	await checkCommand(ctx, client = client)
    except:
      t = parseMessage(ctx.content)
      module = importlib.import_module("commands."+t.getFromIndex(0)[1::])
      await ctx.channel.send(content = "", embed=errorEmbed(ctx.content, module.info.get("name")))
  
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
  if "is" in ctx.content.lower() and "it" in ctx.content.lower() and "christmas" in ctx.content.lower():
    christmas = datetime(2020, 12, 25)
    now = datetime.now()
    difference = christmas - now
    j, k = str(difference).split(",")
    hours, minutes, seconds = k.split(":")
    await ctx.channel.send("There are {j},{hours} hours, {minutes} minutes, and {seconds} seconds until christmas.".format(j = j, hours = hours, minutes = minutes, seconds = seconds))
  if "water" in ctx.content and "wet" in ctx.content and "is" in ctx.content and ctx.author.name != "Robot Man III":

	  await ctx.channel.send("The Merriam-Webster definition of wet is: covered or soaked with a liquid, such as water; not yet dry or firm, such as wet paint; and to be stored or preserved in liquid. Wet seems to be a complex word, and yet this term is thrown around in a lot of improper ways. Mainly is the common misconception is that water is wet. This is simply not true. If we take an in depth look at what water truly is in relation to the adjective of wetness. Namely, how this adjective cannot apply to water in any of its definitions. \n\n The most common definition of wet is to be covered or soaked with a liquid, most commonly water. To keep things simple, we will assume this definition is restricted to just water. If this does not satisfy the reader, an analysis of liquids that can make water considered wet will be made. At the moment, we are assuming this only applies to water. For something to be covered with a water, that means there has to be some sort of discernable difference between the water and what it is covering. This is not the case if you are covering water with water. Even if the different groups have a different salt content, there still will be no guaranteed way to tell the difference between the water, and if this hypothetical experiment were to take place, which group of water will be considered the wet and which is the wetting? This paradox occurs because this definition of water is implying that for something to be wet it must first not be completely made up of the liquid in question, in this case water. Of course, this is all implied, but I think it is safe to assume that without this notion of the material that is being wetted this definition falls apart in a logical paradox.")
	  await ctx.channel.send("\n\n The second definition of wet is to not be dry or firm. This definition is mainly used when referring to a certain set of solids, such as clay or paint. For a material to be wet in this sense assumes that it can exist in two states, one as wet and the other dry, or as firm and soft. This remains true for both clay and paint, respectively, but falls apart once you try to assign this definition to other materials, specifically liquids. For water (liquid water, not ice or water vapor) this rings true. Water can only exist in its liquidized form, with little to no variation other than temperature and soluble content (water is virtually incompressible so pressure is not a factor). It cannot exist in two radically different forms and no radical variation of water exists like in clay or paint. Therefore, water cannot be wet according to this definition or the previous. Only one more is left.\n\n The third and final definition of wet is to be stored or preserved in a liquid (of course, water). I think this is clear, but I know my audience. Water, cannot be preserved. In no way does water spoil. Water does not possess any attributes that can spoil, like meat or milk. Another problem that arises is similar to the logical paradox addressed in paragraph two. To preserve something with the same material as the thing you are preserving is a waste. In no way can water help to preserve water, even if water could be preserved. I feel like this definition is the most obvious to disprove, but again, I know my audience. \n\n In conclusion, water cannot be wet. Under no definition can water be considered wet, all possibilities against this truth are addressed. I hope that these arguments are thoroughly considered and that I have convinced you to finally accept that water is not, cannot, in no way wet. Ever. Under no definition of wet nor in the hypothetical sense can water be wet.")

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

@client.event #Bullying Roger
async def on_member_update(before, after):
  if str(before) == "Proletariat Bot#3382" and str(before.status) == "online" and str(after.status) == "offline":
    channel = client.get_channel(536529708490293248)
    await channel.send("Proletariat Bot went offline lmao")

client.run(os.environ.get("botToken"))