
def get_permutations2(sequence):
    '''
    This problem is a shorter version of get_permutations1.py
    
    sequence: string of characters
    
    Returns list of reorderings of the string
    
    For example, given 'abc', it returns 'abc', 'acb', 'bac', 'bca', 'cab', 'cba'
    
    NOTE: This problem is O(n!) since it does n * (n - 1) * (n - 2) * (n - 3) * ... * 3 * 2 * 1 operations
    ''' 
    #Hint: In recursion problems, we should think about solving the same problem with a smaller size. 
    #So, get the first character and apply it into different indices of the each permutations of the rest of the characters

    if len(sequence) == 0 or len(sequence) == 1:
        return [sequence]
    else: 
        result_list = []
        for perm in get_permutations2(sequence[1:]):
            for i in range(len(sequence)):
                result_list.append(''.join(perm[:i] + sequence[0] + perm[i:]))
        return result_list
    
#Test
print(get_permutations2('abc'))
    