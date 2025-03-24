# JUST ITERATE THE NUMBERS
def naturalnum(n):
    for i in range(1,n+1):
        print(i)
n = int(input("Enter a number:"))
print(naturalnum(n))

##
def natural(n):
    i = 1
    while i <= n:
        print(i)
        i += 2
n =int(input("Enter a number:"))
print(natural(n))