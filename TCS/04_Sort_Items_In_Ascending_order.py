# def sort_items(arr):
#     low = []
#     medium= []
#     high = []
#     for i in arr:
#         if i == 0:
#             low.append(i)
#         elif i == 1:
#             medium.append(i)
#         else:
#             high.append(i)
#     r = low+medium+high
#     return " ".join(map(str,r))
# arr = [1,0,2,1,1,2]
# print(sort_items(arr))

def sort_items(arr):
    arr.sort()
    return arr
arr = [1,0,2,1,1,2]
print(sort_items(arr))