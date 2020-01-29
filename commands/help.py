from config import*

info = {
  "name" : ">help [command]",
  "desc" : "If you really want to know what this thing 'does'"
}

async def command(ctx):
  commandList = []
  t = parseMessage(ctx.content)
  for i in os.listdir("commands"):
    if "pycach" in i:
      continue
    commandList.append(i[:-3])

  try: #Checks if a valid command is given
    command = None
    for i in commandList:
      if i in t.getFromIndex(1):
        command = i
        break
    
    commandFile = importlib.import_module("commands."+command)
    title = ["❓"+ctx.message.author.name+" needs help! ❓", commandFile.info.get("name")]
    field = ["...",commandFile.info.get("desc")]
    await ctx.channel.send(content = "", embed=baseEmbed([title, field]))

  except:
    command = None
    titleList = ["❓"+ctx.author.name+" needs big help! ❓"]
    fieldList = ["..."]
    for i in commandList:
      commandFile = importlib.import_module("commands."+i)
      titleList.append(commandFile.info.get("name"))
      fieldList.append(commandFile.info.get("desc"))
    await ctx.channel.send(content = "", embed=baseEmbed([titleList, fieldList]))