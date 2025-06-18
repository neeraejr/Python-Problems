# 🧠 Problem: Count Frequency of Each Character (Case-Insensitive)
st = input("Enter String: ")
l = list(st)
for w in set(l):
    print(f"{w}: {l.count(w)}")