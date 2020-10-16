from config import*

info = {
  "name" : ">reverse [String]",
  "desc" : "For epic string reversal"
}

async def command(ctx, client):
  t = parseMessage(ctx.content)
  await ctx.channel.send(t.getContent(1)[::-1])