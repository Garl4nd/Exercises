RED, WHITE, BLUE = range(3) 
def dutch_flag_partition(pivot_index, A): 
    pivot = A[pivot_index] 
# First pass: group elements smaller than pivot. 
    for i in range(len(A)): 
# Look for a smaller element. 
        for j in range(i + 1, len(A)): 
            if A[j] < pivot: 
                A[i], A[j] = A[j], A[i] 
                break 
    
# Second pass: group elements larger than pivot. 
    for i in reversed(range(len(A))): 
        if A[i] < pivot: 
            break 
# Look for a larger element. Stop when we reach an element less than 
# pivot, since first pass has moved them to the start of A. 
        for j in reversed(range(i)): 
            if A[j] > pivot: 
                A[i], A[j] = A[j], A[i] 
                break 
def dutch_single(pivot_index,A):
    pivot=A[pivot_index]
    bot=0
    top=len(A)-1
    i=0
    while i<top:
        
        if A[i]<pivot:
            A[i],A[bot]=A[bot],A[i]
            bot+=1
            i+=1
        elif A[i]>pivot:
            A[i],A[top]=A[top],A[i]
            top-=1
        else:
            i+=1
A=[2,3,5,6,5,4,6,2,4]
print(A)
dutch_single(5,A)
print(A)