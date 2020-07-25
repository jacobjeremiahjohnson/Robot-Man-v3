from config import*

info = {
	"name" : ">stats @Person [Game]",
	"desc" : "Get special info on a person on a specified game. Supported Games: duel, prisoner"
}

async def command(ctx, client):
	try:
		user = ctx.mentions[0]
	except:
		await ctx.channel.send("You didn't '@' anyone.")

	t = parseMessage(ctx.content)
	fileList = []
	for i in os.listdir("commands/statFuncs"):
		if i.endswith(".py"):
			fileList.append(i)
	for i in fileList:
		if i == t.getFromIndex(2) + ".py":
			module = importlib.import_module("commands.statFuncs."+t.getFromIndex(2))
			await module.command(ctx, client, user)
			return
	await ctx.channel.send("Game not recognized. Check `>help stats` to see games with supported stats.")
