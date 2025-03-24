def AP(a, d, n):
    # nth term
    nth_term = a + (n - 1) * d
    
    # formula
    sum_of_terms = n / 2 * (2 * a + (n - 1) * d)
    
    return nth_term, sum_of_terms

#  IP function
a = float(input("(a): "))
d = float(input("(d): "))
n = int(input("(n): "))

nth_term, sum_of_terms = AP(a, d, n)

print("n:", nth_term)
print("n:", sum_of_terms)
