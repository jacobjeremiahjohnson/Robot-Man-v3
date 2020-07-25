from config import*

info = {
  "name" : ">dice [Number of sides on die]",
  "desc" : "For some good 'ol fashioned random num generation"
}

async def command(ctx, client):
  t = parseMessage(ctx.content)

  roll = str(random.randint(1, int(t.getFromIndex(1)))) #Gets the maximum provided by the user and chooses a random number

  Embed = baseEmbed([["🎲  " + ctx.author.name + " rolled a 🎲 ", roll], ["...", "..."]])
  await ctx.channel.send(content = "", embed = Embed)