from config import*

info = {
  "name" : ">dab",
  "desc" : "Dab on the haters with this eic command"
}

async def command(ctx, client):
  msg = await ctx.channel.send("<o/")
  print(ctx.content)
  while True:
    await msg.edit(content = "\o>")
    await asyncio.sleep(1)
    await msg.edit(content = "<o/")
    await asyncio.sleep(1)