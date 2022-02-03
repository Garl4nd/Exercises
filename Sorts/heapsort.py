from heap.heap_impl import Heap

def heap_sort(ar):
    heap=Heap.CreateBinHeap(ar,key=lambda x:-x)
    res=[]
    while heap:
        res.append(heap.pop())
    ar[:]=res

ar=[2,1,0,8,9,5]
heap_sort(ar)
print(ar)