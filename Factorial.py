#                       Factorail
# The factorial of a number is the product of all positive 
# integers from 1 to that number.
# ✅ Symbol:
# Factorial of n is written as: n!

n = int(input("Enter number: "))
def fact(n):
    if n == 1 or n ==0:
        return 1
    else: 
        return n * fact(n-1)
print(f"Factorail of {n}! is : {fact(n)}")