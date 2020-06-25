def up_heapify(L, i):
    if i==0:
        return          
    if L[i] < L[parent(i)]:
        (L[i], L[parent(i)]) = (L[parent(i)], L[i])
        up_heapify(L, parent(i))
    return L 
def parent(i): 
    return (i-1)//2

L = [2, 4, 3, 5, 9, 7, 7]
L.append(1)
print(up_heapify(L, 7))
