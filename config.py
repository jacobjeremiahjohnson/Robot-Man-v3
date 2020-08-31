#important functions
import os, importlib, discord, random, time, praw, asyncio, urllib.request, tweepy, calendar, json
from googletrans import Translator #For translating
from prawcore import NotFound #Reddit time deluxe *double dab*
from datetime import datetime

async def checkCommand(context, client = None):  
  t = parseMessage(context.content)

  for i in os.listdir("commands"):
    if i == "__pycache__":
      continue
    if i[:-3] in t.getFromIndex(0):
      module = importlib.import_module("commands."+i[:-3])
      await module.command(context, client)

async def dbCREATE(client, name, data = None):
	server = client.get_channel(716786902342172675)
	final = {
		"name" : name
	}
	if data != None:
		final.update(data)
	else:
		await server.send(json.dumps(final))

async def dbGET(client, name):
	server = client.get_channel(716786902342172675)

	serverMessageList = await server.history(limit = 10000).flatten()
	for i in serverMessageList:
		j = i.content
		dickt = json.loads(j)
		if dickt.get("name") == name:
			return dickt
		else:
			continue
	return False

async def dbADD(client, name, data):
	server = client.get_channel(716786902342172675)

	serverMessageList = await server.history(limit = 10000).flatten()
	for i in serverMessageList:
		j = i.content
		dickt = json.loads(j)
		if dickt.get("name") == name:
			print("PRE UPDATE"+str(dickt))
			dickt.update(data)
			print("POST UPDATE"+str(dickt))
			final = json.dumps(dickt)
			await i.edit(content = final)
			return True
		else:
			continue
	return False

def baseEmbed(embedMatrix): #Base embed for embed calls
  global nickList
  embed = discord.Embed(color = discord.Color.blue())
  i=0

  while embedMatrix:
    try:
      embed.add_field(name = embedMatrix[0][i], value = embedMatrix[1][i], inline = False)
    except:
      break
    else:
      i+=1
  return embed

def errorEmbed(error, syntax): #Embed for error messages
  embed = discord.Embed(color = discord.Color.red())
  embed.set_author(name = "❗Official Syntax Police Report❗")
  embed.add_field(name = "You sent:", value = "`"+error+"`")
  embed.add_field(name = "Proper syntax:", value = "`"+syntax+"`")
  embed.set_footer(text = "Brought to you by your local Syntax Police Department")
  return embed

class parseMessage: #Tools for message processing
  def __init__(self, msg): 
    self.msg = msg

  def getFromIndex(self, index = 0): #Gets word from index
    self.index = index
    return self.msg.split()[self.index]

  def getContent(self , index = 1): #Gets entire message starting at index
    separator = " "
    self.index = index
    message = self.msg.split()
    iterations = 0
    while iterations != index:
      del message[0]
      iterations+=1
    return separator.join(message)

playingList = ["with Proletariat Bot", "Twitch Tetris (www.mixedlaughs.tk)", "league pls help", "with matches", "videojeugos"]

watchingList = ["anime", "pirated anime", "twitch.tv/TheColinizer", "HockeySock", "Disney channel original movies", "Death Note: The Netflix Original Movie", "One Piece (again)", "you", "your mom", "twitch.tv/harrisn_t", "you sleep"]

listeningList = ["jazz", "Chill LoFi Hip Hop", "Vaporwave aestethics", "mumble rap", "my mom", "God"]

streamingList = ["on OF", "my hot Valorant gameplay", "league pls help"]

currentPresenceType = None

def randomActivity(activity): #For literally one command, it just makes that part of the code readable in return for this waste of a function
  print(activity)
  activities = [discord.ActivityType.playing, discord.ActivityType.watching, discord.ActivityType.listening, discord.ActivityType.streaming]
  global currentPresenceType
  gak = str(activities[int(activity)])
  g, randomActivity.currentPresenceType = gak.split(".")
  if randomActivity.currentPresenceType == "listening":
    randomActivity.currentPresenceType = "listening to"
  return activities[int(activity)] #Returns a random (or determined) discord.Activity type

def randomPresence():
  global playingList, watchingList, listeningList, streamingList #Pulls lists of the valid presence messages
  gak = random.randint(0,3) #Chooses a random one
  lists = {
    "1" : playingList,
    "2" : watchingList,
    "3" : listeningList,
    "4" : streamingList
  }
  content = random.choice(lists.get(str(gak+1))) #Gets a valid presece message from the chosen list
  trueActivity = discord.Activity(name = content, type = randomActivity(gak)) 
  print(content)
  return trueActivity #Returns a discord.Activity object consisting of the valid type and matching presence

HELP = """**Help!,** I need somebody
**Help!,** not just anybody
**Help!,** you know I need someone, **HEEelp!**
When I was younger, so much younger than todaaaay
I never needed anybody's help! in any way
But now these days are gone, I'm not so self assuuuured
Now I find I've changed my mind and opened up the doors
Help! me if you can, I'm feeling *doooown*
And I do appreciate you being *roooound*
Help! me get my feet back on the *grooound*
Won't you ***PLEEEEeaaaaase, pleeeeeease*** help! me
 
And now my life has changed in oh so many waaaays
My independence seems to vanish in the haze
But every now and then I feel so insecuuuuure
I know that I just need you like I've never done befooore
Help! me if you can, I'm feeling *doooown*
And I do appreciate you being *roooound*
Help! me get my feet back on the *groooound*
Won't you ***PLEEEAAse, pleeeeease*** help! me
 
When I was younger, so much younger than tooodaaaay
I never needed anybody's help in any way
But now these days are gone, I'm not so self  assuuured
Now I find I've changed my mind and opened up the doors
Help! me if you can, I'm feeling *doooown*
And I do appreciate you being *roooound*
Help! me get my feet back on the *grooooound*
Won't you ***PLEEEEEEase, pleeeeease*** help! me, help! me, help! meeeeee, **ooooooooh**"""
