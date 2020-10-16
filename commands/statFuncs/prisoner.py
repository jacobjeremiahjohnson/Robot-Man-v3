from config import*

async def command(ctx, client, user):
	dickt = await dbGET(client, "prisonerDB")
	for i in dickt:
		if i == str(user.id):
			val = dickt.get(i)
			whole = int(val[0]) + int(val[1])
			part = int(val[0])
			await ctx.channel.send("{name} has ratted {r} times and has denied {d} times, leading to a rat percentage of {t}.".format(name = user.name, r = val[0], d = val[1], t = 100 * float(part)/float(whole)))
			return
		else:
			continue

	await ctx.channel.send("I don't think they've ever played prisoner.")
	