import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7


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
                 is_valid = is_valid or freqs[l] <= hand_copy.get(l, 0)
    else:
           is_valid = True
           if word_copy not in word_list:
               return False
           for l in word_copy:
                 if not is_valid:
                    return False
                 is_valid = is_valid and get_frequency_dict(word_copy)[l] <= hand_copy.get(l, 0)
                 print(l,"->",is_valid)
                 
    return is_valid

def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    #1. get the list of values of hand
    length_list = hand.values()
    #2. interate through the list and calculate the sum of value items
    sum = 0
    for len in length_list:
        sum += len
    return sum

word_list = ["hello", "how", "are", "you", "reciprocation"]
hand = {"h":1, "e":2, "l":2, "*":1, "y": 2, "u":1, "w":2}
word = "h*z"

print (calculate_handlen(hand))
#print("is "+ word + " valid: "+ str(is_valid_word(word, hand, word_list)))
