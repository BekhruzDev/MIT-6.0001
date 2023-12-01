def merge_sort(list):
    '''
    1. If len(L) == 0 or 1, then already sorted
    2. if len(L) > 1, then split into 2 lists and merge_sort(each list)
    3. Merge sorted sublists
   
    Time Complexity: since we are halving the whole list at each step, 
    we will have logn steps, in each of which we merge 2 sublist that costs n. 
    Overall, it will be O(nlogn), which is loglinear.
    NOTE: For sorting large lists, merge_sort is good
    '''
    if len(list) == 0 or len(list) == 1:
        return list
    if len(list) > 1:
        middle = len(list) // 2
        left_list =  merge_sort(list[:middle])
        right_list = merge_sort(list[middle:])
        return merge_lists(left_list, right_list)
    
    

def merge_lists(left_list, right_list):
    '''
    Merges sorted sublists
    1. Look at the first element of each sublist, move smaller one to the end of the result
    2. When one list is empty, just copy the rest of the elements in the other list
    Time Complexity: due to comparing and copying list elements to the result list, overall O(n) + O(n) = O(n) which is linear
    '''
   
    result = []
    i, j = 0,0
    #when there are elements in both lists
    while i < len(left_list) and j < len(right_list):
        if left_list[i] > right_list[j]:
            result.append(right_list[j])
            j += 1
        else: 
            result.append(left_list[i])
            i += 1
    
    #when no elements left in the right list
    while i < len(left_list):
        result.append(left_list[i])
        i += 1
            
    #when no elements left in the left list
    while j < len(right_list):
        result.append(right_list[j])
        j += 1
    return result
            
#TEST
print("Test merge_list:")
list1 = [1,2,5,9,14,23,52,63]
list2 = [2,15,22,45,57,85,92,100]
print(merge_lists(list1, list2))
print("====================\n")

print("Test merge_sort:")
list = [2,1,15,22,45,57,2,5,9,23,85,92,100,0,52]
print(merge_sort(list))

    