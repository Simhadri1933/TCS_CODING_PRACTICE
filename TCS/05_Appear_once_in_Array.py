# FREQUENCY OF A NUMBERS
"""you are given an array containg N integers where only one element is unique (appear exactly once),
while all other elements appear twice. find and return the unique elements
input =[5,3,2,3,2]
output 5
"""
""""
def once(arr):
    for i in set(arr):
        print(f"{i}:{arr.count(i)}")
arr = [5,3,2,3,2]
print(once(arr))"""

## 1 NUMBBER IS EQUAL
def count_num(arr):
    for i in arr:
        if arr.count(i)==1:
            return i
arr = [5,5, 9, 3, 9]
print(count_num(arr))

## INCASE 2 NUMBERS ARE UNIQUE
def unique(arr):
    uniques = []
    for i in arr:
        if arr.count(i)==1:
            uniques.append(i)
    return uniques
arr = [5, 3, 2, 3, 2, 7]
print(unique(arr))
