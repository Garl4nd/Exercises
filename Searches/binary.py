def find(ar,val):
    l,u=0,len(ar)-1

    while l<=u:
        m=l+(u-l)//2
        if ar[m]<val:
            l=m+1
        elif ar[m]==val:
            return m
        else:
            u=m-1
    return -1

def find_first(ar,val):
    l,u=0,len(ar)-1

    while l<=u:
        m=l+(u-l)//2
        if ar[m]<val:
            l=m+1
        elif ar[m]==val:
            u=m
            while ar[l]!=val:
                m=l+(u-l)//2
                if ar[m]!=val:
                    l=m+1
                else:
                    u=m
            return l
        else:
            u=m-1
    return -1

ar=[1,5,8,9,23,49]
print(ar[find(ar,4)])
x=[1,3, 5,5,5,5,5,4,444,2,3,5,7]
print(find_first(x,5))
