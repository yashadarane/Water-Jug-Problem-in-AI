visited={}
jug1,jug2,aim=4,3,2

def jugsolver(amt1,amt2):
    if amt1==aim:
        print(amt1,amt2)
        return True
    if (amt1,amt2) not in visited:
        print(amt1,amt2)
        visited[(amt1,amt2)]=True
        return jugsolver(0,amt2) or jugsolver(amt1,0) or jugsolver(jug1,amt2) or jugsolver(amt1,jug2) or jugsolver(amt1 + min(amt2, (jug1-amt1)), amt2 - min(amt2, (jug1-amt1)))
    else:
        return False

print("Steps: ")
jugsolver(0,0)
