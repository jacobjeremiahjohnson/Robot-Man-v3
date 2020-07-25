from config import*

info = {
  "name" : ">reddit [hot, top, etc.] [subreddit]",
  "desc" : "There's NSFW protection now you degenerates"
}

async def command(ctx, client):
  reddit = praw.Reddit(client_id=os.environ.get("secret"), \
                     client_secret=os.environ.get("token"), \
                     user_agent='Robot man', \
                     username=os.environ.get('username'), \
                     password=os.environ.get('password'))
  t = parseMessage(ctx.content)

  try: #Sets default sort to hot as well as define subreddit
    sub = t.getFromIndex(2)
    sortBy = t.getFromIndex(1)
  except:
    sub = t.getFromIndex(1)
    sortBy = "hot"

  if sub.startswith("r/"):
    sub = sub[2::]

  subreddit = reddit.subreddit(sub)

  subredditMap = {
    "hot" : subreddit.hot(),
    "top" : subreddit.top(),
    "rising" : subreddit.rising(),
    "controversial" : subreddit.controversial(),
    "new" : subreddit.new()
  }

  Subreddit = subredditMap.get(sortBy)

  try:
    for submission in Subreddit:
      print("this thing exists")
      break
  except NotFound:
    await ctx.channel.send(content = "", embed=errorEmbed(ctx.message.content, ">reddit [Sort By][EXISTING Subreddit]"))
  else:
    for submission in Subreddit:

      if submission.stickied != True and len(submission.title) < 256:
        elements = submission.url.split("/")

        if submission.over_18 == True:
          with urllib.request.urlopen(submission.url) as site:
            urllib.request.urlretrieve(submission.url, elements[3])
          link = elements[3]
          File = discord.File(link, spoiler = True)

        else:
          with urllib.request.urlopen(submission.url) as site:
            urllib.request.urlretrieve(submission.url, elements[3])
          link = elements[3]
          File = discord.File(link, spoiler = False)
          
        embed = discord.Embed(
            title = submission.title,
            description = "[r/" + sub + " " + sortBy + "]"+"(https://reddit.com/r/"+sub+"/"+sortBy+")",
            colour = 16733952
        )
        if submission.selftext != "" and len(submission.selftext) < 1024:
            embed.add_field(name = "...", value = submission.selftext, inline = False)

        embed.set_image(url="attachment://"+link)
        embed.add_field(name = "...", value = "[u/" + str(submission.author)+"]"+"(https://reddit.com/u/"+str(submission.author)+"/)", inline = False)
        embed.add_field(name = "...", value = "[Post](https://reddit.com"+submission.permalink+")", inline = False)
        print("a real error")
        await ctx.channel.send(content="",embed=embed,file=File)
        os.remove(link)
        break
      else:
        continue