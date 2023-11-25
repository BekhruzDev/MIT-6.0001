# Problem Set 4A
# Name: <Bekhruz Abdullkahujaev>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. 
    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    #Assume that it is a non-empty string.  
    assert not len(sequence) == 0
    
    #base case: when we have length = 1 sequence
    if len(sequence) == 1:
        #return singleton list containing that sequence
        return [sequence]
    #letter index, currently index of the first letter
    index = 0
    #if len(sequence) > 1, then do the same get_permutations() without the first_letter
    return reorder_wordlist(sequence[0], get_permutations(sequence[index+1::]))
    
    
    
def reorder_wordlist(first_letter, permutated_words_list):
    '''
    Permutates all sequence elements of the list with the given letter
    
    first_letter (character): the character to be place into all indices of the sequence
    
    permutated_words_list (list<string>): list of elements to be permutated
    
    Returns list of all permutations of all sequence elements combined with first_letter 
    '''
    result_list = []
    # every element in the permutated_words_list
    for word in permutated_words_list:
        # extend list with all possible permutations of word with first letter
        result_list.extend(reorder_word(first_letter, word))
    return result_list


def reorder_word(letter, word):
    '''
    Permutates word by combining it with the letter
    
    letter(char): letter to combine
    
    word(string): word to permutate
    
    Returns list of all possible permutations of the word with the letter
    
    Example: letter = 'b' and word = "ust"
    then reorder_word gives us: "bust", "ubst", "usbt", "ustb"; 

    '''
    # save all reordered words
    reordered_words = []
    
    for index in range(len(word) + 1):
            # get word as a list of chars
            chars_list = list(word)
            # insert the letter into specific consequent indices
            chars_list.insert(index, letter)
            # add the resulting chars_list as a string into reordered_words
            reordered_words.append("".join(chars_list))
            # clear chars_list to prepare for the next permutation
            chars_list.clear()
    return reordered_words
    

    

#TESTS
if __name__ == '__main__':
    
    # Check if Expected and Actual outputs are True 
    def check_equality(actual, expected):
        return sorted(actual) == sorted(expected)
    
    sample_inputs_list = ['abc', 'xdz', 'ej', 'o', 'okay'] 
    expected_output0 = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    expected_output1 = ['xdz', 'xzd', 'dxz', 'dzx', 'zxd', 'zdx']
    expected_output2 = ['ej', 'je']
    expected_output3 = ['o']
    expected_output4 = ["okay", "okya", "oaky", "oayk", "oyka", "oyak", "koya", "kayo", 
                        "koay", "kaoy", "kyoa", "kyao", "aoky", "aoyk", "akoy", "akyo", 
                        "ayok", "ayko", "yoka", "yoak", "ykao", "ykoa", "yaok", "yako"]
    
    expected_outputs_list = [expected_output0, expected_output1, expected_output2, expected_output3, expected_output4]
  
  
    for i in range(5):
        print("\n===========================")
        print("TEST:", i)
        print("===========================\n")
        sample_input = sample_inputs_list[i]
        expected_output = expected_outputs_list[i]
        actual_output = get_permutations(sample_input)
        print('Input:', sample_input)
        print('Expected Output:', expected_output)
        print('Actual Output:', actual_output)
        print("Are the outputs equal to each other:", check_equality(actual_output, expected_output))

    
    
 
    
    
    


    
