#move function
def move(fr, to):
    print("Move from", str(fr), "to", str(to))
    
    
#towers_of_hanoi recursion
def towers_of_hanoi(n, p1, p2, p3):
    '''
    Moves n number of disks from Peg 1 to Peg 2 using Peg 3. Can move only one disk at a time. 
    
    n: number of disks on Peg1
    p1, p2, p3: Peg 1, Peg 2, Peg3
    
    Returns nothing but print statements describing the movements
    
    NOTE: This problem is O(2^n) and grows exponential 
    since each recursion call invokes more than one call of the same type.
    '''
    if n == 1:
        move(p1, p2)
        return
    else:
        # the same problem with a smaller size
        towers_of_hanoi(n - 1, p1, p3, p2)
        towers_of_hanoi(1, p1, p2, p3)
        # the same problem with a smaller size
        towers_of_hanoi(n - 1, p3, p2, p1)


#Test
towers_of_hanoi(44, "P1", "P2", "P3")
    