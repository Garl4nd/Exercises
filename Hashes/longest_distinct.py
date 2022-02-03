from collections import deque,Counter
def distinct(text):
    posdict={}
    
    
    textwords=text.split()
    maxlen=0
    entry_queue=deque()
    l,u=0,0
    textwords+=[textwords[0]]
    for ind,word in enumerate(textwords):
        
            if word in entry_queue:
                mx,mn=ind-1,posdict[entry_queue[0]]
                if (dif:=mx-mn)>maxlen:
                    maxlen=dif
                    l,u=mn,mx
                
                while entry_queue.popleft()!=word:
                    pass
            
            entry_queue.append(word)
            posdict[word]=ind
    return l,u

def longest_growing(nums): # finds the longest growing subarray
    
    
    
    maxlen=0
    entry_queue=deque()
    l,u=0,0
    lastnum=nums[0]
    nums+=[nums[-1]-1]
    firstind=0
    for ind,num in enumerate(nums):
        
            if num<lastnum:
                mx,mn=ind-1,firstind
                if (dif:=mx-mn)>maxlen:
                    maxlen=dif
                    l,u=mn,mx
                firstind=ind
            lastnum=num
    
    return l,u

def longest_containing(nums): #O(n^2) :( (ale průměrně asi lepší)
    
    
    
    
    maxlen=0
    entry_queue=deque()
    l,u=0,0
    
    firstind=0
    maxind=0
    
    while firstind<len(nums):

        zarazka=True
        nextfirst=firstind+1
        num=nums[firstind]
        rolmax=num
        lastnum=num

        for ind2 in range(firstind+1,len(nums)):
            num2=nums[ind2]
            if zarazka and num2<lastnum:
                nextfirst=ind2
                zarazka=False
            if num2>rolmax:
                
                rolmax=num2
                if (dif:=ind2-firstind)>maxlen:
                    print(">",num,rolmax,ind2,firstind,maxlen)
                    l,u=firstind,ind2
                    maxlen=dif

            if num2<num:
                break
            lastnum=num2
        firstind=nextfirst
        
    
    return l,u



def longest_succesive(nums):
    numcount=Counter(nums)
    maxchain=0
    chain=0
    l,u=0,0
    for num in range(min(numcount),max(numcount)+1):
        print(num,numcount[num],chain,maxchain)
        if numcount[num]==1:
            chain+=1
            if chain>maxchain:
                maxchain=chain
                l,u=num-maxchain+1,num
        else:
            chain=0
        
    return l,u

def longest_succesive2(A):  # pomerne elegantni reseni z knihy, vyuziva set. Stejne jako predchozi reseni je casova komplexita O(n), ale stačí jen jeden průchod. Na druhou stranu ale musí pokaždé kontrolovat přítomnost prvku v poli! To je O(1)?! Ano, protože set je implementován jako hash table.
# unprocessed_entries records the existence of each entry in A. 
    unprocessed_entries = set(A) 
    max_interval_size = 0
    while unprocessed_entries: 
        a = unprocessed_entries.pop() 
    # Finds the lower bound of the largest range containing a. 
        lower_bound = a - 1 
        while lower_bound in unprocessed_entries: 
            unprocessed_entries.remove(lower_bound) 
            lower_bound -= 1 
        
        # Finds the upper bound of the largest range containing a. 
        upper_bound = a + 1 
        while upper_bound in unprocessed_entries: 
            unprocessed_entries.remove(upper_bound) 
            upper_bound += 1 
        max_interval_size = max(max_interval_size, upper_bound - lower_bound - 1) 
    return max_interval_size 

print(distinct("a b  c b d e f a b f i k"))
#print(longest_growing([0, 2, 3,2,4,5,76,2,89,92,95,99]))
ar=[0, 2, 3,5,7,8,10,2,3,5,7,8,9,10,2,3,3,3,3,3,3,3,3,3,3,3,4]
l,u=longest_containing(ar)
print(l,u,ar[l],ar[u])

print(longest_succesive([7,8,1,3,5,6]))
print(longest_succesive([7,1,3,5,6]))
print(longest_succesive2([7,8,1,3,5,6]))
