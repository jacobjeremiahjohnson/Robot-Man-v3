from config import*

info = {
  "name" : ">presence [Type] (1=Playing, 2=Watching, 3=Listening, 4=Streaming), [Activity]",
  "desc" : "Open-source presence generation"
}

async def command(ctx):
  t = parseMessage(ctx.content)
  if t.getFromIndex(1) == "random": #If the content is "random", the presence is changed to a random presence from a list
    activityVar = randomPresence()
  elif t.getFromIndex(1) in [1,2,3,4]: #If a type is provided, the type is changed along with the content
    presence = t.getContent(2) #Gets content
    print("gak")
    activityVar = discord.Activity(name = presence, type = randomActivity(int(t.getFromIndex(1))-1)) #Changes presence to the content, the type to the provided type 
  await client.change_presence(activity = activityVar)
  global currentPresenceType
  await ctx.channel.send(content = "", embed = baseEmbed([["🐛 "+ctx.author.name+" changed the presence to 🐛", "`"+currentPresenceType+ " " +activityVar.name+"`"],["...","..."]]))