#                    ✅ Problem 4: Print Fibonacci series up to n terms
# Input: n = 10
# Output: 0 1 1 2 3 5 8 13 21 34

n = int(input("Enter number: "))
a = 0
b = 1
print(a, b, end=" ")
for i in range(n - 2):  
    c = a + b
    print(c, end=" ")
    a = b
    b = c