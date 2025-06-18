# Problem Statement:
# Given a string, replace every space character with the substring %20.
# Example:
# Input: "my name is Neeraj"
# Expected Output: "my%20name%20is%20Neeraj"

st = input("Enter String: ")
l = list(st)
l2 = []
for w in l:
    if w == " ":
        l2.append("%20")
    else:
        l2.append(w)
print("".join(l2))

