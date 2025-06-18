#                                      Armstrong 
# An Armstrong number is a number whose sum of its 
# own digits each raised to the power of the number 
# of digits is equal to the number itself.
# ✅ Example:
# Take 153
# It has 3 digits
# 13+53+33=1+125+27=1531 
# 3+53+33=1+125+27=153 
# ✅So, 153 is an Armstrong number.

num = int(input("Enter Number: "))
val = num
sum = 0
while val>0:
    vl = val %10
    sum= (vl**3) + sum
    val = val //10
if num == sum:
    print("Armstrong")
else:
    print("Not Armstrong")