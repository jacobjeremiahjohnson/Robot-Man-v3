from config import*

info = {
  "name" : ">translate [Language Code] [Foreign String]",
  "desc" : "For all those people who speak English and want to understand some off-brand language"
}

async def command(ctx):
  translator = Translator()
  t = parseMessage(ctx.content)
  if t.getFromIndex(1).startswith("lang:"): 
    index = 2
    call, lang = t.getFromIndex(1).split(":")
    Dest = lang
  elif translator.translate(t.getContent(1)).text == t.getContent():
    index = 1
    Dest = 'es'
  else:
    index = 1
    Dest = 'en'
  await ctx.channel.send(content = "", embed = baseEmbed([["💱"+ctx.author.name+" is doing a translate 💱", translator.translate(t.getContent(index), dest = Dest).text],["...","..."]]))