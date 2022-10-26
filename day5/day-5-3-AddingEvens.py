#calculates the sum of all the even numbers from 1 to 100 including 1 and 100

tot= 0
for num in range(0,101):
    if num %2==0 :
        tot+=num

print(f'Sum of all even numbers from 1 to 100 (inclusively) is: {tot}')