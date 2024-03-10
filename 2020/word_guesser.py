import random, os, time, sys

class Player:
	def __init__(self,word):
		self.name = input("Player Name:")
		self.penalties = 0
		self.points = 0
		self.guessed_letter = word

	def action(self):
		guess = input("Your Guess (1 letter):")[:1]
		if guess:
			return guess
		else:
			print("Invalid Input (try again)")
			guess = self.action()
			return guess

	def render(self):
		print(f"Points: {self.points}")
		print(f"Penalties: {self.penalties}")
		word = ""
		for letter in self.guessed_letter:
			word += letter
		print(f"Current Guesses: {word}")

	def __str__(self):
		return str(self.guessed_letter) + self.name

class Game: 
	def __init__(self,player_num):
		self.word_list = ["apple","michael","computer","laptop","window","important","quantum"]
		self.chosen_word = random.choice(self.word_list)
		self.entities = []
		for i in range(player_num):
			placeholder = []
			for letter in range(len(self.chosen_word)):
				placeholder.append("_")
			self.entities.append(Player(placeholder))
		print(f"This Word Have {len(self.chosen_word)} Letters")

	def check(self,guess,player):
		pos = []
		for i in range(len(self.chosen_word)):
			if guess == self.chosen_word[i]:
				pos.append(i)
		if not pos:
			print("Wrong Guess")
			print("You Gained 1 PENALTY")
			player.penalties += 1	
			return
		for indice in pos:
			if player.guessed_letter[indice] == "_":
				print("Correct Guess")
				print("You Gained 1 POINT")
				player.guessed_letter[indice] = guess
				player.points += 1
				return
		print("Already Guessed")
		guess = player.action()
		self.check(guess,player)

	def update(self):
		for player in self.entities:
			os.system("clear") 
			print(f"{player.name}, Your Turn")
			guess = player.action()
			self.check(guess,player)
			print("Stats:")
			player.render()
			if "_" not in player.guessed_letter:
				print(f"{player.name} Won The Game!!")
				print(f"Total Points: {player.points - player.penalties}")
				sys.exit(0)
			input("Enter To Continue")

game = Game(2)
time.sleep(2)
while True:
	try:
		game.update()
	except KeyboardInterrupt:
		break




