# Problem Set 4B
# Name: Bekhruz Abdullakhujaev
# Collaborators:
# Time Spent: x:xx

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("ProblemSet4\story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = "L:\MIT 6.0001\Problem Sets\ProblemSet4\words.txt"

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        lower = list(string.ascii_lowercase)
        map = {}
        for i in range(26):
            letter = lower[i]
            map[letter] = lower[(i + shift) % 26]
            map[letter.upper()] = lower[(i + shift) % 26].upper()
        return map
        

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        cipher_text = ""
        map = self.build_shift_dict(shift)
        for l in self.message_text:
            if l not in string.ascii_letters:
                cipher_text = cipher_text + l
            else:
                cipher_text = cipher_text + map[l]
        return cipher_text
            
        

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)
    

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.__init__(self.message_text, self.shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        
        

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
                
        # keep dict of (shift:list<valid words>)
        dict = {}
        # most valid words list
        max_valid = []
        # key of the most valid words list
        max_valid_key = 0 
        letters_count = 26
       
        # iterate in range(26) shifting by 26-s.
        for s in range(letters_count): 
            sequence = self.apply_shift((26 - s) % 26)
            for word in sequence.split():
                if is_word(self.valid_words, word):
                    if s not in dict.keys():
                        dict[s] = []
                    dict[s].append(word)
       
        # get the dict values that has the most valid words
        for k in dict:
            if len(dict[k]) > len(max_valid):
                # assign the max_valid to the dict value (list) that has max number of elements
                max_valid = dict[k]
                max_valid_key = k
       
        # return tuple of shift having most valid words and those most valid words
        max_valid_shift = letters_count - max_valid_key
        return (max_valid_shift, " ".join(max_valid))
	
        
        

if __name__ == '__main__':

   #Example test cases for PlaintextMessage
   print("\n================================\n")
   plaintext = PlaintextMessage('hello', 2)
   print('Expected Output: jgnnq')
   print('Actual Output:', plaintext.get_message_text_encrypted())
   
   print("\n================================\n")
   plaintext = PlaintextMessage('are u ok?', 25)
   print('Expected Output: zqd t nj?')
   print('Actual Output:', plaintext.get_message_text_encrypted())
   
   
   

   #Example test cases for CiphertextMessage
   print("\n================================\n")
   ciphertext = CiphertextMessage('jgnnq')
   print('Expected Output:', (24, 'hello'))
   print('Actual Output:', ciphertext.decrypt_message())
   
   print("\n================================\n")
   ciphertext1 = CiphertextMessage('zqd xnt ehmd?')
   print('Expected Output:', (1, 'are you fine?'))
   print('Actual Output:', ciphertext1.decrypt_message())


   #: best shift value and unencrypted story
   print("\n================================\n")
   cipher_story = CiphertextMessage(get_story_string())
   decrypted_story = cipher_story.decrypt_message()
   print("Cipher shift of the story:", decrypted_story[0])
   print("\nEnjoy reading the story!\n")
   print(decrypted_story[1])
    
    
    