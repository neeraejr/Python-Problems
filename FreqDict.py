# Count frequency of elements in a list using dictionary
l = [1,1,2,2,3,3,3,4,4,4,4,4]
dt = {}
for w in set(l):
    dt[w] = l.count(w)
print(dt)