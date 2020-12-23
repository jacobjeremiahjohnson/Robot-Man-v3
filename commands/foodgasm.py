from config import*

info = {
  "name" : ">foodgasm",
  "desc" : "It's not porn, mom, it's **art**"
}

async def command(ctx, client):
  imageList = ["https://cdn.discordapp.com/attachments/459080723253690389/576123702140207127/7.png", "https://cdn.discordapp.com/attachments/459080723253690389/576123492773134336/Untitled.png", "https://cdn.discordapp.com/attachments/459080723253690389/576123528923840532/foodgasm_5.png","https://cdn.discordapp.com/attachments/459080723253690389/576123553431158808/foodgasm_4.png","https://cdn.discordapp.com/attachments/459080723253690389/576123576550162443/foodgasm_3.png","https://cdn.discordapp.com/attachments/459080723253690389/576123599644262400/foodgasm_2.png","https://cdn.discordapp.com/attachments/459080723253690389/576123630702952459/foodgasm_1.png","https://cdn.discordapp.com/attachments/459080723253690389/576123654165889024/8.png"]
  
  embed = discord.Embed(color = discord.Color.purple()
  )
  embed.set_author(name = "💢"+ctx.author.name+" doesn't have a soul 💢")
  embed.set_image(url = random.choice(imageList))
  await ctx.channel.send(content = " ", embed=embed) #Displays a random image from a list