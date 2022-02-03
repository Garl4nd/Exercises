from collections import Counter

def constructible(magazine,letter):
    
    mag_count=Counter(magazine)
    let_count=Counter(letter)
    
    for key,val in let_count.items()    :
        if mag_count[key]<val:
            return False
    return True

def constructible2(magazine,letter):
    
    mag_count=Counter(magazine)
    let_count=Counter(letter)

    return not (let_count-mag_count)

def constructible3(magazine,letter):
    
    let_count=Counter(letter)
    
    for letter in magazine:
        if letter in let_count:
            let_count[letter]-=1
        if let_count[letter]==0:
            del let_count[letter]
        if not let_count:
            return True
        
    return False




print(constructible("abbcddef","acef"),constructible("abbcddef","acefg"))
print(constructible2("abbcddef","acef"),constructible2("abbcddef","acefg"))
print(constructible3("abbcddef","acef"),constructible3("abbcddef","acefg"))

