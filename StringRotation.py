#                    1. Check if two strings are rotations of each other
# Input: "ABCD", "CDAB" → ✅
# (Hint: s2 in s1+s1)

s1 = "ABCD"
s2 = "CDAB"
temp = s1+s1
if s2 in temp:
    print("It's a Rotation")
else:
    print("Not a Rotation")