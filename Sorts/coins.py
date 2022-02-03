def payable(*coinlist):
    scoinlist=sorted(coinlist)
    res=set()
    ressum=0
    firstgap=None
    for coin in scoinlist:
        if coin<=ressum+1:    
            res.update(range(ressum,ressum+coin+1))
        else:
            if firstgap is None:
                firstgap=ressum+1
                
            res.update(list(r+coin for r in res)+[coin])
        ressum+=coin
    if firstgap is None:
        firstgap=ressum+1
        

    return res,firstgap


print(payable(1,2,5,10,20,100,200))
#print(payable(1,2,4))
