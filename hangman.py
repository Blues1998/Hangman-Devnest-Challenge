import string
import time
import re
from words import choose_word
from images import IMAGES

LETTERS = string.ascii_lowercase

def is_word_guessed(secret_word, letters_guessed):

	for letter in secret_word:
		if letter not in letters_guessed:
			return False
	return True

#	print(str(''.join(sorted(set(secret_word)))))
#	print(str(''.join(sorted(letters_guessed))))
#	if str(''.join(sorted(set(secret_word)))) in str(''.join(sorted(letters_guessed))):
#		return True
#	return False

def get_guessed_word(secret_word, letters_guessed):
    guessed_word = ""
    for letter in secret_word:
    	if letter in letters_guessed:
    		guessed_word += letter
    	else:
    		guessed_word += '_'
    return guessed_word

def get_available_letters(letters_guessed):
	
	global LETTERS
	if len(letters_guessed) >= 1:
		LETTERS = LETTERS.replace(letters_guessed[-1],'')
	return LETTERS

def display_hangman(remaining_lives, letters_guessed):
	print(IMAGES[7 - remaining_lives])

def hangman(secret_word):
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
			print("\tGame over!!\n"+"_"*150)
			print("\n\tThe word was: {}".format(secret_word))
			break
#Load the list of words into the variable wordlist
#So that it can be accessed from anywhere in the program

if __name__ == '__main__':
	secret_word = choose_word()
	hangman(secret_word)

