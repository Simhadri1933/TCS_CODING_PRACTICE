# """
# Fredo is assigned a new task today. He is given an array A
# containing N integers. His task is to update all elements of array to 
# some minimum value x, that is, A[i] = x; 1 ≤ i ≤ N such that sum 
# of this new array is strictly greater than the sum of the initial array.
# Note that x should be as minimum as possible such that sum of the 
# new array is greater than the sum of the initial array.

# Input Format:
# First line of input consists of an integer N denoting the number of
# elements in the array A.
# Second line consists of N space separated integers denoting the
# array elements.

# Output Format:
# The only line of output consists of the value of x.
# Input Constraints:

# 1≤ N ≤ 10**5
# 1 ≤A [i] ≤1000

# sample input: 
#  5 
#  1 2 3 4 5
# o/p = 4

# Explanation
# Initial sum of array \(= 1+2+3+4+5= 15\)
# When we update all elements to 4, sum of array \(= 4+4+4+4+4 = 20\) which is
# greater than \(15\)
# Note that if we had updated the array elements to 3, \(sum= 15l) which is 
# not greater than \(15\). So, 4 is the minimum value to which array elements need 
# to be updated
# """

# ## code



def minarray(n,arr):
    total =sum(arr)
    min_x =(total//n)+(1 if total % n !=0 else 0)
    return min_x
n = 5
arr = list(map(int,input().split()))
print(minarray(n,arr))

# modify from above

def minarray(n, arr):
    total = sum(arr)
    min_x = total // n
    if total % n != 0:
        min_x += 1
    return min_x

n = 5
arr = [1 ,2, 3, 4, 5]
print(minarray(n, arr))



n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

total = sum(arr)
min_x = total // n
if total % n != 0:
    min_x += 1

print(min_x)


## Pactice 

def minarray(n, arr):
    total = sum(arr)
    min_x = total // n
    if total % n != 0:
        min_x += 1
    return min_x

n = int(input())
arr =  [1,2,3,4,5]
print(minarray(n, arr))