from config import*

info = {
  "name" : ">noah",
  "desc" : "Get the latest inspirational, insightful tweet from America's sweetheart Noah Centineo"
}

async def command(ctx):
  t = parseMessage(ctx.content)

  auth = tweepy.AppAuthHandler(os.environ.get("consumerkey"), os.environ.get("consumersecret"))
  api = tweepy.API(auth)
  noah = api.get_user(336715401)

  try:
    gak = t.getFromIndex(1)
  except:
    gak = "none"

  if gak == "random":
    x = 0
    postList = []
    flagId = noah.status.id

    while True:
      recents = api.user_timeline(336715401, max_id=flagId)
      for i in recents:
        postList.append(i)
        x+=1
        #await m.edit(content = m.content)
      for i in postList:
        if i.retweeted == True:
          postList.pop(postList.index(i))
      flagId = postList[len(postList)-1].id
      postList.pop(len(postList)-1)
      if len(postList) > 1500:
        break
    post = randomItem(postList)
  elif gak == "none":
    post = noah.status

  embed = discord.Embed(
      title = noah.name+" • "+str(calendar.month_name[post.created_at.month])+" "+str(post.created_at.day)+", "+str(post.created_at.year),
      description = "["+post.text+"]"+"("+"https://twitter.com/noahcent/status/"+str(post.id)+")",
      colour = 0x1dcaff,
  )
  embed.set_author(name = "@"+noah.screen_name, icon_url="https://cdn.discordapp.com/attachments/459080723253690389/642374653892886548/noah",url="https://twitter.com/noahcent?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor")
  embed.set_footer(text = "Twitter for iPhone")
  embed.add_field(name = "<3 - "+str(post.favorite_count)+"  |  -> - "+str(post.retweet_count), value = "I'm sorry")
  await ctx.channel.send(embed=embed,content="")