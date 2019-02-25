import math
k = 0
n = int(input("Enter the number to get the difference between the sum of the squares and sqaure of sum : "))
for i in range (1,n+1):
    j = math.pow(i,2)
    k = k + j
l = 0
for i in range (1,n+1):
    l = l + i
    p = math.pow(l,2)
d = p - k
print("Difference between Sum of Square & Square of Sum is :",d)
