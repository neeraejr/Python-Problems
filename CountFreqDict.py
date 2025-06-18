# 🧩 Problem: Count frequency of each character in a string using dictionary (without collections).
st = input("Enter String: ")
d = {}
for w in set(st):
    d[w] = st.count(w)
print(d)