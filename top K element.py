import random
def partition(L, v):
    smaller=[]
    bigger=[]
    for val in L:
        if val < v:
            smaller.append(val)
            
        elif val > v:
            bigger.append(val)
        
    return smaller,[v],bigger

def top_k(L,k):
    v=L[random.randrange(len(L))]
    (left,middle,right)=partition(L, v)
    if len(left)==k: return left
    if len(left)==k+1: return left+middle
    if len(left)>k: return top_k(left,k)
    return left+middle+top_k((right),k-len(left)-1)
L=[31,45,91,51,66,82,28,33,11,89,84,27,36]
print(top_k(L,2))    
