import numpy as np

def find_first(ar,val):
    l,u=0,len(ar)-1
    minover=u
    while l<=u:
        if ar[u]>val:
            minover=u
        #print(ar,minover)
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
            return l,minover
        else:
            u=m-1
    return -1,minover

def search_2D(ar,val):
    maxind=ar.shape[1]-1
    for i in range(ar.shape[0]):
        #print(maxind)
        res,maxind=find_first(ar[i,:maxind+1],val)
        if res!=-1:
            return i,res
    return -1,-1

x=np.array([[1,4,9,15],[5,5,13,20],[6,7,24,35]])
print(x)
print(search_2D(x,5))

            