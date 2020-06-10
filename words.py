import random


def load_words():
    word_list = ["learning", "kindness", "joy", "kiet", "good"]
    
    WORDLIST_FILENAME = "words.txt"
    inFile = open(WORDLIST_FILENAME, 'r')
    for line in inFile:
    	for word in line.split():
    	    word_list.append(word)
    return word_list
	
	
def choose_word():
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()
    return secret_word
    
