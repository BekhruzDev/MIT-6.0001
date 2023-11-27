#move function
def move(fr, to):
    print("Move from", str(fr), "to", str(to))
    
    
#towers_of_hanoi recursion
def towers_of_hanoi(n, p1, p2, p3):
    if n == 1:
        move(p1, p2)
        return
    else:
        towers_of_hanoi(n - 1, p1, p3, p2)
        towers_of_hanoi(1, p1, p2, p3)
        towers_of_hanoi(n - 1, p3, p2, p1)

towers_of_hanoi(3, "P1", "P2", "P3")
    