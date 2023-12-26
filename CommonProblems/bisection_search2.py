
def bisection_search2(list, x):
    '''
    Assume that list is sorted. 
    Uses bisection search method to search for the element in the list
    
    list: List of sorted elements
    e: element to search in the list
    
    Returns True if e exists in the list, else False
    
    NOTE: 
    This version of bisection_search is O(logn).
    Because we need logn steps to reach the solution and in every recursive call we are just passing
    the lowest and the highest values of list halves unlike bisection_search1.py in which we are copying 
    the half elements of the list, which is O(n), in every recursive call 
    '''
    
    def bisection_search_helper(list, x, low, high):
        if low == high:
            return list[low] == x
        mid = (low + high) // 2 #flooring
        if list[mid] == x:
            return True
        if list[mid] > x:
            if list[low] == list[mid]:
                return False #no elements left
            return bisection_search_helper(list, x, low, mid - 1)
        else:
            return bisection_search_helper(list, x, mid + 1, high)
    
    if len(list) == 0:
        return False
    return bisection_search_helper(list, x, 0, len(list) - 1)


#Test
sample_list = [1,2,3,4,5,6,7,8,9,10,13,16,45]
element_to_search = 7
print(bisection_search2(sample_list, element_to_search))
            