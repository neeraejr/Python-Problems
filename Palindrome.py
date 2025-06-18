#                                   Palindrome Program
# A palindrome is a word, number, or phrase that
# reads the same forward and backward.
# ✅ Examples:
# Word: "madam", "level"
# Number: 121, 1331
# Phrase: "nurses run" (ignoring spaces)

name = input("Enter String: ")
revname = list(name[::-1])
revers = "".join(revname)
if name == revers:
    print("Palindrome")
else:
    print("Non Palindrome")