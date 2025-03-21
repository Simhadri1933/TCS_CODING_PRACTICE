# n = int(input("Enter a number: "))

# for i in range(1,int(n**0.5)+1):
#     print(i*i)




n = int(input("Enter a number: "))

i = 1
while i * i <= n:
    print(i * i)
    i += 1