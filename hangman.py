# Importing required libraries
import string
import time
import re
import random
from words import choose_word
from images import IMAGES

# Initializing libraries
LETTERS = string.ascii_lowercase
HINT_USED = False

def is_word_guessed(secret_word, letters_guessed):
	'''
	Function to verify if letters_guessed can create secret_word
	Basically checking if all the letters in secret_word are present in letters_guessed
	'''
	for letter in secret_word:
		if letter not in letters_guessed:
			return False
	return True

def get_guessed_word(secret_word, letters_guessed):
	'''
	Returning words with guessed letters exposed and letters yet to be guessed with an underscore _
	'''
    guessed_word = ""
    for letter in secret_word:
    	if letter in letters_guessed:
    		guessed_word += letter
    	else:
    		guessed_word += '_'
    return guessed_word

def get_available_letters(letters_guessed):
	'''
	Returning letters that are available for the player to guess still. Initialising with letters [a-z]
	'''
	global LETTERS
	if len(letters_guessed) >= 1:
		LETTERS = LETTERS.replace(letters_guessed[-1],'')
	return LETTERS

def display_hangman(remaining_lives, letters_guessed):
	'''
	Function to simply print the hangman status every time there's a incorrectly guessed letter by the player.
	'''
	print(IMAGES[7 - remaining_lives])

def check_validity(guess, secret_word, letters_guessed):
	'''
	Function for checking validity of input from player and providing support for hint.
	'''
	global HINT_USED
	if len(guess) != 1:
		if guess.lower() == 'hint':
			if not HINT_USED:
				try:
					print("\tHint: {}\n\n".format(random.choice([c for c in secret_word if c not in letters_guessed])))
					HINT_USED = True
					return False
				except IndexError:
					print("\n\tAn error occurred.\n\tCannot choose from an empty sequence!\n\n")
			else:
				print("\tHint is available only once in one gameplay!\n\n")
				return False
		print("\tInvalid input, enter a letter as guess.\n\n")
		return False
	elif guess not in string.ascii_lowercase:
		print("\tInvalid input, enter a letter as guess.\n\n")
		return False
	return True

def hangman(secret_word):
	'''
	Pretty much the entire layout setup, input handling etc is present in this chunk of code.
	'''
	print("\n\n\n\t\t\t\t\t\tWelcome to the game, Hangman!")
	time.sleep(2)
	print("\n\tI am thinking of a word that is {} letters long.".format(str(len(secret_word))), end = '\n\n')
	time.sleep(2)
	letters_guessed =[]
	remaining_lives = 8
	blanks_to_fill = len(secret_word)
	
	while remaining_lives > 0:
		available_letters = get_available_letters(letters_guessed)
		
		blanks_to_fill = len(re.sub("|".join(letters_guessed), "", secret_word))
		
		# Some nice formatting
		print("\n\t"+">"*125)
		print("\tAvailable letters: {} \t\t\tRemaining lives: {}\t\t\tBlanks to fill: {}".format(available_letters, remaining_lives, blanks_to_fill))
		time.sleep(1)
		guess = input("\n\n\tPlease guess a letter: ")
		if not check_validity(guess, secret_word, letters_guessed):
			continue
		letter = guess.lower()
		
		time.sleep(1)
		if letter in letters_guessed:
			print("\n\tYou have already guessed {}\n\tTry something different this time!\n\n".format(letter))
			continue
		if letter in secret_word:
		
			letters_guessed.append(letter)
			print("\n\tGood guess: {} ".format(get_guessed_word(secret_word, letters_guessed)))
			
			if is_word_guessed(secret_word, letters_guessed):
				print("\n\n\t\t\t\t\t\t * * Congratulations, you won! * * ")
				
				if len(letters_guessed) == len(secret_word):
					print("\t\t\t\t\t\t * * Perfect Game!! You rock!! * * ")
					
				else:
					print("\t\t\t\t\t\t* * You won with {} lives left! * *".format(remaining_lives))
				
				break
		else:
			remaining_lives -= 1
			print("\tOops! That letter is not in my word: {} \n".format(get_guessed_word(secret_word, letters_guessed)))
			letters_guessed.append(letter)
			display_hangman(remaining_lives, letters_guessed)
			
		if remaining_lives == 0:
			print("\tGame over!!\n")
			print("\n\tThe word was: {}".format(secret_word))
			print("_"*150)
			break

if __name__ == '__main__':
	'''
	Driver function
	'''
	secret_word = choose_word()
	hangman(secret_word)
