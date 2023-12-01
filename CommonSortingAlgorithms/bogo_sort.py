def bogo_sort(list):
    '''
    This sorting technique is also called monkey sort, stupid sort, permutation sort.
    Throws away a deck of n cards and collect them randomly. Checks if it is sorted, if not then repeat again.
    Time complexity is actually O(n!) but in real life a person may never sort the list
    '''
    
    # take the list
    # shuffle the list
    # see if it is sorted
    import random

    shuffle = True
    while shuffle:
        print("List:", list)
        shuffle = not is_sorted(list)
        if shuffle:
            random.shuffle(list)
    print("Sorted List:", list)
    
def is_sorted(list):
    is_sorted = True
    for i in range(1, len(list)):
        is_sorted = is_sorted and list[i - 1] <= list[i]
    return is_sorted
        
        

#TEST            
list_sample = [2,6,8,1,6,4,32]
print("List size:", len(list_sample))
print(bogo_sort(list_sample))
    
        
                        
                
            
        