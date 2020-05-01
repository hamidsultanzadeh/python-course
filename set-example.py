a = set()

b = set()

a.add(3)
a.add(2)
a.add(4)
a.add(5)

b.add(1)
b.add(3)
b.add(4)

print(a, "set a")
print(b, "set b")
print("="*10)
print(a.difference(b), "Difference a -> b")
print(b.difference(a), "Difference b -> a")
print(a.intersection(b), "Intersection a -> b or b -> a")
# difference_update
print(a.union(b), "a b union")
a.remove(3)  # if doesnt exist throw exception
a.discard(3)  # no exception

print(a, "after remove element - set a")
