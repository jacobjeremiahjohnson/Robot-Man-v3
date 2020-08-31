from config import*

async def game(ctx, client, initial, opponent):

	# Initial setup

	# Valid numbers in play
	numDict = {
		"1" : "1⃣",
		"2" : "2⃣",
		"3" : "3⃣",
		"4" : "4⃣",
		"5" : "5⃣",
		"6" : "6⃣",
		"7" : "7⃣",
		"8" : "8⃣",
		"9" : "9⃣"
	}

	# Valid numbers to display
	emojiDict = {
		"1⃣" : "1",
		"2⃣" : "2",
		"3⃣" : "3",
		"4⃣" : "4",
		"5⃣" : "5",
		"6⃣" : "6",
		"7⃣" : "7",
		"8⃣" : "8",
		"9⃣" : "9"
	}

	possibleWins = ["123", "231", "312", "456","564", "645", "789", "879", "798", "147", "471", "714", "258", "582", "825", "369", "693", "936", "159" ,"591", "915", "357", "573", "735"]

	def checkWin(moveList):

		if len(moveList) < 3: # A valid win can never happen before three moves
			return False

		elif len(moveList) >= 3: # Do stuff

			for i in range(1, len(moveList)+1): # Iterate through each element of the total move list
					print(moveList)
					tripString = ""

					for i in moveList[0:3]: # Create three-character strings at each index of the move List
						tripString = tripString + i
					print(tripString)

					if tripString in possibleWins: # Check if the current three-character string is in the list of valid wins
						return True	

					elif tripString.reverse() in possibleWins: # Reverse to increase chances of reading a valid string
						return True

					else: # Cycle through the move list to shuffle and vary the next three-character string
						tag = moveList[0]
						moveList.remove(tag)
						moveList.append(tag)
					print(moveList)
			return False
			

	board = """

{}{}{}
{}{}{}
{}{}{}

""" # Board template

	turn = random.choice([ctx.author, opponent]) # Randomize who goes first

	moveRequest = "{mention}, it's your turn!".format(mention = turn.mention) # Ping whoever's turn it is

	screen = await ctx.channel.send(moveRequest + board.format(numDict.get("1"), numDict.get("2"), numDict.get("3"), numDict.get("4"),numDict.get("5"),numDict.get("6"),numDict.get("7"),numDict.get("8"),numDict.get("9"))) # Yucky yucky code that draws the board from the valid numbers in play

	authorList = [] # Initialize lists of both players' moves
	opponentList = []

	# Main Game Loop 
	while True:
		moveRequest = "{mention}, it's your turn!".format(mention = turn.mention)

		# This disgusting line displays the board with the corresponding emojis in numDict

		await screen.edit(content = moveRequest + board.format(numDict.get("1"), numDict.get("2"), numDict.get("3"), numDict.get("4"),numDict.get("5"),numDict.get("6"),numDict.get("7"),numDict.get("8"),numDict.get("9")))

		# This adds the proper reactions based on what has already been played

		for key in emojiDict:
			await screen.add_reaction(key)

		# Only accept input from person who's turn it is

		def check(reaction, user):
			emoji = False
			for key in numDict:
				if numDict.get(key) == str(reaction.emoji):
					emoji = True

			return user == turn and emoji == True

		try:
			reaction, user = await client.wait_for('reaction_add', timeout = 30.0, check = check) 
		except asyncio.TimeoutError: # If nobody does anything
			await screen.clear_reactions()
			await screen.edit(content = "Game over, someone didn't make a move.")
			return
		else:

			# Turn toggle and other stuff
			digit = emojiDict.get(str(reaction.emoji)) # Gets corresponding number from reaction

			# Removes the reaction that was just played

			await screen.remove_reaction(str(reaction.emoji), client.user) 
			await screen.remove_reaction(str(reaction.emoji), turn)

			if turn == ctx.author:
				mark = "🔴"	
				authorList.append(digit)
				if checkWin(authorList) == True:
					dickt = await dbGET(client, "tictactoeDB")
					for i in dickt:
						if i == str(turn):
							val = dickt.get(str(turn))

							pair = {str(turn):str(int(val) + 1)}
							await dbADD(client, "tictactoeDB", pair)
							return
					else:
						continue

					await dbADD(client, "tictactoeDB", {str(turn):"1"})

					await screen.clear_reactions()
					numDict[digit] = mark
					await screen.edit(content = turn.mention + " won!" + board.format(numDict.get("1"), numDict.get("2"), numDict.get("3"), numDict.get("4"),numDict.get("5"),numDict.get("6"),numDict.get("7"),numDict.get("8"),numDict.get("9")))

					return
				turn = opponent
			else:
				mark = "❌"
				opponentList.append(digit)
				if checkWin(opponentList) == True:
					dickt = await dbGET(client, "tictactoeDB")
					for i in dickt:
						if i == str(turn):
							val = dickt.get(str(turn))

							pair = {str(turn):str(int(val) + 1)}
							await dbADD(client, "tictactoeDB", pair)
							return
					else:
						continue

					await dbADD(client, "tictactoeDB", {str(turn):"1"})

					await screen.clear_reactions()
					numDict[digit] = mark
					await screen.edit(content = turn.mention + " won!" + board.format(numDict.get("1"), numDict.get("2"), numDict.get("3"), numDict.get("4"),numDict.get("5"),numDict.get("6"),numDict.get("7"),numDict.get("8"),numDict.get("9")))
					
					break
				turn = ctx.author

			numDict[digit] = mark
			emojiDict.pop(str(reaction.emoji))
			
			if bool(emojiDict) == False:
		
				await screen.edit(content = "Tie, that's lame." + board.format(numDict.get("1"), numDict.get("2"), numDict.get("3"), numDict.get("4"),numDict.get("5"),numDict.get("6"),numDict.get("7"),numDict.get("8"),numDict.get("9")))

				break