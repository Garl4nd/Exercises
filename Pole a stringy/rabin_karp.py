#Rabin_karpův algoritmus. Kupodivu na krátké substringy je pomalejší
import functools as ft
def rk_find(text,substr):
    base=ord("z")-ord("A")
    lss=len(substr)
    sb=base**(lss)
    val_dict={chr(ord("A")+pos):pos for pos in range(base)}
    cur_val=ft.reduce(lambda num,c: num*base+val_dict[c],text[:lss],0)
    ss_val=ft.reduce(lambda num,c: num*base+val_dict[c],substr,0)
    #print(cur_val,ss_val)
    def update(cur,c):
        cur=(cur*base)%sb+val_dict[c]    
        return cur
    pos=0
    for c in text[lss:]:
        if cur_val==ss_val:
            return pos
        else:
            cur_val=update(cur_val,c)
            #print(c,cur_val,ss_val)
            pos+=1

    return -1

def naive_find(text,substr):
    lss=len(substr)
    l_main=len(text)
    for ind in range(0,l_main-lss):
        cur=text[ind:ind+lss]
        #print(cur)
        if cur==substr:
            return ind
    return -1

def naive_find2(text,substr):
    lss=len(substr)
    l_main=len(text)
    cur_text=text[:lss]
    pos=0
    for c in text[lss:]:
        if cur_text==substr:
            return pos
        else:
            cur_text=cur_text[1:]+c
            pos+=1
        #print(cur)
        

    return -1


text="liojabcdef"
ss="cde"
l_ss=len(ss)
#ind=rk_find(text,"cde")
ind=naive_find2(text,"cde")
print(ind,text[ind:ind+l_ss])
    