def bubble_sort(list):
    '''
    1. Compare consecutive pairs of elements
    2. Swap elements in pair such that smaller is first
    3. When reach end of the list, start over again
    4. Stop when no more swaps have been made
    Note: The largest unsorted element is always at the end, so at most n passes. 
    The worst case happens when the input list is revesely sorted. 
    
    Time complexity = (n - 1) comparisons in each of (n - 1) passes, that is O(n^2), quadratic
    '''
    swap = True
    passes = 0
    while swap:
        swap = False
        passes += 1
        print("Pass", passes, "List:", list)
        for i in range(1, len(list)):
            if list[i - 1] > list[i]:
                swap = True
                list[i - 1], list[i] = list[i], list[i - 1]
       
    return list


#TEST
list_sample = [2,6,8,1,6,4,32,0]
print("List size:", len(list_sample))
print(bubble_sort(list_sample))
    