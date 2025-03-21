"""Q GIVEN A STRING that can change the values of the given string by the condition the condition 
   that is even places are shift forward 2 lenghth and odd places are shift backward 1 character"""


"""given a string like  abcdef i can change the even number positon character by  1 charcter
previous in alphabets character and odd positons of the character can cahnge by shift 2 
charater forward the 
final ansewer is caecge"""



def changee_form_stirng(s):
    result = ""
    for i in range(len(s)):
        if i % 2 == 0:
            new_char = chr((ord(s[i]) - ord('a') + 2) % 26 + ord('a'))
        else:
            new_char = chr((ord(s[i]) - ord('a') - 1) % 26 + ord('a'))
        result += new_char
    return result

input_str = "abcdef"
output = changee_form_stirng(input_str)
print(output)

## practice 2
def changestrig(s):
    result = ""
    for i in range(len(s)):
        if i % 2 == 0:
            new_chr = chr((ord(s[i])-ord("a") + 2) % 26 + ord("a"))
        else:
            new_chr = chr((ord(s[i])-ord("a") - 1) % 26 + ord("a"))
        result += new_chr
    return result
s = "abcdef"
print(changestrig(s))