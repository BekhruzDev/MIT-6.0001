# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"
VOWELS = ['a', 'o', 'i', 'u', 'e']


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    sorted_secret_letters = sorted(list(secret_word))
    sorted_guess_letters = sorted(letters_guessed)
    return sorted_secret_letters == sorted_guess_letters


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_so_far = ''
    for secret_letter in secret_word:
        if(secret_letter in letters_guessed):
            guessed_so_far += secret_letter
        else:
            guessed_so_far += "_ "

    return ''.join(guessed_so_far)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    import string
    all_letters = list(string.ascii_lowercase)
    for l in letters_guessed:
        all_letters.remove(l)
    return ''.join(all_letters)


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_left = 6
    warnings_left = 3
    while (guesses_left <= 6):
        print("You have", guesses_left, "guesses left")
        print("Available letters:", get_available_letters(letters_guessed))
        input_guess = input("Please guess a letter: ")
        if input_guess.isalpha() and input_guess not in letters_guessed:
            valid_input_guess = input_guess.lower()
            letters_guessed.append(valid_input_guess)
            if(valid_input_guess in secret_word):
                if valid_input_guess not in unique_letters:
                    unique_letters.append(valid_input_guess)
                print("Good guess:", get_guessed_word(secret_word, letters_guessed) )
                if (get_guessed_word(secret_word, letters_guessed) == secret_word):
                    print('Congratulations, you won!')
                    print('Your total score for this game is:', guesses_left * len(unique_letters))
                    break
            else:
                if valid_input_guess in VOWELS:
                    guesses_left -= 2
                else: 
                    guesses_left -= 1
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                
        else: 
            warnings_left -= 1
            if warnings_left == 0:
                warnings_left = 3
                guesses_left -= 1
            elif input_guess in letters_guessed:
                print("Oops! You have already entered the letter", input_guess, ".  You have", warnings_left, "warnings left:", get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! That is not a valid letter. You have", warnings_left, "warnings left:", get_guessed_word(secret_word, letters_guessed))
        if guesses_left == 0:
            print('Sorry, you ran out of guesses. The word was', secret_word)
            break
        print("-------------  ")
    

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    is_match = True
    my_word_without_space = ''.join(my_word.split())
    abc_list = list(string.ascii_lowercase)
    available_letters = [item for item in abc_list if item not in my_word_without_space]
    if len(my_word_without_space) != len(other_word): 
       return False
    for index in range(len(my_word_without_space)):
        if not is_match:
            return is_match
        my_letter = my_word_without_space[index]
        other_letter = other_word[index]
        if my_letter.isalpha():
            is_match = is_match and my_letter == other_letter
        else:
            is_match = is_match and other_letter in available_letters
    return is_match
        


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
              Keep in mind that in hangman when a letter is guessed, all the positions
              at which that letter occurs in the secret word are revealed.
              Therefore, the hidden letter(_ ) cannot be one of the letters in the word
              that has already been revealed.

    '''
    possible_matches = [item for item in wordlist if match_with_gaps(my_word, item)]
    if len(possible_matches) == 0:
        print("No matches found")
        return
    print(" ".join(possible_matches))
    


def hangman_with_hints(secret_word):
    attempts = 0
    guesses_left = 6
    warnings_left = 3
        
    print("Welcome to the game Hangman! ")
    print("I am thinking of a word that is", len(
        secret_word), "letters long.  ")
    print("The secret word is", secret_word)
    print("-------------  ")
    
    while (guesses_left <= 6):
      
        attempts += 1
        print("You have", guesses_left, "guesses left")
        print("Available letters:", get_available_letters(letters_guessed))
        input_guess = input("Please guess a letter: ")
      
        if input_guess.isalpha() and input_guess not in letters_guessed:
            valid_input_guess = input_guess.lower()
            letters_guessed.append(valid_input_guess)
          
            if(valid_input_guess in secret_word):
                if valid_input_guess not in unique_letters:
                    unique_letters.append(valid_input_guess)
                print("Good guess:", get_guessed_word(secret_word, letters_guessed) )
                if (get_guessed_word(secret_word, letters_guessed) == secret_word):
                    print('Congratulations, you won!')
                    print('Your total score for this game is:', guesses_left * len(unique_letters))
                    break
            else:
                if valid_input_guess in VOWELS:
                    guesses_left -= 2
                else: 
                    guesses_left -= 1
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
         
        elif input_guess == "*" and len(get_available_letters(letters_guessed))<26:
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
    
        else: 
            warnings_left -= 1
            if warnings_left == 0:
                warnings_left = 3
                guesses_left -= 1
            elif input_guess in letters_guessed:
                print("Oops! You have already entered the letter", input_guess, ".  You have", warnings_left, "warnings left:", get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! That is not a valid letter. You have", warnings_left, "warnings left:", get_guessed_word(secret_word, letters_guessed))
  
        if guesses_left == 0:
            print('Sorry, you ran out of guesses. The word was', secret_word)
            break
        print("-------------  ")

wordlist = load_words()
secret_word = choose_word(wordlist)
letters_guessed = []
unique_letters = []
hangman_with_hints(secret_word)



