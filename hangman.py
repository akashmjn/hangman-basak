# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
import os

WORDLIST_FILENAME = os.path.join(os.getcwd(),"words.txt")

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "\n\nLoading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    return all([char in lettersGuessed for char in secretWord])

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    isLetterGuessed = [char in lettersGuessed for char in secretWord]
    output = ["_ " for char in secretWord]
    for i in range(len(secretWord)):
        if isLetterGuessed[i]:
            output[i]=secretWord[i]
    return "".join(output)

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    allLetters = [char for char in string.ascii_lowercase]
    output = [char for char in allLetters if char not in lettersGuessed]
    return "".join(output)

def invalidGuess(guess):
    '''
    invalidGuess(guess) -> True if invalid 
    '''
    if len(guess) > 1:
        print "Please enter a valid letter"
        return True
    elif guess in string.ascii_lowercase:
        return False 
    else: 
        print "Please enter a valid letter"
        return True    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, lets the user know how many 
      letters the secretWord contains.

    * Asks the user to supply one guess (i.e. letter) per round.

    * Displays feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, displays to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    '''
    roundCount = 7
    lettersGuessed = [] 

    def round(remGuess):
        """
        Advances a Hangman round forward, printing all required messages
        round(remGuess) -> True if remaining guesses to be reduced 
        """
        print "------------"
        print "You have %d guesses left." % remGuess
        print "Available letters: %s" % getAvailableLetters(lettersGuessed)
        #Taking input and checking validity. Repeat until valid input.
        guess = raw_input("Please guess a letter: ")
        guess = guess.lower()
        while invalidGuess(guess):
            guess = raw_input("Please guess a letter: ")   
        #Evaluating guesses    
        if guess in lettersGuessed:
            print "Oops! You've already guessed that letter: %s" \
            % getGuessedWord(secretWord,lettersGuessed)
            return False
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print "Good guess: %s" % getGuessedWord(secretWord,lettersGuessed)            
            return False
        else: 
            lettersGuessed.append(guess)
            print "Oops! That letter is not in my word: %s" \
            % getGuessedWord(secretWord,lettersGuessed)
            return True

    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is %d letters long." % len(secretWord)            

    while roundCount > 0:
        if isWordGuessed(secretWord,lettersGuessed):
            print "------------"
            print "Congratulations, you won!"
            break 
        else:    
            if round(roundCount): roundCount -= 1

    if roundCount == 0:
           print "------------"         
           print "Sorry, you ran out of guesses. The word was %s." % secretWord


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! 

wordlist = loadWords()
game = True
while game:
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)
    inp = raw_input('Play another game? (y/n): ')
    game = inp in ['y','Y']

