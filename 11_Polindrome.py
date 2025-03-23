
# # Given number can check the it is polidndrome or not
# def palindrome(n):
#     rev = 0
#     original_n = n
#     while n > 0:
#         digit = n % 10
#         rev = rev * 10 + digit
#         n //= 10
#     if rev == original_n:
#         print("is a palindrome")
#     else:
#         print("is not a palindrome")

# n = 1234
# palindrome(n)


# def palindrome(start, end):
#     sum = 0
#     for num in range(start, end + 1):
#         rev = 0
#         original = num
#         while num > 0:
#             digit = num % 10
#             rev = rev * 10 + digit
#             num //= 10
#         if rev == original:
#             print(original,end="")
#             sum += original
#     print("\nsum:",sum)

# start = 10
# end = 100
# (palindrome(start,end))



## RANGE OF A NUMBERS
# for num in range(10, 200):  # Example range from 10 to 199
#     reverse = 0
#     temp = num  # Copy of num for calculations

#     while temp > 0:
#         digit = temp % 10
#         reverse = reverse * 10 + digit
#         temp //= 10

#     if num == reverse:
#         print(num, end=" ")



# num = 12321
# reverse = int(str(num)[::-1])

# if num == reverse:
#   print('Palindrome')
# else:
#   print("Not Palindrome")



def checkPalindrome(str):
    for i in range(0, len(str)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True
s = "kayak"

print("Palindrome") if checkPalindrome(s) else print("Not Palindrome")