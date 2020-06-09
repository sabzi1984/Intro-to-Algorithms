def russian_peasant(a,b):
    z=0
    while a>0:
        if a%2==1: z=z+b
        a,b=a>>1,b<<1
    return z
print(russian_peasant(2578,3125))
