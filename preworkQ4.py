def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        print(f'{a_year} is a leap year')
    elif a_year % 400 == 0:
        print (f'{a_year} is a leap year')
    else:
        a_year = False
        print(f'{a_year}')
is_leap_year(2001)
    