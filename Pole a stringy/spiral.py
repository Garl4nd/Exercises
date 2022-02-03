def spiral(ar):
    n=len(ar)
    res=[]
    k=0
    for i in range(n-1,-1,-2):
        if i==0:
            res.append(ar[k][k])
        res+=ar[k][k:k+i]
        res+=[ar[l][n-1-k] for l in range (k,k+i)]
        res+=ar[n-1-k][n-i-k:n-k][::-1]
        res+=[ar[l][k] for l in range (n-i-k,n-k)][::-1]
        k+=1        
    return res

n=7
ar=[[k for k in range(i*n+1,(i+1)*n+1)] for i in range(n)]
print(ar)
res=spiral(ar)
print(res,len(res))