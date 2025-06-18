#                   Vowel Counter
# A vowel counter counts how many vowels (a, e, i, o, u) 
# are present in a given string.
# ✅ Example:
# Input: "hello world"
# Vowels: e, o, o → Total 3 vowels

name = input("Enter string: ")
l1 = list(name)
l2 = [x for x in l1 if x in 'aeiou'] 
for l in set(l2):
    print(f"{l} = {l2.count(l)}")
