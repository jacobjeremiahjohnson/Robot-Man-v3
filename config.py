#important functions
import os, importlib, discord, random, time, praw, asyncio, urllib.request, tweepy, calendar
from googletrans import Translator #For translating
from prawcore import NotFound #Reddit time deluxe *double dab*
from datetime import datetime

async def checkCommand(context):  
  for i in os.listdir("commands"):
    if i == "__pycache__":
      continue
    if i[:-3] in context.content:
      module = importlib.import_module("commands."+i[:-3])
      await module.command(context)

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

playingList = ["with Proletariat Bot", "Minecraft: Battle Royale", "clarinet lol", "piano lol", "ZombsRoyale.io", "agar.io","slither.io","diep.io","Protobowl","repl.it","Discord","C#-esqe frameworks", "Kirby's Epic Yarn: Battle Royale", "Wii Sports: Battle Royale","Wii Sports Resort: GOTY Edition", "TwitchTetris", "with Legos","dead","videojuegos","virtualpiano.net","Solitaire","Checkers: Battle Royale"]

watchingList = ["anime", "porn lol", "hentai lol", "pirated anime", "twitch.tv/TheColinizer", "HockeySock", "Disney channel original movies", "Death Note: The Netflix Original Movie", "One Piece (again)", "you", "your mom", "eSports", "you sleep"]

listeningList = ["emo garbage", "jazz", "Chill LoFi Hip Hop", "Vaporwave", "Juicewave", "mumble rap", "my mom", "God"]

streamingList = ["butt stuff","twitch","pirated anime","Discord","Netflix", "Hulu", "live video feed of your bathroom","live video feed of your webcam","Stardew Valley hentai(???)"]

currentPresenceType = None

def randomActivity(activity): #For literally one command, it just makes that part of the code readable in return for this waste of a function
  print(activity)
  activities = [discord.ActivityType.playing, discord.ActivityType.watching, discord.ActivityType.listening, discord.ActivityType.streaming]
  global currentPresenceType
  gak = str(activities[int(activity)])
  g, currentPresenceType = gak.split(".")
  if currentPresenceType == "listening":
    currentPresenceType = "listening to"
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