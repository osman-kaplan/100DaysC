# This is how you work out whether if a particular year is a leap year.

# on every year that is evenly divisible by 4 

# **except** every year that is evenly divisible by 100 

# **unless** the year is also evenly divisible by 400
yr= int(input('Which year do you want to check?\n> '))

year=2000
if year %4 ==0:
        if year % 100 ==0:
            if year % 400 ==0:
                print('Leap year.')
            else:
                print('Not leap year.')
        else:
            print('Leap year')
else:
    print('Not leap year.')