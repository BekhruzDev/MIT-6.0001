def fibonacci1(n):
    '''
    n:int, n-th fibonacci number, assume n >= 0
    Returns the n-th fibonacci number
    
    This version of fibonacci algorithm is O(2^n).
    Because, in every recursive call, the algorithm returns 2 more recursive function calls
    
    '''
    assert n >= 0
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci1(n-1) + fibonacci1(n-2)



#Test
n = 12
for i in range(n):
    print(i+1,"- th fibonacci:", fibonacci1(i))