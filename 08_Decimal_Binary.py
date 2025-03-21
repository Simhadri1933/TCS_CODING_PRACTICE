## APPROACH
def decimal_binary(n):
    binary = " "
    while n >0:
        remainder = n % 2
        binary =str(remainder)+ binary
        n = n//2
    return binary
num = int(input("enter a number: "))
print("binary representaion",decimal_binary(num))