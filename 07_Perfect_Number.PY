## APPROACH 1
n = int(input("enter a number:"))
sum = 0
for i in range(1,n):
    if n % i == 0:
        sum +=i
if sum == n:
    print("perfect numvber")
else:
    print("not perfect")

    
## APPROACH 2
def is_perfect(num):
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            sum +=i
    return sum == num
n = int(input("enter a number :"))
if is_perfect(n):
    print("its perfect")
else:
    print("not perfect")