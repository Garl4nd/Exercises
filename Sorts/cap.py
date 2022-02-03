def get_caps(wages,payroll): #neelegantní řešení - nevyužívá toho, že se dá dokázat, že pro problém existuje nanejvýš jedno řešení
    
    if payroll>sum(wages):
        return []

    sorted_wages=[0]+sorted(wages)
    cumsum=0
    res=[]
    n=len(wages)
    
    for s,wage in enumerate(sorted_wages):
        cumsum+=wage
        if cumsum>payroll:
            break
        cap=(payroll-cumsum)/(n-s)
        print(cap)
        if cap<=sorted_wages[s+1] and cap>wage:
            res.append((payroll-cumsum)/(n-s))
        else:
            continue
    return res

def get_caps2(wages,payroll): #lepší (ale jen kvůli tomu, že jakmile najde, tak rovnou vrací, jinak to řešení přes porovná capu s hodnotami mezd je průhlednější)
    
    if payroll>sum(wages):
        return -1

    sorted_wages=sorted(wages)
    cumsum=0
    n=len(wages)
    
    for s,wage in enumerate(sorted_wages):
        
        if cumsum>payroll:
            break
        rem=n-s
        if cumsum+wage*rem>payroll:
            return (payroll-cumsum)/rem
        cumsum+=wage
    return -1
print(get_caps([20,30,40,90,100,150,250],500))
print(get_caps2([20,30,40,90,100],50))

