def quicksort(ar):
    def _quicksort(ar,lb,ub):
        if lb>=ub:
            return 
        piv_ind=rearange(ar,lb,ub)
        _quicksort(ar,lb,piv_ind)
        _quicksort(ar,piv_ind+1,ub)
    _quicksort(ar,0,len(ar))
    
def rearange(ar,lb,ub):
        pivot=ar[lb]
        lowloc=lb
        for i in range(lb+1,ub):
            if ar[i]<pivot:
                lowloc+=1
                ar[lowloc],ar[i]=ar[i],ar[lowloc]
                
                
            #print(ar)
        ar[lowloc],ar[lb]=ar[lb],ar[lowloc]
        return lowloc


ar=[2,1,0,8,9,5]
quicksort(ar)
print(ar)