from math import *

print("Here you can see the prime numbers as you want.")
a = int(input("Enter the starting number : "))
b = int(input("Enter the ending number : "))

def prime(n):
    if n<2:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True
x  = 0
for j in range(a,b+1):
    if prime(j):
        print(j,end=" ")
        x += 1
print()
print("Total prime numbers are", x)