def delete_dups1(ar): #O(n^2)
    non_empty=len(ar)
    for i in range(len(ar)):
        x=ar[i]
        j=i+1
        while j<non_empty:
            if ar[j]==x:
                non_empty-=1
                ar[j],ar[non_empty]=ar[non_empty],None
                
            else:
                j+=1
def delete_dups2(ar): #O=O(sort)+O(n)
    proper_ind=0
    ar.sort()
    last_val=ar[0]
    for i in range(1,len(ar)):
        if ar[i]==last_val:
            ar[i]=None
        else:
            last_val=ar[i]
            proper_ind+=1
            ar[i],ar[proper_ind]=ar[proper_ind],ar[i]
def delete_val(ar,val):
    i=0
    shift=0
    while i<len(ar):
        if ar[i]==val:
            shift+=1
        else:
            ar[i-shift]=ar[i]
        if i+shift>=len(ar):
            ar[i]=None
        i+=1
        
ar=[1,4,5,6,1,2,4,5,5,7,8]
print(set(ar))
delete_dups2(ar)
print(ar)
ar=[1,2,3,1,2,4,5]
delete_val(ar,1)
print(ar)