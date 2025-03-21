"""A chocolate factory is packing chocolates into the packets. The chocolate packets here represent an array  
of N number of integer values. The task is to find the empty packets(0) of chocolate and push it to the end of 
the conveyor belt(array).

Example 1 :

N=8 and arr = [4,5,0,1,9,0,5,0].

There are 3 empty packets in the given set. These 3 empty packets represented as O should be pushed towards 
the end of the array

Input :

8  – Value of N

[4,5,0,1,9,0,5,0] – Element of arr[O] to arr[N-1],While input each element is separated by newline

Output:

4 5 1 9 5 0 0 0"""


## Zeros into Last
def emptypockets_into_last(n):
    n_zero =[]
    zero=[]
    for i in n:
        if i != 0:
            n_zero.append(i)
        else:
            zero.append(i)
    r = (n_zero+zero)
    return " ".join(map(str,r))
print(emptypockets_into_last([4,5,0,1,9,0,5,0]))


# ZEROS IN TO 1ST

# def emptypockets_into_last(n):
#     n_zero =[]
#     zero=[]
#     for i in n:
#         if i == 0:
#             n_zero.append(i)
#         else:
#             zero.append(i)
#     r = (n_zero+zero)
#     return " ".join(map(str,r))
# print(emptypockets_into_last([4,5,0,1,9,0,5,0]))
