from config import*

async def game(ctx, client, initial, opponent):

	# initial setup

	board = """

	{}{}{}{}{}{}{}
	{}{}{}{}{}{}{}	
	{}{}{}{}{}{}{}	
	{}{}{}{}{}{}{}	
	{}{}{}{}{}{}{}	
	{}{}{}{}{}{}{}	
"""

	board  = "{}{}{}{}{}{}{}"

	eL = [["⚫️","⚫️","⚫️","⚫️","⚫️","⚫️"],
	["⚫️","⚫️","⚫️","⚫️","⚫️","⚫️"],
	["⚫️","⚫️","⚫️","⚫️","⚫️","⚫️"],
	["⚫️","⚫️","⚫️","⚫️","⚫️","⚫️"],
	["⚫️","⚫️","⚫️","⚫️","⚫️","⚫️"],
	["⚫️","⚫️","⚫️","⚫️","⚫️","⚫️"],
	["⚫️","⚫️","⚫️","⚫️","⚫️","⚫️"]]

	# Edit collumns directly from reacts, display board by creating a list of the 0th item from the collumn lists and messaging line at a time, edit live, detect wins somehow

	lineList = [line0, line1, line2, line3, line4, line5]

	line0 = None
	line1 = None
	line2 = None
	line3 = None
	line4 = None
	line5 = None

	for i in range(0, 5):
		for b in range(0, 6):
			await ctx.channel.send(board.format(eL[i][b]))
