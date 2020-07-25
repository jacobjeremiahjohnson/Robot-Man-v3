from config import*

info = {
  "name" : ">eat",
  "desc" : "monch"
}

async def command(ctx, client):

	board = """
	1️⃣2️⃣3️⃣
4️⃣5️⃣6️⃣
7️⃣8️⃣9️⃣"""

	await ctx.channel.send(board)
	await ctx.channel.send(content = "No, I don't want thaht")