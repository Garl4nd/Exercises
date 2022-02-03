def int_sr(n):
    l,u=0,n
    while l<=u:
        m=l+(u-l)//2
        if m**2<n:
            l=m+1
        elif m**2==n:
            return m
        else:
            u=m-1
    return l-1

def real_sr(x,tol=1.e-5):
    l,u=(1,x) if x>=1 else (x,1)
    m=l+(u-l)/2
    while abs(x-m**2)>tol:
        m=l+(u-l)/2
        if m**2<x:
            l=m
        elif m**2==x:
            return m
        else:
            u=m
    return m

print(int_sr(8))
print(real_sr(7))
