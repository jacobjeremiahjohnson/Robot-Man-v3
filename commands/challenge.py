from config import*

info = {
	"name" : ">challenge @Opponent [Game Name]",
	"desc" : "Challenge people to games! Games: duel, prisoner, tictactoe"
}

async def command(ctx, client):
	t = parseMessage(ctx.content)
	
	# Check for mentions or a game

	try:
		opponent = ctx.mentions[0]
	except:
		await ctx.channel.send("You didn't challenge anyone monkey.")
		return
	
	if opponent == ctx.author:
		await ctx.channel.send("You can't challenge yourself silly.")
		return
	
	try:
		name = t.getFromIndex(2)
	except:
		await ctx.channel.send("You forgot a game. Use `>help challenge` to see a list of games.")

	# Send base accept prompt and setup react conditional

	initial = await ctx.channel.send("🚩 {m}, do you accept?".format(m = opponent.mention))
	await initial.add_reaction("✔️")
	await initial.add_reaction("❌")
	# React check
	def check(reaction, user):
		return user == opponent and str(reaction.emoji) == "✔️" or user == opponent and str(reaction.emoji) == "❌"

	try:
		reaction, user = await client.wait_for('reaction_add', timeout = 30.0, check = check)
	except asyncio.TimeoutError:
		await initial.edit(content = "Request timed out.")

	else:

		try:
			gameList = []
			for game in os.listdir("commands/games"):
					if game.endswith(".py") == True:
						gameList.append(game)
			for i in gameList:
					if i == name + ".py":
						module = importlib.import_module("commands.games."+name)
		except:
			await ctx.channel.send("Game not recognized. Check `>help stats` to see games with supported stats.")
			return

		if str(reaction.emoji) == "❌":
			await initial.edit(content = "Challenge declined.")
		elif str(reaction.emoji) == "✔️":
			await module.game(ctx, client, initial, opponent)
			return