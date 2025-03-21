
# ## to find the GCD and to output one number that one number can have the factors that can you pirnt
# ## the commo for the two numbers

# def gcd(a,b):
#     while b:
#         a,b=b,a%b
#     return a

# def count_factors(n):
#     count = 0
#     i = 1
#     while i * i <= n:
#         if n %  i == 0:
#             count += 1
#             if i != n //i:
#                 count+=1
#         i +=1
#     return count
# a = 18
# b = 12
# print(count_factors(gcd(a,b)))


# Practice
def gcd(a,b):
    while b:
        a,b = b,a%b
    return a
def count_factors(n):
    count = 0
    i = 1
    while i * i <= n:
        if n% i == 0:
            count += 1
            if i != n//i:
                count+= 1
            i += 1
    return count
a,b = 18,12
print(count_factors(gcd(a,b)))