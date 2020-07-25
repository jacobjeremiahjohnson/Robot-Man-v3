from config import*

info = {
  "name" : ">ping",
  "desc" : "For testing if I've fucked something up"
}

async def command(ctx, client):
  PingList = ["Pang", "Pyng", "Pung", "Peng", "Gak", "lmao fuck you julie"]
  await ctx.channel.send(random.choice(PingList))