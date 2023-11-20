# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <Bekhruz>
# Collaborators : <No collaborators>
# Time spent    : <Started at: 11.01, Ended at ,,,>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = 'L:\\MIT 6.0001\\Problem Sets\\ProblemSet3\\words.txt'


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    word_lowercase = word.lower()
    first_component = 0
    for i in word_lowercase:
        if i != "*":   
            first_component += SCRABBLE_LETTER_VALUES[i]
    wordlen = len(word_lowercase)
    second_component = max((7 * wordlen - 3 * (n - wordlen)), 1)
    return first_component * second_component


#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    print()                              # print an empty line
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels - 1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    hand['*'] = 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    hand_copy = hand.copy()
    for letter in word.lower():
        hand_copy[letter] = hand_copy.get(letter, 0) - 1
        if(hand_copy[letter] <= 0):
            del hand_copy[letter]
    return hand_copy

#
# Problem #3: Test word validity
#

 
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    is_valid = False
    word_lower = word.lower()
    freqs = get_frequency_dict(word_lower)
    hand_copy = hand.copy()
    word_copy = word_lower
    vowels_left = []
    for v in VOWELS:
        if v not in hand_copy.keys():
            vowels_left += v
    if "*" in word:
        for v in vowels_left:
           word_copy = word_lower.replace("*", v)
           if word_copy not in word_list:
             continue
           for l in word_copy:
                 if is_valid:
                  return True
                 is_valid = is_valid or get_frequency_dict(word_copy)[l] <= hand_copy.get(l, 0)
    else:
           is_valid = True
           if word_copy not in word_list:
               return False
           for l in word_copy:
                 if not is_valid:
                    return False
                 is_valid = is_valid and get_frequency_dict(word_copy)[l] <= hand_copy.get(l, 0)                 
    return is_valid
  

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    # get the list of values of hand
    length_list = hand.values()
    # interate through the list and calculate the sum of value items
    sum = 0
    for len in length_list:
        sum += len
    return sum

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed. display_hand(hand)
    
    * The user may input a word. get user input

    * When any word is entered (valid or invalid), it uses up letters update_hand(hand, word)
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.                                if invalid, ask for another word

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    

    # Keep track of the total score
    total_score = 0
    
    # As long as there are still letters left in the hand:
    while len(hand.keys()) > 0:
        
    
        # Display the hand
        display_hand(hand)
        
        # Ask user for input
        user_input_word = input("Enter word, or '!!' to indicate that you are finished: ")
        
        # If the input is two exclamation points:
        if user_input_word == "!!":
            # End the game (break out of the loop)
            break

            
        # Otherwise (the input is not two exclamation points):
        else:
            # If the word is valid:
            if is_valid_word(user_input_word, hand, word_list):

                # Tell the user how many points the word earned,
                # and the updated total score
                word_score = get_word_score(user_input_word, len(hand.keys()))
                total_score += word_score
                print(user_input_word, "earned", word_score, "points. Total:", total_score, "points")
            
            # Otherwise (the word is not valid):
                # Reject invalid word (print a message)
            else:
                print("That is not a valid word. Please choose another word.")
            
            # update the user's hand by removing the letters of their inputted word
            hand = update_hand(hand, user_input_word)  
            
            

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    print("Total score for this hand:", total_score, "points")

    # Return the total score as result of function
    return total_score



#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    #variables: input_letter:string, all_letters, letters_left, random_letter
    
    #1. ask user for the letter in hand to substitute
    input_letter = letter
    #3. get all alphabet letters both VOWELS and CONSONANTS
    all_letters = list(VOWELS + CONSONANTS)
    #4. subtract hand's keys from all letters
    letters_left = [item for item in all_letters if item not in hand.keys()]
    #5. get random letter from the letters_left
    random_letter = random.choice(letters_left)
    #6. add that random_letter as a new element to the hand, equalling it to the value of the letter the user has chosen to substitute
    hand[random_letter] = hand[input_letter]
    #7. delete the key representing that letter from the hand
    del hand[input_letter]
    #8. return the changed hand
    return hand
    
   
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands
  
    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
    total_score = 0
    has_replayed = False
    # ask for total number of hands
    total_hands = int(input("Enter total number of hands: "))
    total_hands_const = total_hands
    random_hand = {}
    
    print("\n======================================")
    print("Game Started ")
    print("======================================\n")
    
    # while number of hands is greater than 0:
    while total_hands > 0:
        has_substituted = False
    #   keep track of every hand score, has_substituted, has_replayed
        previous_hand = random_hand
    #   generate random_hand
        random_hand = deal_hand(HAND_SIZE)
    #   display the current hand before every attempt
        display_hand(random_hand)
        
    #   if it is the second or higher hand and has_replayed = false: 
        if total_hands_const - total_hands > 0 and has_replayed == False :
    #       ask if to replay the previous hand:
            wanna_replay = input("Would you like to replay the hand? ")
    #       if yes -> has_replayed = true, has_substituted = true and replay_score = play_hand(previous hand)
            if wanna_replay in ["Y", "Yes", "y", "yes" ]:
                has_replayed = True
    #           once replay option is selected, user cannot substitute option
                has_substituted = True
    #           before adding a new hand score, subtract the score of previous attempt from the total_score
                total_score -= hand_score
                replay_score = play_hand(previous_hand, word_list)
    #           only maximum score is accounted if replayed
                hand_score = max(replay_score, hand_score)  
    #           replaying does not cost hand
                total_hands += 1 
                
    #   if has_substituted == false
        if not has_substituted:
    #       ask if to substitute a letter
            wanna_substitute = input("Would you like to substitute a letter? ")
    #       if yes -> substitute and hand_score = play_hand()
            if wanna_substitute in ["Y", "Yes", "y", "yes" ]:
                input_letter = input("Which letter would you like to replace: ")
                new_hand = substitute_hand(random_hand, input_letter)
                hand_score = play_hand(new_hand, word_list)
            else: 
    #           play the given random hand
                hand_score = play_hand(random_hand, word_list)
        total_hands -= 1
    #   update the total_score at the end of every hand
        total_score += hand_score
        print("\n********************************************")
    print("\n==========================================")
    print("GAME OVER!")
    print("Total score over all hands: ", total_score)
    print("==========================================\n")
        
        
        
   
 
        


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
