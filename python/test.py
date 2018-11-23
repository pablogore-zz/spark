from functools import reduce

l = range(1, 1000)
f = filter(lambda y: y % 2 == 0, l)
m = map(lambda x: x * x, f)
total = reduce(lambda x, y: x + y, m)

print(total)
