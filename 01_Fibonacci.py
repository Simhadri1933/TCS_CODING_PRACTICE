# TYPE 1
def fib(n):
    n1, n2 = 0, 1
    print(n1, n2, end=" ")
    for i in range(2, n):
        n3 = n1 + n2
        n1, n2 = n2, n3
        print(n3, end=" ")

fib(9)


# TYPE 2
n = int(input("enteer a number:"))
n1 = 0
n2= 1
print(n1,n2,end=" ")
for i in range(0,n):
    n3 = n1 +n2
    n1 = n2
    n2 = n3
    print(n3,end=" ")