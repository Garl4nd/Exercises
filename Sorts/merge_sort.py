def merge_sort(ar):
    def _sort(i0,i1):
        if i1<=i0:
            return
        midpoint=i0+(i1-i0)//2
        _sort(i0,midpoint)
        _sort(midpoint+1,i1)
        _merge(i0,i1,midpoint)

    def _merge(i0,i1,midpoint):
        helper=[]
        i,j=i0,midpoint+1
        while i<=midpoint or j<=i1:
            #print(i)
            if j>i1 or i<=midpoint and ar[i]<ar[j]:
                helper.append(ar[i])
                i+=1
                
            else:
                helper.append(ar[j])
                j+=1
#        print(helper)
        ar[i0:i1+1]=helper
    _sort(0,len(ar)-1)

ar=[4,25,2,7]
merge_sort(ar)
print(ar)

