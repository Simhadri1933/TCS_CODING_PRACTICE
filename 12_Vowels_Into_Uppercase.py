def vowels_into_upper(s):
    vowels = "aeiou"
    result = ""
    for char in s:
        if char.lower() in s:
            result += char.upper()
        else:
            result += char
    return result
s = "i love you"
print(vowels_into_upper(s))