#                           Prime Number Check
# 👉 Take input from user and check if the number is prime.

num = int(input("Enter number: "))
for i in range(2,num-1):
    if num%i==0:
        print("Not Prime")
        break
else:
    print("Prime Number")