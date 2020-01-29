from config import*

info = {
  "name" : ">dab",
  "desc" : "Dab on the haters with this epic command"
}

async def command(ctx):
  msg = await ctx.channel.send("<o/")

  while True:
    await msg.edit(content = "\o>")
    await asyncio.sleep(1)
    await msg.edit(content = "<o/")
    await asyncio.sleep(1)