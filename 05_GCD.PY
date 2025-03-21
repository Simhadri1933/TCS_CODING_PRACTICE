def gcd(a,b):
    while b!=0:
        a, b = b, a%b
    return a
a = 48
b = 18
print(gcd(a,b))

# USING TEMP

a = 48
b = 18

while b != 0:
    temp = a % b
    a = b
    b = temp

print("GCD is:", a)