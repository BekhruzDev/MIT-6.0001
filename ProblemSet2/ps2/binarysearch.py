# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 10:03:53 2023

@author: mrabd
"""


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    import string
    import math

    all_letters = list(string.ascii_lowercase)
    letters_left_reversed = []
    low = 0
    high = len(all_letters)
    times = 0
    for l in letters_guessed:

    while(times <= math.log2(len(all_letters))):
        mid = (low + high) / 2
        if all_letters[mid] ==

    # for l in letters_guessed:
    #     all_letters.remove(l)
    # return ''.join(all_letters)


letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
print(get_available_letters(letters_guessed))
