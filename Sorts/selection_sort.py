def selection_sort(ar):
    for i in range(len(ar)):
        for j in range(i+1,len(ar)):
            #print("["+", ".join(map(str,ar[:i]))+"|"+", ".join(map(str,ar[i:]))+"]")
            if ar[j]<ar[i]:
                ar[i],ar[j]=ar[j],ar[i]

def selection_sort2(ar):
    
    for i in range(len(ar)):
        minval,minind=ar[i],i
        for j in range(i+1,len(ar)):
            #print("["+", ".join(map(str,ar[:i]))+"|"+", ".join(map(str,ar[i:]))+"]")
            if ar[j]<minval:
                minval=ar[j]
                minind=j
        ar[i],ar[minind]=ar[minind],ar[i]
        
ar=[2,1,0,8,9,5]
selection_sort2(ar)
print(ar)
