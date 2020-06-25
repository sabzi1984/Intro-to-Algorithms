def parent(i): 
    return (i-1)/2
def left_child(i): 
    return 2*i+1
def right_child(i): 
    return 2*i+2
def is_leaf(L,i): 
    return (left_child(i) >= len(L)) and (right_child(i) >= len(L))
def one_child(L,i): 
    return (left_child(i) < len(L)) and (right_child(i) >= len(L))


def down_heapify(L, i):
    
    if is_leaf(L, i): 
        return
    if one_child(L, i):
        if L[i] > L[left_child(i)]:
            (L[i], L[left_child(i)]) = (L[left_child(i)], L[i])
        return
   
    if min(L[left_child(i)], L[right_child(i)]) >= L[i]: 
        return
   
    if L[left_child(i)] < L[right_child(i)]:
        (L[i], L[left_child(i)]) = (L[left_child(i)], L[i])
        down_heapify(L, left_child(i))
        return
    else:
        (L[i], L[right_child(i)]) = (L[right_child(i)], L[i])
        down_heapify(L, right_child(i))
        return
    
def build_heap(L):
    for i in range(len(L)-1, -1, -1):
        down_heapify(L, i)
    return L


L = list(range(10))
print(build_heap(L))
