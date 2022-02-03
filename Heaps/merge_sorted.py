from heap_impl import Heap

def merge_noheap(*ars):
    
    #print([(ar[0],ind) for ind,ar in enumerate(ars)])
    
    arits=[iter(ar) for ar in ars]
    min_heap=Heap.CreateBinHeap([(next(arit),ind) for ind,arit in enumerate(arits)],key=lambda x:-x[0])
    ended=0
    res=[]
    lar=len(ars)
    
    while ended<lar:
        min_heap.sprint()
        val,ind=min_heap.pop()
        print(val)
        res.append(val)
        try:            
            print(res)

            min_heap.append((next(arits[ind]),ind))
            
        except StopIteration:
            ended+=1
    min_heap.sprint()
    return res

ars=[[1,5,7,9,25],[2,4,6,8,12,24,27],[0,3,4,7,8,50]]
#res=Heap.CreateBinHeap([0,1,2])
#res=Heap(5)
#res.append
#res.pop()
#res.sprint()
res=merge_noheap(*ars)
print(res)

    
