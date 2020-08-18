from config import*

info = {
	"name" : ">hello",
	"desc" : "Hello penguin simulator"
}

async def command(ctx, client):

	voice_channel = ctx.author.voice.channel
	print(str(voice_channel))
	await voice_channel.connect()