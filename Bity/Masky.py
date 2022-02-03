def set_bit(pos):
    return 1 << (pos-1)

def get_bit(x,pos):
    return (x>>pos-1) &1

#def check_bit(x,bit_pos):
    #return x&set_bit(bit_pos)>0

def unset_bit(x,bit_pos):
    return x & ~set_bit(bit_pos)
def toggle_bit(x,bit_pos):
    return x ^set_bit(bit_pos)
def print_bin(x,l=None):
    if l is None:
        l=x.bit_length()
    print("{x:0{l}b}".format(x=x,l=l))
def erase_lowest(x):
    return x&(x-1)
def extract_lowest(x):
    return x&~(x-1)
def parity(x):
    result=0
    while x:
        result ^=1
        x &= x-1
    return result
def rightfill(x):#nahradi nuly napravo od prvni jednicky jednickama
    n=x.bit_length()
    return x ^ (extract_lowest(x)-1)
def mod_pow(x,n):
    return x & (set_bit(n+1)-1)

def test_powof2(x):
    return x&(x-1)==0
def swap_bits(x,m,n):
    if (x>>m) & 1 == (x>>n) & 1:
        return x
    else:
        mask=set_bit(m) |set_bit(n)
        return x ^ mask
def bit_add(x,y):
    carry=0
    result=0
    print_bin(x,5)
    print_bin(y,5)
    k=1
    if x<0:
        nx=x.bit_length()

    tx,ty=x,y
    while tx or ty:

        bx,by=x & k,y & k
        #bx,by=x & 1, y& 1
        res=bx ^ by ^carry
        carry=bx & by | bx & carry | by & carry
        tx>>=1
        ty>>=1    
        result |= res #k (k if res else 0)
        k<<=1
        carry<<=1
      #  print("r:")
        print(bx,by,res,carry)
        print_bin(result,5)
        print(tx,ty)
      #  print_bin(result)
    return  result | carry# (k if carry else 0)

def bit_add_2(x,y):
    
    carry=0
    result=0
    print_bin(x,5)
    #print_bin(y,5)
    k=1
    while x!=0 or y!=0:
        bx,by=x & 1, y& 1
        res=bx ^ by ^carry
        carry=bx & by | bx & carry | by & carry
        x>>=1
        y>>=1    
        result = result | (k if res else 0)
        k<<=1
      #  print("r:")
        print(bx,by,res,carry)
        print_bin(result,5)
      #  print_bin(result)
    return  result | (k if carry else 0)

def bit_multiply(x,y):
    k=1
    result=0
    while x:
        if x &1:
            result=bit_add(result,y)
        x>>=1
        y<<=1
    return result

def divide(x,y):
    res=0
    
    while x>=y:
        ty=y
        twok=1
        while True:
            
            if (ty<<1)>x:
                break            
            ty<<=1
            twok<<=1
            print(ty,twok)

        res+=twok
        print(x,ty)
        x-=ty
    return res

def exp(x,y):
    res=1
    while y:
        if y&1:
            res*=x
        x,y=x*x,y>>1
    return res

def exp2(x,y):
    x0=x
    res=1
    while y>0:
        c=1
        x=x0
        while c<<1<y:
            c<<=1
            x=x*x
            print(c,x,y)
        y-=c
        res*=x
    return res
#print(check_bit(6,5))
print(get_bit(6,4))
print_bin(6)
print_bin(unset_bit(6,3),3)
print_bin(toggle_bit(6,3),3)
print_bin(7)
print(parity(7))
print_bin(erase_lowest(7),3)
print_bin(extract_lowest(7),3)
x=0b10010101000
print_bin(x)
print_bin(~2**11%extract_lowest(x),11)
print_bin(rightfill(x))
print(mod_pow(15,3))
print(test_powof2(15))
print_bin(14)
print_bin(swap_bits(14,1,4),4)
x=2
y=2
#print_bin(x,5)
#print_bin(y,5)
print(bit_add(x,y))
#print(bit_multiply(4,8))
#print_bin(bit_add(x,y),5)
print(divide(24,5))
print(exp2(3,4))
print(exp(2,3))