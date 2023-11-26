def bisection_search1(list, e):
    '''
    Assume that list is sorted
    Uses bisection search method to search for the element in the list
    
    list: List of sorted elements
    e: element to search in the list
    
    Returns True if e exists in the list, else False
    
    NOTE:
    This version of bisection_search is actually O(n*logn) but...
    logn -> we need logn steps (divisions by 2) to reach the solution
    n -> we copy HALF of the elements every time we call the function recursively
    
    Hence, this version if bisection_search is generally O(n) since it dominates the logn cost 
    '''
    if len(list) == 0:
        return False
    if len(list) == 1:
        return list[0] == e
    mid = len(list)//2
    if list[mid] == e:
        return True
    if list[mid] > e:
        return bisection_search1(list[:mid], e)
    else:
        return bisection_search1(list[mid:], e)
    
#Test

sample_list = [1,2,3,4,5,6,7,8,9,10,13,16,45]
element_to_search = 16
print(bisection_search1(sample_list, element_to_search))
        
    