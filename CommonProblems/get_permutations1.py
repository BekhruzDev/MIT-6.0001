
def get_permutations(sequence):
    '''
    sequence: string of characters
    
    Returns list of reorderings of the string
    
    For example, given 'abc', it returns 'abc', 'acb', 'bac', 'bca', 'cab', 'cba'
    ''' 
    #Hint: In recursion problems, we should think about solving the same problem with a smaller size. 
    #So, get the first character and apply it into different indices of the each permutations of the rest of the characters
    if len(sequence) == 0:
        print("Please, provide non-empty string!")
    if len(sequence) == 1:
        return [sequence[0]] 
    return permutate_sequence(sequence[0], get_permutations(sequence[1:]))
    


#apply to the each indices of the given sequence
def apply_character(char, sequence):
    result_list = []
    for i in range(len(sequence) + 1):
        sub_list = list(sequence)
        sub_list.insert(i, char)
        result_list.append("".join(sub_list))
        sub_list.clear()
    return result_list	

#use apply_character() for every permutation from the list come out from the same problem with a smaller size (n - 1)	
def permutate_sequence(first_letter, permutations):
	result_list = []
	for sequence in permutations:
		result_list.extend(apply_character(first_letter, sequence))
	return result_list

print(get_permutations('bust'))