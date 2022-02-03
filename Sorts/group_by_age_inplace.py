from dataclasses import dataclass
from collections import Counter

@dataclass
class Person:
    age: int
    name: str

ages=40,23,23,51,40,26,24,25,23,40,75,72,75,40
people=[Person(age,chr(ord("a")+i)) for i,age in enumerate(ages)]

def sort_inplace(people):
    counts=[]
    counts=Counter(person.age for person in people)
    offsets,offset={},0
    for age,count in counts.items():
        offsets[age]=offset
        offset+=count
    ind=0
    while offsets:
        ind+=1
        age_i=next(iter(offsets)) #Tady jednoduše procházíme pole jako 1,2...n, přičemž se postoupí ve chvíli, kdy v předchozím kroce byl index na správném místě (tj. když age_i==age_j)
        i=offsets[age_i]
        age_j=people[i].age #zvolí se věk na i-tém místě. Pokud je j na správném místě, tj. když age_i==age_j, tak se pokročí v dalším kroce dál, pokud je na špatném, tak se dá na své místo a prohodí se s prvkem, kterým na tom místě byl předím. Jakmile se prvek jednou dá na správné místo, tak už se na něj nesahá (zvětší se offset, ze kterého se čerpá i) 
        j=offsets[age_j]
        people[j],people[i]=people[i],people[j]
        counts[age_j]-=1
        if counts[age_j]>0:
            offsets[age_j]+=1
        else:
            del offsets[age_j]
            
sort_inplace(people)
print(people)




