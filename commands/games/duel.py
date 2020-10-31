from config import*
import asyncio, random

async def game(ctx, client, initial, opponent):

			# Game time
			await initial.edit(content = "In a few seconds, I'll send 🚩. Once that happens, whoever sends a message first wins.")
			
			def check(msg):	
				return msg.author == ctx.author or msg.author == opponent

			try:
				message = await client.wait_for('message', timeout = random.randint(4, 9), check=check)
			except asyncio.TimeoutError:
				# GAME TIME p.2
				await ctx.channel.send("🚩")

				def check(m):
					return m.author == ctx.author or m.author == opponent

				try:
					message = await client.wait_for('message', timeout = 10, check=check)
				except asyncio.TimeoutError:
					await ctx.channel.send("...no one said anything.")
				else:
					winner = message.author
					await ctx.channel.send("🔫{x} won!".format(x = message.author.mention))

			else: #If a message was sent in between game time and game time p.2
				await ctx.channel.send("❗ Misfire ❗ {x} loses!".format(x = message.author.mention))
				if message.author == opponent:
					winner = ctx.author
				elif message.author == ctx.author:
					winner = opponent
			
			print(winner)
			dickt = await dbGET(client, "DuelDB")
			for i in dickt:
				if i == str(winner.id):
					val = dickt.get(str(winner.id))

					pair = {str(winner.id):str(int(val) + 1)}
					await dbADD(client, "DuelDB", pair)
					return
				else:
					continue

			await dbADD(client, "DuelDB", {str(winner.id):"1"})
			return