#TCS question
"""you are given three integers p,q,r you can perform the following operations any number of times
- select any two numbers and increase both by 1
- decrease the third number by 1
your task is to deterime the minimum of operations require to make all three numbers equal
input
1 2 3
4 4 4 
3 2 6
1 1 7 
output
-1
0
-1
3
give simple python code to this"""
# APPROACH 1
# def all_nums_equla(x, y, z):
#     if x != y:
#         return "x and y equal tesko ra ayya"
#     n = (z - y) // 2
#     return n
# x,y,z = map(int,input("Enter numbers:").split())
# r = all_nums_equla(x, y, z)
# if isinstance(r, str):
#     print(r)
# else:
#     print(r)
    
## APPROACH 2

# def min_operations(p, q, r):
#     if (q - p) % 2 != 0 or (r - q) % 2 != 0:
#         return -1
#     else:
#         return (q - p) // 2 + (r - q) // 2

# p, q, r = map(int, input("Enter p, q, r: ").split())
# print(min_operations(p, q, r))

# # NIVAS ANSWER
# x,y,z=map(int,input("enter").split())
# if x==y and z>=y and (z-y)%2==0:
#     print((z-y)//2)
# else:
#     print(-1)



def min_operations(a, b, c):
    total = a + b + c
    if total % 3 != 0:
        return -1
    target = total // 3
    return max(0, (target - a) + (target - b) + (target - c)) // 2

# Read input
a = 1
b = 2
c = 3
print(min_operations(a, b, c))