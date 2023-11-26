def bisection_search(list, e):
    '''
    Assume that list is sorted
    '''
    if len(list) == 0:
        return False
    if len(list) == 1:
        return list[0] == e
    mid = len(list)//2
    if list[mid] == e:
        return True
    if list[mid] > e:
        return bisection_search(list[:mid], e)
    else:
        return bisection_search(list[mid:], e)
    
#Test

sample_list = [1,2,3,4,5,6,7,8,9,10,13,16,45]
element_to_search = 16
print(bisection_search(sample_list, element_to_search))
        
    