# def armstrong(s):
#     temp = s
#     sum = 0
#     for digits in str(s):
#           sum += int(digits)** len(str(s))
#     return temp == sum

# def print_armstrong_numbers(start, end):
#     for num in range(start, end + 1):
#         if armstrong(num):
#             print(num)

# print_armstrong_numbers(1,1000)


# APPORACH 2
def armstrong(n):
    temp = n
    sum = 0
    power = len(str(n))
    original = n

    # Calculate the power
    # while temp != 0:
    #     temp = temp // 10
    #     power += 1

    temp = n
    # Calculate the sum
    while temp != 0:
        digit = temp % 10
        sum += digit ** power
        temp = temp // 10

    return sum == original

def print_armstrong_numbers(start, end):
    for num in range(start, end + 1):
        if armstrong(num):
            print(num)

print_armstrong_numbers(1,10000)