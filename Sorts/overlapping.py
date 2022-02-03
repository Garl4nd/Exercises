from dataclasses import dataclass

@dataclass
class Bandwidth:
    start: float
    end: float
    bwval: int

def peak_bandwidth(bws): #Varianta úlohy na zjištění počtu překrývajících se intervalů
    @dataclass 
    class Endpoint:
        time: float
        is_start: bool
        bwval: int
        def __lt__(self,other):
            return self.time<other.time or self.time==other.time and self.is_start and not other.is_start
    
    endpoints=[]
    for bw in bws:
        endpoints.append(Endpoint(bw.start,True,bw.bwval))
        endpoints.append(Endpoint(bw.end,False,bw.bwval))
    
    bwval=maxbwval=0
    for endpoint in sorted(endpoints):
        if endpoint.is_start:
            bwval+=endpoint.bwval
        else:
            bwval-=endpoint.bwval
        if bwval>maxbwval:
            maxbwval=bwval
        
    return maxbwval

data=(0,5,10),(5.1,10,50),(4,5.08,70)
bws=[Bandwidth(dat[0],dat[1],dat[2]) for dat in data]
print(peak_bandwidth(bws))

