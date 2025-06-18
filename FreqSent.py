# ✅ Problem 4: Count frequency of each word in a sentence (case-insensitive)

import re
st = input("Enter Sentence: ")
s = re.sub(r'[^\w\s]', '', st)
s = s.lower()
l = s.split()
d ={}
for w in set(l):
    d[w] = l.count(w)
print(d)

