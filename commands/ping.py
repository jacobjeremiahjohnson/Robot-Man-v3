from config import*

info = {
  "name" : ">ping",
  "desc" : "For testing if I've fucked something up"
}

async def command(ctx):
  PingList = ["Pang", "Pyng", "Pung", "Peng", "Gak"]
  await ctx.channel.send(random.choice(PingList))