def selection_sort(list):
    '''
    1. Extract minimum element. Swap it with the element at index 0
    2. In the remaining sublist, extract minimum element, swap it with element at index 1
    3. Keep the left portion of the list sorted
         3.1 At i'th step, first i elements in the list are sorted
         3.2 All other elements are bigger
    Time Complexity: n - 1 comparisons in each of n passes, that is O(n^2), quadratic 
    
    NOTE: Unlike bubble_sort, even if the list is sorted after some number of passes, 
    the selection_sort goes through all passes which is n.
    '''
    suffix_start = 0
    while suffix_start<len(list):
        print("Pass No", suffix_start+1, "List:", list)
        for i in range(suffix_start, len(list)):
            if list[suffix_start] > list[i]:
                list[suffix_start], list[i] = list[i], list[suffix_start]
        suffix_start += 1
    return list

#TEST
list_sample = [2,6,8,1,6,4,32,0]
print("List size:", len(list_sample))
print(selection_sort(list_sample))