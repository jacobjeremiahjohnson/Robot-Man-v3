from config import parseMessage, baseEmbed, HELP
import os, importlib, asyncio

async def command(ctx, client):
  commandList = []
  user = client.get_user(ctx.author.id)
  t = parseMessage(ctx.content)
  for i in os.listdir("commands"):
    if "pycach" in i:
      continue
    elif i[len(i)-3:len(i)-1] != ".p":
      continue
    commandList.append(i[:-3])

  try: #Checks if a valid command is given
    command = None
    for i in commandList:
      if i in t.getFromIndex(1):
        command = i
        break

    commandFile = importlib.import_module("commands."+command)
    title = ["❓"+ctx.author.name+" needs help! ❓", commandFile.info.get("name")]
    field = ["...",commandFile.info.get("desc")]

    await ctx.channel.send(content = "", embed = baseEmbed([title, field]))

  except:
    command = None
    titleList = ["❓"+ctx.author.name+" needs big help! ❓"]
    fieldList = ["..."]
    for i in commandList:
      commandFile = importlib.import_module("commands."+i)
      titleList.append(commandFile.info.get("name"))
      fieldList.append(commandFile.info.get("desc"))

    he = await ctx.channel.send(HELP)
    await user.send(content = "", embed=baseEmbed([titleList, fieldList]))
    await asyncio.sleep(4)
    await he.delete()

info = {
  "name" : ">help [command]",
  "desc" : "If you really want to know what this thing 'does'"
}