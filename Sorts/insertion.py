def insertion_sort(ar):
    for i,el in enumerate(ar):
        j=i
        while j>0 and el<ar[j-1]:
            ar[j],ar[j-1]=ar[j-1],ar[j]
            j-=1

ar=[4,7,8,6,2,5,1]
insertion_sort(ar)
print(ar)