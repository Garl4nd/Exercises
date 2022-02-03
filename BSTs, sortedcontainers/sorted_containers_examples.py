from sortedcontainers import SortedList
sl = SortedList(['e', 'a', 'c', 'd', 'b'])
sl
SortedList(['a', 'b', 'c', 'd', 'e'])
sl *= 10_000_000
print(sl.count('c'))
print(sl[-3:])
print(sl.pop(0))
from sortedcontainers import SortedDict
sd = SortedDict({'c': 3, 'a': 1, 'b': 2})
SortedDict({'a': 1, 'b': 2, 'c': 3})
print(sd.popitem(index=-1))
print(sd.pop("a"))
from sortedcontainers import SortedSet
ss = SortedSet('abracadabra')
print(ss)
SortedSet(['a', 'b', 'c', 'd', 'r'])
print(ss.bisect_left('c'))
