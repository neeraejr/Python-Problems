# 🧩 Problem: Merge two dictionaries but add values of common keys.

d1 = {'a': 10, 'b': 20}
d2 = {'b': 30, 'c': 40}
d3 = {}
for w in d1:
    d3[w] = d1[w]

for w in d2:
    if w in d3:
        d3[w] += d2[w]
    else:
        d3[w] = d2[w]
print(d3)