from heap_impl import Heap
import numpy as np


def median_calc(stream):
    
    min_heap=Heap(None,key=lambda x:-x)
    max_heap=Heap(None)
    median=inval=next(stream)
    yield median
    min_heap.append(inval)
    max_heap.append(inval)
    odd=True
    while True:
        odd=not odd
        try:
            val=next(stream)
        except StopIteration:
            return
        if not odd:
            if val<=median:
                max_heap.append(val)
                max_heap.pop()
            else:
                min_heap.append(val)
                min_heap.pop()
        else:
            if val<=median:
                max_heap.append(val)
                min_heap.append(max_heap.root.val)
            else:
                min_heap.append(val)
                max_heap.append(min_heap.root.val)
        
        median=(min_heap.root.val+max_heap.root.val)/2
        yield median
        
        


ar=[7,1,0,-5,54,100]
stream=iter(ar)

for median,ind in zip(median_calc(stream),range(len(ar))):
    print(median,np.median(ar[:ind+1]))