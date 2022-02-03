valids=set()
invalids=set()
def colatz(num,lim=10**20):
    startnum=num
    candidates=set()
    candidates.add(num)
    while num!=1:
    #while num!=0:
        if num in valids:
            valids.update(candidates)        
            return True
        if num in invalids:
            invalids.update(candidates)
            return False
      
        #num=(num+2)%10
        if num%2:
            num=3*num+4
        else:
            num=1
        if num==startnum or num>lim:
            invalids.update(candidates)
            return False

        candidates.add(num)
    
    valids.update(candidates)
    return True
    
def test(maxnum):
    for i in range(1,maxnum,2):
      
        print(i,colatz(i))

test(130)