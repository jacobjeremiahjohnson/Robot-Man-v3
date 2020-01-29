from config import*

info = {
  "name" : ">flood [cusom string]",
  "desc" : "Make *all* the mods angry"
}

async def command(ctx):
  t = parseMessage(ctx.content)
  print(t.getContent(1))
  
  if t.getContent(1) == "": #If no custom message is provided, a random one from a list is
    for i in range (0,5): #Wow I learned how to do it
      spam = ['gak','mo','bee','loot','owo']
      await ctx.channel.send(os.environ.get(random.choice(spam)))
  else:
    custom = t.getContent(1) #Sets custom to custom message provided 
    newCustom = custom #Creates two identical variables 
    while 2000-len(custom) > len(newCustom): #Adds the custom message to the full message until adding another one would break the 2000 character limit
      custom = custom+newCustom
    for i in range (0,5): #This *should* work
      await ctx.channel.send(custom)