import random
def minimize_absolute(L):
    f=len(L)//2
    if len(L) % 2==1:
        
        return 1.0*top_k(L,f)
        
    if len(L) % 2==0:
           
        return 1.0*(top_k(L,f-1)+top_k(L,f))/2
   
        
        

def partition(L, v):
    smaller=[]
    bigger=[]
    middle=[]
    for val in L:
        if val < v:
            smaller.append(val)
            
        if val > v:
            bigger.append(val)
        if val==v:
            middle.append(val) 
    return smaller,middle,bigger

def top_k(L,k):
    v=L[random.randrange(len(L))]
    (left,middle,right)=partition(L, v)
    if len(left)>k:
        return top_k(left,k)  
    elif len(left)+len(middle)>k: return middle[0]
    
        
    return top_k(right,k-len(left)-len(middle))
    


    
L=[5, 5, 4, 5,8,10,13,18]
print(minimize_absolute(L))
