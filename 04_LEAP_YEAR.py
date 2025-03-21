# year = int(input("enter a year:"))
# if year % 400 == 0 or year % 4 == 0 and year% 100 != 0:
#     print("leap year")
# else:
#     print("not leap")


def print_leap_years(start, end):
    for year in range(start, end+1):
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            print(year,end=" ")

print_leap_years(1,1000)