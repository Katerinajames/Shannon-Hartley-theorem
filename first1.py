import math
print ("SHANNON HARTLEY THEOREM")
print ("ACHIEVABLE CAPAVITY CALCULATION")
print  ("C = B * log2(1+ S/N)")
print("------------------------------------------")

b=float(input("Enter bandwidth\n"))
s=float(input("Enter average signal power \n"))
n=float(input("Enter average noise  power \n"))

c=b*math.log2(1+s/n)

print ("The achievable channel capacity is %.2f "%(c))

#https://www.inf.fu-berlin.de/lehre/WS01/19548-U/shannon.html
