# FizzBuzz from 1 to 100
# divisable by 3 =Fizz
# divisable by 5=Buzz
# divisable by 3 & 5 = FizzBuzz


for num in range(3,101):
    if num % 3==0 and num %5 ==0:
        print('FizzBuzz')
    elif num %3== 0:
        print('Fizz')
    elif num %5==0:
        print('Buzz')
    else:
        print(num)
