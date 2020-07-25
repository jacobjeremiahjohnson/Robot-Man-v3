from config import*

info = {
  "name" : ">noah",
  "desc" : "Get the latest inspirational, insightful tweet from America's sweetheart Noah Centineo"
}

async def command(ctx, client):
  async with ctx.channel.typing():
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

      post = random.choice(postList)

    elif gak == "none":
      post = noah.status

    embed = discord.Embed(
        title = str(calendar.month_name[post.created_at.month])+" "+str(post.created_at.day)+", "+str(post.created_at.year),
        description = post.text,
        colour = discord.Color.blue(),
    )

    embed.set_author(name = "{name} (@{username})".format(name = noah.name, username = noah.screen_name), icon_url=noah.profile_image_url_https,url="https://twitter.com/noahcent?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor")
    embed.set_footer(text = "Twitter", icon_url = "")
    embed.add_field(name = "Retweets", value = str(post.favorite_count))
    embed.add_field(name = "Likes", value = str(post.retweet_count))
    
    await ctx.channel.send(embed=embed,content="")