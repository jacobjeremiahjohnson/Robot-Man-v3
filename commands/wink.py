from config import*

info = {
  "name" : ">wink",
  "desc" : "( ͡- ͜ʖ ͡°)"
}

async def command(ctx):
  msg = await ctx.channel.send("( ͡° ͜ʖ ͡°)")

  while True:
    await msg.edit(content = "( ͡° ͜ʖ ͡°)")
    await asyncio.sleep(2)
    await msg.edit(content = "( ͡- ͜ʖ ͡°)")
    await asyncio.sleep(0.5)
    await msg.edit(content = "( ͡° ͜ʖ ͡°)")
    await asyncio.sleep(2)
    await msg.edit(content = "( ͡° ͜ʖ ͡-)")
    await asyncio.sleep(0.5)