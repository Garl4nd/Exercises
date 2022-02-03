def alternate(ar):
    ar=list(ar)
    sign=1
    for i in range(len(ar)-1):
        sign*=-1
        if sign*ar[i]<sign*ar[i+1]:
            ar[i],ar[i+1]=ar[i+1],ar[i]
    return ar
    
def permute(ar,perm):
    
    for i in range(len(perm)):
        j=i
        temp=ar[i]    
        while perm[j]>=0:
            k=perm[j]
            temp,ar[k]=ar[k],temp
            perm[j]*=-1
            j=k

    perm[:]=[el*-1 for el in perm]
    return ar


def dictsuc(perm,inv=False):
    if inv:
        perm=[-el for el in perm]
    else:
        perm=list(perm)
    for i in reversed(list(range(1,len(perm)))):
            if perm[i]>perm[i-1]:
                perm[:i-1]=perm[:i-1]
                for k in reversed(range(i,len(perm))):
                    if perm[k]>perm[i-1]:

                        perm[i-1],perm[k]=perm[k],perm[i-1]
                        perm[i:]=list(reversed(perm[i:]))
                        break
                break
    else:
        return []
    if inv:
        return [-el for el in perm]
    else:
        return perm



perm=[1,2,3,4,5]
for i in range(120):
    print(perm,(perm:=dictsuc(perm)))
perm=[5,4,3,2,1]
for i in range(120):
    print(perm,(perm:=dictsuc(perm,inv=True)))