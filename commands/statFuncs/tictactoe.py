from config import*
	
async def command(ctx, client, user):
	dickt = await dbGET(client, "tictactoeDB")
	for i in dickt:
		if i == str(user.id):
			await ctx.channel.send("Overall, they have {x} wins.".format(x = str(dickt.get(i))))
			return
		else:
			continue
	await ctx.channel.send("Erm, I don't think that person has played tictactoe yet..")