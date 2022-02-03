import heapq

def sort_almost_sorted(ar,k):
    min_heap=ar[:k+1]
    heapq.heapify(min_heap)
    res=[]
    print(min_heap)
    for el in ar[k+1:]:
        res.append((x:=heapq.heappop(min_heap)))
        heapq.heappush(min_heap,el)
    
    while min_heap:
        res.append(heapq.heappop(min_heap))
    return res

ar=[3,5,2,8,7,12,6,24,15]
print(sort_almost_sorted(ar,3))


