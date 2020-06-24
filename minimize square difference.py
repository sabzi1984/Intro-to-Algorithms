def minimize_square(L):
    x = 0
    for val in L:
        x+=val
    x=1.0*x/(len(L))
    return x
