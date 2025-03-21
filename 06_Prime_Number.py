
# # 1st APPROACH
# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not a prime")
#             break
#     else:
#         print("Prime number")
# else:
#     print("Not a prime number")


# # APPROACH 2
# n = int(input("Enter a mumber:"))
# for num in range(2,n+1):
#     for i in range(2,int(num**0.5)+1):
#         if num % i == 0:
#             break
#     else:
#         print(num,end=" ")

# APPROACCH 3
def prime(start,end):
    count = 0
    for num in range(start,end+1):
        if num>1:
            for i in range(2,num):
                if num % i == 0:
                    break
            else:
                count += 1
                print(num,end=" ")
    return count

start = 1
end = 100
countprime =prime(start,end)
print(f":{countprime}")