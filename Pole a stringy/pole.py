import bisect
import random
from shutil import move
def sorted_ins(ar,x): #vloží prvek do pole tak, aby zachoval jeho seřazenost
    ar.insert(bisect.bisect(ar,x),x)
def dutch_flag(ar,i):
    pivot=ar[i]
    for j in range(len(ar)):
        if ar[j]>=pivot:
            for k in range(j+1,len(ar)):
                if ar[k]<pivot:
                    ar[j],ar[k]=ar[k],ar[j]
    for j in range(len(ar)):
        if ar[j]>pivot:
            for k in range(j+1,len(ar)):
                if ar[k]==pivot:
                    ar[j],ar[k]=ar[k],ar[j]
    return ar
def dutch_flag2(ar,i):
    pivot=ar[i]
    lowind=0
    for j in range(len(ar)):
        if ar[j]<pivot:
            ar[j],ar[lowind]=ar[lowind],ar[j]
            lowind+=1
    highind=len(ar)-1
    for j in reversed(range(len(ar))):
        if j==lowind-1:
            break
        if ar[j]>pivot:
            ar[j],ar[highind]=ar[highind],ar[j]
            highind-=1
    return ar

def dutch_flag3(ar,i):
    pivot=ar[i]
    smaller,j,higher=0,0,len(ar)-1

    while(j<=higher):
        if ar[j]<pivot:
            ar[j],ar[smaller]=ar[smaller],ar[j]
            smaller+=1
            j+=1
        elif ar[j]>pivot:
            
            ar[j],ar[higher]=ar[higher],ar[j]
            higher-=1
        else:
            j+=1  
    return ar
def increment_int(intar):
    for j in range(len(intar)-1,-1,-1):
        if intar[j]<9:
            intar[j]+=1
            return intar 
        else:
            intar[j]=0
            if j==0:
                return [1]+intar
def create_intar(x,inverse=False):
    if not inverse:
        ar=[]
        while x>0:
            ar.append(x%10)
            x//=10                
        return list(reversed(ar))
    else:
        pow10=1
        num=0
        for el in reversed(x):
            num+=el*pow10
            pow10*=10
        return num

def move_game(input): #rekurze
    def has_solution(input,i):
        if i+input[i]>=len(input):
            return True
        for k in range(1,input[i]+1):
            if input[i+k]==0:
                continue
            else:
                if has_solution(input,i+k):
                    return True
        return False
    return has_solution(input,0)

def move_game2(input): #iterativně
    current=0
    max_dist=input[0]
    while max_dist<len(input) and current<=max_dist:
        max_dist=max(max_dist,input[current]+current)
        current+=1
    return max_dist>=len(input)

def all_moves_gen(input):
        def has_solution(input,i,steps):
            if i+input[i]>=len(input):
                yield steps+[input[i]]
            for k in range(i+1,min(input[i]+i+1,len(input))):
                if input[k]==0:
                    continue
                else:
                    yield from has_solution(input,k,steps+[k-i])
            
        yield from has_solution(input,0,[])

def move_game_solve(input): 
    
    try: 
        return min(all_moves_gen(input),key=len)
    except ValueError:
        return []

print(dutch_flag([3,2,10,12,42,12,23,8,4],3))
print(dutch_flag2([3,2,10,12,42,12,23,8,4],3))
print(dutch_flag3([3,2,10,12,42,12,23,8,4],3))
ar=sorted([random.randint(0,19) for _ in range(20)])
print(ar)
for _ in range(20):
    sorted_ins(ar,random.randint(0,19))
print(ar)
ar.reverse()
print(ar)
print(list(reversed(ar)))
nums=9,99,98,994,998,999
for num in nums:
    numar=create_intar(num)
    res=increment_int(list(numar))
    print(num,numar,res,create_intar(res,inverse=True))
print(move_game([5]))
print(move_game([1,4]))
print(move_game([2,3,2,1,0,2,3]))
print(move_game2([1]))
print(move_game_solve([2,4,2,1,0,2,3]))
    