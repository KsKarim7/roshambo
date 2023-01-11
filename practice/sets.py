s = {'asdf', 'asdf', 12, 3, 4, 12, 5}
p = {'asdf', 1, 3, 4, 5, 6, 2, 3, }
# print(s)
# print(type(s))

emptSet = set()
emptDict = {}

# print(s.union(p))
s.update(p)


cities = {'Tokyo', 'Kualalampur', 'Berlin', 'Dhaka', 'Seoul'}
cities2 = {'Tokyo', 'Kualalampur', 'Islamabad', 'Kabul'}
cities3 = cities.symmetric_difference(cities2)
print(cities3)
