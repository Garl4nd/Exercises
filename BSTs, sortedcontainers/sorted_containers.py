from sortedcontainers import SortedList
sl = SortedList(['e', 'a', 'c', 'd', 'b'])
print(sl)
sl *= 10_000_000
print(sl.count('c'))
print(sl[-3:])
print(sl.pop(0))
from sortedcontainers import SortedDict
sd = SortedDict({'c': 3, 'a': 1, 'b': 2})
print(sd,sd.items()[0])
print(sd.popitem(index=-1))
from sortedcontainers import SortedSet
ss = SortedSet('abracadabra')
print(ss)
SortedSet(['a', 'b', 'c', 'd', 'r'])
print(ss.bisect_left('c'))
