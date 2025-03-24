def check_number(num):
    if num > 0:
        print(num, "is positive.")
    elif num < 0:
        print(num, "is negative.")
    else:
        print(num, "is zero.")


def check_number(num):
    result = "positive" if num > 0 else "negative" if num < 0 else "zero"
    print(num, "is", result)