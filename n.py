from math import *
print("I'm going to rock")
u = int(input("enter a number here : "))
if u < 2:
    print("Prime numbers starts from 2.")
else:
    is_prime = True
    for i in range(2,int(sqrt(u))+1):
        if u % i == 0:
            is_prime = False
            break
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")