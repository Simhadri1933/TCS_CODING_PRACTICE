# def sum_primes(start, end):
#     total = 0
#     for num in range(start, end + 1):
#         if num > 1:
#             is_prime = True
#             for i in range(2, num):
#                 if num % i == 0:
#                     is_prime = False
#                     break
#             if is_prime:
#                 total += num
#     return total

# start = int(input("Start: "))
# end = int(input("End: "))
# print(f"Sum of primes: {sum_primes(start, end)}")


## PRACTICE 2    (GROK)
def sum_primes(start,end):
    sum = 0
    for num in range(start,end+1):
        is_prime = True
        for i in range(2,num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            sum += num
    return sum

start = int(input("enter a number:"))
end = int(input("enter a number:"))
print(sum_primes(start,end))