from collections import Counter
import itertools as it

def palindromable(text):
    c=Counter(text)
    oddnum=0
    for val in c.values():
        if val%2:
            oddnum+=1
        if oddnum>1:
            return False
    return True

def form_palindromes(text):
    if not palindromable(text):
        raise ValueError("The word is not palindromable!")
    c=Counter(text)
    middle=""
    edge=""
    for key,val in c.items():
        if val%2:
            middle=key
            if val>1:
                edge+=key
        else:
            edge+=key
    for right in it.permutations(edge):
        print(right)
    return ["".join(right)[::-1]+middle+"".join(right) for right in it.permutations(edge)]


    print(c.most_common())
print(palindromable("tarotor"))
print(form_palindromes("tarotor"))