def Mode(L):
    counts={}
    max_counts=0
    mode=None
    for val in L:
        if val not in counts:
            counts[val]=1
        else:
            counts[val]+=1
            if counts[val]>max_counts:
                max_counts=counts[val]
                mode=val
    return mode
L=[31,45,91,51,66,82,28,33,11,89,84,27,36,54,31,11,11]
print(Mode(L))
