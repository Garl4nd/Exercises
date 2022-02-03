import sortedcontainers as sc
t =sc.SortedDict([(5, 'Alfa'), (2, 'Bravo'), (7, 'Charlie'), (3, 'Delta'), 
(6, 'Echo')]) 
print(t[2]) # 'Bravo' 
#print (t. min_item () , t.max_item()) # (2, 'Bravo'), (7, 'Charlie') 
print(t.items()[0],t.items()[-1])
# {2: 'Bravo', 3: 'Delta', 5: 'Alfa', 6: 'Echo', 7: 'Charlie', 9: 'Golf'} 
#t.insert((9,'Golf'))
t.update({9: 'Golf'})
print(t) 
#print(t.min_key() , t.max_key()) #2, 9 
print(t.keys()[0], t.keys()[-1]) #2, 9 
#t.discard(3) 
del t[3]
print(t) # {2: 'Bravo', 5: 'Alfa', 6: 'Echo', 7: 'Charlie', 9: 'Golf'} 
# a = (2: 'Bravo ') 
#a = t.pop_min() 
a=t.popitem(0)
print(t) # {5: 'Alfa', 6: 'Echo', 7: 'Charlie', 9: 'Golf'} 
# b = (9, 'Golf') 
#b = t.pop_max() 
b=t.popitem(-1)
print(t) # {5: 'Alfa', 6: 'Echo', 7: 'Charlie'} 
