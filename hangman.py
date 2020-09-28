from play import word_list
import random

def getRandom():
	word = random.choice(word_list)
	return word.upper()

def play(word):
	word_complition = "-"*len(word)
	guessed = False
	guess_letter = []
	guess_word = []
	tries = 6

	print("Lets play Hangman!")
	print(word_complition)
	print(displayHangman(tries))

	while not guessed and tries > 0:
		guess = input("Enter the guess: ").upper()
		if len(guess) == 1 and guess.isalpha():
			if guess in guess_letter:
				print(f"You have already guessed {guess}")
			elif guess not in word:
				print(guess,"is not in the word.")
				tries -= 1
				guess_letter.append(guess)
				# print(tries)
				print(displayHangman(tries))
			else:
				print("Good job",guess,"is in the word!")
				guess_letter.append(guess)
				word_as_list = list(word_complition)
				indices = [i for i,letter in enumerate(word) if letter == guess]
				for index in indices:
					word_as_list[index] = guess
				word_complition = "".join(word_as_list)
				if "-" not in word_complition:
					guessed = True
			print(word_complition)
		elif len(guess) == len(word) and guess.isalpha():
			if guess in guess_word :
				print("You have already guessed this word",guess)
			elif guess != word:
				print(guess,"is not in the word.")
				guess_word.append(guess)
				tries -= 1
				print(displayHangman(tries))
			else:
				# print("Good job",guess,"is the correct word!")
				guessed = True
				word_complition = word

		else:
			print("Not vaild case")
			print(word_complition)

	if guessed:
		print("Congrats, you gussed the word! You win!\n\n")


	else:
		print("Sorry you ran out of tries.The word was",word,".")





def displayHangman(tries):
	stages = [
	# 6 Final stage : head body two hands and two legs
	"""
		--------
		|   |
		|   O
		|  \\|/
		|   |  	
		|  / \\
	   

	""",
	# 5 :head body hands and one leg
	"""
		--------
		|   |
		|   O
		|  \\|/
		|   |  	
		|  / 
	    

	""",
	# 4 :head body two hands
	"""
		--------
		|   |
		|   O
		|  \\|/
		|   |  	
		|   
	    

	""",
	# 3 : head body and one hand
	"""
		--------
		|   |
		|   O
		|  \\|
		|   |  	
		|   
	    

	""",
	#2 : head body
	"""
		--------
		|   |
		|   O
		|   |
		|   |  	
		|   
	    

	"""	,
	# 1:head 
	"""
		--------
		|   |
		|   O
		|  
		|     	
		|   
	    

	""",
	# 0 : Initial Stage
	"""
		--------
		|   |
		|	
		|  
		|     	
		|   
        

	"""	 	]

	return stages[tries]

def main():
	word = getRandom()
	print(word)
	play(word)

if __name__ == "__main__":
	while True:
		main()
		ans = input("Shall we continue? ([y]/n): ")
		if ans == "n":
			break