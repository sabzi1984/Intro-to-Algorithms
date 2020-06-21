def rank(L,v):
    pos=0
    for val in L:
        if val<v:
            pos+=1
    return pos
L=[31,45,91,51,66,82,28,33,11,89,84,27,36]
print(rank(L,84))
