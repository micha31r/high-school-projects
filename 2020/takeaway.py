"""
-------------------------------------------------
   Project: Take-Away Game
  Standard: 91883 (AS1.7) v.1
    School: Tauranga Boys' College
    Author: Michael Ren
      Date: 20 March 2020
    Python: 3.6.4
   License: MIT
-------------------------------------------------
"""

import random as RD 	# import the random library to generate random numbers
import sys 				# import the sys library to quit the program

class Player:
	def __init__(self):
		self.name = input("Name:")
		self.score = 0

	# Receive and validate user input 
	def userInput(self):
		amount_to_take = input(f"Select the amount of chips to take:")
		# Input validation
		try: amount_to_take = abs(int(amount_to_take)) # Convert input to a positive interger
		except: self.inputError()
		return amount_to_take

	# Display input error and quit the game
	def inputError(self):
		print("Invalid Input!")
		print("Don't Try To Break THE GAME!")
		print("I QUIT!")
		sys.exit(0)


class Game:
	def __init__(self):
		self.entities = [] 	# This array will store all player entities
		self.MAXCHIPS = 21 	# A constant of the total number of chips
		self.MAX_TAKE_AWAY_AMOUNT = 10
		self.MAXROUNDS = input("How Many Rounds?")
		# Only proceed if the MAXROUND variable is a number
		if self.MAXROUNDS.isdigit(): self.MAXROUNDS = abs(int(self.MAXROUNDS))
		else: sys.exit(0) # Quit Game

	# Create a player obj and store store it in self.entities
	def addPlayer(self): 
		player = Player()
		if not player.name.isalpha(): self.addPlayer() # Player name validation
		else: self.entities.append(player)

	# Set random player order
	def shufflePlayerOrder(self): 
		random.shuffle(self.entities)

	# Main game loop
	def loop(self):
		# Cycle through each round
		for i in range(self.MAXROUNDS):
			chips_left = self.MAXCHIPS 
			print(f"\nRound {i+1}!\n")
			# While this round is not finished
			while chips_left > 0:
				# Cycle through each player
				for player in self.entities: 
					# Print whos turn is it and the amount of chips left
					print(f"{player.name}, Your turn")
					print(f"{chips_left} Chips Left\n")
					amount_to_take = player.userInput() # Get user input
					# Validate user input
					# Input cannot be larger than MAX_TAKE_AWAY_AMOUNT
					if amount_to_take > self.MAX_TAKE_AWAY_AMOUNT: 
						amount_to_take = self.MAX_TAKE_AWAY_AMOUNT
						print(f"The Max Amount You Can Take is {self.MAX_TAKE_AWAY_AMOUNT}")
						print(f"Grabbed {self.MAX_TAKE_AWAY_AMOUNT} Chips")
					if amount_to_take > chips_left: amount_to_take = chips_left
					# Drops a random amount of chips if player grabs more than one chip
					if amount_to_take > 1:
						dropped = RD.randint(0, amount_to_take)
						# Subtract the dropped chips from the amount player wishes to take
						amount_to_take -= dropped 
						if dropped > 0: 
							print("Ohh No! The Chips Are Too Hard To Grab On!")
							print(f"Dropped {dropped} Chips\n")
					# Subtract grabbed chips from the remaining chips
					chips_left -= amount_to_take 
					# Increase player score if player wins the current round
					if chips_left == 0: 
						print(f"Congrats {player.name}!")
						player.score += 1
						break # Break Loop to start a new round

	def winner(self):
		best = 0
		winner = None
		# Cycle thought every player and compare to see who has the most score
		for player in self.entities:
			if player.score > best:
				winner = player
				best = player.score
		print(f"Winner: {winner.name} scored {best}")

try: 
	game = Game() 	# Initialise the Game
	for i in range(int(input("How Many Players?"))): game.addPlayer()
	game.loop() 	# Start the game loop
	game.winner() 	# Show winners
except:
	# If anything goes wrong then display this message instead of STD error message
	print("I Have A Bad Feeling About This..")
