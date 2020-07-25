from config import*

async def game(ctx, client, initial, opponent):

	try:
				challenger = ctx.author
				background = "So, you and __{x}__ have both been taken in for questioning. The police officer gives you a choice, either **deny** the crime or **rat out** __{x}__. __{x}__ has the same choice. If you **both deny** the crime, you each serve **1 year** in prison. If **one of you denies** and the **other rats out**, the **one who denied** gets **2 years** and the **one who ratted out goes free.** If **both of you rat eachother out,** you **each** serve a **year and a half.** "
				challBack = await challenger.send(background.format(x = opponent.name))
				oppoBack = await opponent.send(background.format(x = challenger.name))

				opponentVote = None
				challengerVote = None

				opponentChoice = await opponent.send("Do you **rat** or **deny**? (You have 60 seconds)")
				
				await opponentChoice.add_reaction("🐀")
				await opponentChoice.add_reaction("🚫")

				challengerChoice = await challenger.send("Do you **rat** or **deny**? (You have 60 seconds)")

				await challengerChoice.add_reaction("🐀")
				await challengerChoice.add_reaction("🚫")

				def check(reaction, user):
					return user == opponent or user == challenger and str(reaction.emoji) == "🐀" or str(reaction.emoji) == "🚫"

				reaction, user = await client.wait_for('reaction_add', timeout = 60.0, check = check)

				choicePair = ["-", "-"]

				while True:
					reaction, user = await client.wait_for('reaction_add', timeout = 60.0, check = check)

					if user == opponent:
						choicePair[1] = str(reaction.emoji)
					elif user == challenger:
						choicePair[0] = str(reaction.emoji)
					
					if choicePair[0] != "-" and choicePair[1] != "-":
						break

				choiceDict = {
					"🐀🚫" : ["free","to jail for 2 years"],
					"🐀🐀" : ["to jail for a year and a half","to jail for a year and a half"],
					"🚫🐀" : ["to jail for 2 years", "free"],
					"🚫🚫" : ["to jail for 1 year", "to jail for 1 year"]
				}

				result = choiceDict.get("".join(choicePair))

				await ctx.channel.send("The results are in.\n**{x}** chose {emoji1}.\n**{y}** chose {emoji2}.\nTherefore,\n**{x}** goes {result1} and **{y}** goes {result2}.".format(x = challenger.mention, y = opponent.mention, emoji1 = choicePair[0], emoji2 = choicePair[1], result1 = result[0], result2 = result[1]))

				async def challengerADD():

					dickt = await dbGET(client, "prisonerDB")
					for i in dickt:
						if i == str(challenger):
							val = dickt.get(str(challenger))
							#Values are two item lists, first value is ratted, second is denied
							if str(choicePair[0]) == "🐀":
								resultList = [val[0] + 1, val[1]]
							elif str(choicePair[0]) == "🚫":
								resultList = [val[0],val[1] + 1]
							pair = {str(challenger):resultList}
							await dbADD(client, "prisonerDB", pair)
							return
						else:
							continue

					if str(choicePair[0]) == "🐀":
						resultList = [1 , 0]
					elif str(choicePair[0]) == "🚫":
						resultList = [0 , 1]
					pair = {str(challenger):resultList}
					await dbADD(client, "prisonerDB", pair)

				async def opponentADD():

					dickt = await dbGET(client, "prisonerDB")
					for i in dickt:
						if i == str(opponent):
							val = dickt.get(str(opponent))
							#Values are two item lists, first value is ratted, second is denied
							if str(choicePair[1]) == "🐀":
								resultList = [val[0] + 1, val[1]]
							elif str(choicePair[1]) == "🚫":
								resultList = [val[0],val[1] + 1]
							pair = {str(opponent):resultList}
							await dbADD(client, "prisonerDB", pair)
							return
						else:
							continue

					if str(choicePair[1]) == "🐀":
						resultList = [1 , 0]
					elif str(choicePair[1]) == "🚫":
						resultList = [0 , 1]
					pair = {str(opponent):resultList}
					await dbADD(client, "prisonerDB", pair)

				await challBack.delete()
				await oppoBack.delete()
				await opponentChoice.delete()
				await challengerChoice.delete()

				await challengerADD()
				await opponentADD()

	except:
				await ctx.channel.send("Oop that person can't be dm'd, sorry.")