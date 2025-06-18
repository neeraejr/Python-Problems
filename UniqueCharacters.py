#               3. Check if string has all unique characters
# Input: "abcde" → ✅, "hello" → ❌
st = input("Enter string: ")
l1 = list(st)
l2 = set(st)
if len(l1) == len(l2):
    print("String has unique characters.")
else:
    print("Not Unique")

#  or

st = input("Enter string: ")
if len(st) == len(set(st)):
    print("Unique characters")
else:
    print("Not Unique")
