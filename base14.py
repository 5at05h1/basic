# セット

s = {'a', 'b', 'c', 'd'}
t = {'c', 'd', 'e', 'f'}

u = s | t
u = s.union(t)

print(u)

u = s & t
print(u)

u = s - t
print(u)

u = s ^ t
print(u)

s |= t
print(s)

s = {'apple', 'banana'}
t = {'apple', 'banana', 'lemon'}
u = {'cherry'}

print(s.issubset(t))
print(t.issuperset(s))

print(t.isdisjoint(s))
print(t.isdisjoint(u))