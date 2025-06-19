# ✅ Problem: Find the Top 2 Highest Frequency Words in a Sentence

st = input("Enter Sentence: ")
l = st.split()
d = {}
for w in set(l):
    d[w] = l.count(w)

sorted_dict = sorted(d.items(), key = lambda x: x[1], reverse=True)
print(sorted_dict)
print(f"Top 1: {sorted_dict[0][0]} = {sorted_dict[0][1]}")
print(f"Top 2: {sorted_dict[1][0]} = {sorted_dict[1][1]}")