from config import dbCREATE, dbADD

info = {
	"name" : ">edit",
	"desc" : "Don't worry about it"
	}

async def command(ctx, client):

	await ctx.channel.send("Edited!")