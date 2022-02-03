def bubble_sort(ar):
    n=len(ar)-1
    sorted=False
    while not sorted:
        sorted=True
        for i in range(len(ar)-1):
            
            if ar[i]>ar[i+1]:
                ar[i],ar[i+1]=ar[i+1],ar[i]
                sorted=False

ar=[4,7,8,6,2,5,1]
bubble_sort(ar)
print(ar)