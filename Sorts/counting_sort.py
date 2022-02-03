from collections import Counter
def counting_sort(dic,keys,k): #input: dictionary, neuspořádaný podseznam jeho celočíselných klíčů, které jsou všechny menší než k, k. Output: Pole hodnot dic seřazené podle klíčů
    count=Counter(keys)
    cumsum=[0]
    res=[0 for _ in range(len(keys))]
    for i in range(1,k):
        cumsum.append(cumsum[-1]+count[i])
    for key in keys:
        cumsum[key]-=1
        res[cumsum[key]]=dic[key]
        

    return res

def counting_sort2(dic,keys,k): #To samé co výše, ale explicitnější. Musí se ale iterovat až do k, zatímco předtím jen do velikosti seznamu.
    count=[0 for _ in range(k)]
    for key in keys:
        count[key]+=1
    res=[]
    #print(sorted((key,val) for key,val in count.items()))
    for i in range(k):
        res=res+[i]*(count[i])
        
    return [dic[key] for key in res]



print(counting_sort({1:3,2:5,3:6,5:7,6:8,8:9},[8,1,2,2,3,5,5,6,2],10))
print(counting_sort2({1:3,2:5,3:6,5:7,6:8,8:9},[8,1,2,2,3,5,5,6,2],10))
print(counting_sort3({1:3,2:5,3:6,5:7,6:8,8:9},[1,2,2,3,5,5,6,2,8],10))
