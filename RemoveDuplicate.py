#               ✅ Problem 5: Remove duplicates from a list without using set()
# Input: [1,2,2,3,4,1]
# Output: [1,2,3,4]

l = [1,2,2,3,4,1]
el = []
for i in l:
    if i in el:
        continue
    else:
        el.append(i)
print(el)