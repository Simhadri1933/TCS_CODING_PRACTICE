# def oper(arr):
#     for i in arr:
#         if arr[0]==arr[1] or arr[0]== arr[2] or arr[1] == arr[2]:
#             return "proced the operation"
#         else:
#             return (arr[1] - arr[0]) // 2 + (arr[2] - arr[1]) // 2
# arr =[1,1,7]
# print(oper(arr))

# def operate(arr):
#     if len(arr) != 3:
#         return "take three"
    
#     if arr[0] == arr[1] or arr[0] == arr[2] or arr[1] == arr[2]:
#         return (arr[1] - arr[0]) // 2 + (arr[2] - arr[1]) // 2
        

# arr = [1, 7, 1]
# print(operate(arr))

# APPROACH 1
def all_nums_equla(x, y, z):
    if x != y:
        return "x and y equal tesko ra ayya"
    n = (z - y) // 2
    return n
x,y,z = map(int,input("Enter numbers:").split())
r = all_nums_equla(x, y, z)
if isinstance(r, str):
    print(r)
else:
    print(r)
    
## APPROACH 2
def min_operations(p, q, r):
    if (q - p) % 2 != 0 or (r - q) % 2 != 0:
        return -1
    else:
        return (q - p) // 2 + (r - q) // 2

p, q, r = map(int, input("Enter p, q, r: ").split())
print(min_operations(p, q, r))
