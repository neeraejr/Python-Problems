# 🔹 Problem: Capitalize first letter of every 
# word in a sentence (without using title())
st = input("Enter Sentence: ")
l = st.split()
l2 = []
for word in l:
    capitalized = word[0].upper() + word[1:]
    l2.append(capitalized)
l3 = " ".join(l2)
print(l3)