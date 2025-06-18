                #  ✅ Problem 3: Check whether a number is a perfect number
# 👉 A number is perfect if sum of its divisors (excluding itself) = the number
# Example: 6 → 1 + 2 + 3 = 6 ✅
# 28 → 1 + 2 + 4 + 7 + 14 = 28 ✅

num = int(input("Enter number: "))
sum = 0
for i in range(1,num):
    if num%i==0:
        sum = i + sum
if sum == num:
    print("It's a perfect number")
else:
    print("Not a perfect number")  