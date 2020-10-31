info = {
  "name" : ">close",
  "desc" : "Don't even *try* to use this command. For emergencies **only**"
}

async def command(ctx, client):
	await client.close()
