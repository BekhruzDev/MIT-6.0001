def get_power_sets(n):
    '''
    n: Int, 
    Returns list of power sets from 1 to n
    
    NOTE: This problem is O(2^n), which is exponential since we get e.g. 4 sets for n=2, 8 sets for n=3 and so on...
    '''
    
    if n == 0:
        return [[],]
    old_power_set = get_power_sets(n - 1)
    new_power_set = []
    for i in old_power_set:
        # combine each list (set) of old_power_set with singleton list of n, and append the result
        # to the new_power_set
        new_power_set.append(i + [n])
    return old_power_set + new_power_set

#Test
print(get_power_sets(44))