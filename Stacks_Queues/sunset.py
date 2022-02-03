def get_sunset_builds_EW(heights):
    res=[]
    
    max_h=0
    for height in heights:
        while res and height>res[-1]:
            
            if height>res[-1]:
                res.pop()
            

        res.append(height)
        
    return res

def get_sunset_builds_WE(heights):
    res=[]
    max_h=0
    for height in heights:
        
        if height>max_h:
            res.append(height)
            max_h=height
    return res

print(get_sunset_builds_WE([7,12,8,14]))
print(get_sunset_builds_EW(reversed([7,12,8,14])))
        