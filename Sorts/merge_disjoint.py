def merge(oldints,newint):
    res=[]
    
    i=0
    for i,(startpoint,endpoint) in enumerate(oldints):

        if endpoint<newint[0]:
            res.append((startpoint,endpoint))    
        elif startpoint>newint[1]:
            break            
        elif startpoint<=newint[1]:
            newint=(min(startpoint,newint[0]),max(endpoint,newint[1]))
 
    return res+[newint]+oldints[i:]

def merge2(oldints,newint):
    res=[]
    added=False
    i=0
    lint=len(oldints)
    while i in range(lint):
        startpoint,endpoint=oldints[i]
        
        if endpoint<newint[0]:
            res.append((startpoint,endpoint))    
        elif startpoint>newint[1]:
            break
        elif startpoint<=newint[1]:
            newint=(min(startpoint,newint[0]),max(endpoint,newint[1]))
        i+=1
    return res+[newint]+oldints[i:]

def make_disjoint(ints):
    
    sorted_ints=sorted(ints,key=lambda tup:tup[0])
    res=[]
    for int in ints:
        res=merge2(res,int)
    return res

ints=[(0,2),(2,3),(6,7),(8,10),(11,12)]
#ints=[(0,1)]
newint=(0,1)
print(merge(ints,newint))
print(merge2(ints,newint))
            
print(make_disjoint([(0,1),(2,7),(6,8)]))
