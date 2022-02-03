def find_kth(ar,k):
    l,u=0,len(ar)
    k=k-1
    while u!=k:
        piv=rearange(ar,l,u)
        if piv<k:
            l=piv+1
        else:
            u=piv


    return ar[u]
    
def rearange(ar,l,u):
    val=ar[l]
    pivind=l
    for i in range(l+1,u):
        
        if ar[i]>=val:
            pivind+=1
            ar[i],ar[pivind]=ar[pivind],ar[i]
            
    ar[l],ar[pivind]=ar[pivind],ar[l]
  
    return pivind

refar=[1,2,3,4,8,9,12,25]
ar=[2,3,8,1,9,4,25,12]
print(find_kth(ar,3))