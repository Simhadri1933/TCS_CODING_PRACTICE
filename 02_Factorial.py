# APPROACH 2
def factorial(n):
    fact = 1
    while n<0:
        print("not possible")
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

n = 4
print(factorial(n)) 


## APPROACH 2
n =6
fact = 1
if n<0:
    print("not possible")
else:
    for i in range(1,n+1):
        fact = fact*i
print(fact)