#                   Count Characters in a String
# 👉 Count how many:
# Alphabets
# Digits
# Special characters
# Spaces

st = input("Enter String: ")
l1 = list(st)
v = [x for x in l1 if x in 'aeiou']
c = [x for x in l1 if x in 'bcdfghjklmnpqrstvwxyz']
d = [x for x in l1 if x in '1234567890']
s = [x for x in l1 if x in '!`~@#$%^&*()_+=-[];:\'\\\{\}/*.,?<>']
sp = [x for x in l1 if x in ' ']
print(f"Alphabets: {len(l1)}")
print(f"Vowels: {len(v)}")
print(f"Consonents: {len(c)}")
print(f"Digits: {len(d)}")
print(f"Special Characters: {len(s)}")
print(f"Spaces: {len(sp)}")