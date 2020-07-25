from config import*
	
async def command(ctx, client, user):
	dickt = await dbGET(client, "DuelDB")
	for i in dickt:
		if i == str(user):
			dickt = {k: v for k, v in sorted(dickt.items(), key=lambda item: item[1])}
			for j in dickt:
				top = j
				break
			await ctx.channel.send("Overall, they have {x} wins.".format(x = str(dickt.get(i))))
			return
		else:
			continue
	await ctx.channel.send("Erm, I don't think that person has dueled anyone yet..")