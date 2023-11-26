def fibonacci2(n):
    '''
    n:int, n-th fibonacci number, assume n >= 0
    Returns the n-th fibonacci number
    
    This version of fibonacci algorithm is O(n).
    Because, it reaches the solution just by looping through the n elements 
    unlike fibonacci1.py which is recursive.
    '''
    assert n >= 0
   
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    first = 0
    second = 1
    # Loop through range(n-1) not n. Because, for n >= 2, ith fibonacci actually outputs the value of (i+1)th fibonacci
    for i in range(n - 1):
        temp = first
        first = second
        second = temp + first
    return second


#Test
n = 20
for i in range(n):
    print(i+1,"- th fibonacci:", fibonacci2(i))
