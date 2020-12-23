from config import*

info = {
  "name" : ">flood [custom string]",
  "desc" : "Make *all* the mods angry"
}

async def command(ctx, client):
  t = parseMessage(ctx.content)

  if ctx.author.guild_permissions.manage_messages:

    if t.getContent(1) == "": #If no custom message is provided, a random one from a list is
      for i in range (0,5): #Wow I learned how to do it
        spam = ['gak','mo','bee','loot','owo']
        choice = random.choice(spam)
        await ctx.channel.send(os.environ.get(choice))
    else:
      custom = t.getContent(1) #Sets custom to custom message provided 
      newCustom = custom #Creates two identical variables 
      while 2000-len(custom) > len(newCustom): #Adds the custom message to the full message until adding another one would break the 2000 character limit
        custom = custom + newCustom
      for i in range (0,5): #This *should* work
        await ctx.channel.send(custom)
	
  else:
    m = await ctx.channel.send("You don't have manage message permissions, file a complaint with your precinct's Discord moderator")

 