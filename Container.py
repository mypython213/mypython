from collections import namedtuple, deque, OrderedDict, defaultdict, Counter

Point = namedtuple('point', ['x','y'])

p = Point(11,22)

# print (p.x, p.y)

my_deque = deque()
my_deque.append(10)
my_deque.appendleft(20)
my_deque.append(11)
# print(my_deque)
# print(my_deque.popleft())
# print(my_deque)


od = OrderedDict()

od['a'] = 1, 2
od['d'] = 4
od['b'] = [2, 3]
od['c'] = od

# print(od)

dd = defaultdict(lambda :1)
dd['eee'] = 2
# print(dd['eee'])


cnt = Counter({'first':1, 'second':2, 'third':3})
print (cnt)
print (cnt.get('first'))