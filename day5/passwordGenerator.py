from random import randint
import random

letters='a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D I F G H I J K L M N O P Q R S T U V W X Y Z'.split()


numbers='0 1 2 3 4 5 6 7 8 9'.split()

symbols='! # $ % & ( ) * + < > | /  \\'.split()

print("Welcome to the PyPassword Generator! ")

num_letters=int(input('How many letters do u like you password to have? \n> '))

num_numbers= int(input('How many numbers you would like your password has?\n> '))

num_symbol=int(input('How many sysmbols you would like your password has?\n>'))

password=''

for i in range(num_letters):
    dig= letters[randint(0,len(letters)-1)]
    password+=dig

for i in range(num_numbers):
    dig= numbers[randint(0,len(numbers)-1)]
    password+=dig

for i in range(num_symbol):
    dig= symbols[randint(0,len(symbols)-1)]
    password+=dig



# print(password)
# print(len(password))
# password2=''

# first wayı to shuffle ==????
"""
while len(password2) < (num_symbol + num_numbers + num_letters) :
    if len(password)==0:
        break
    a= password[randint(0,len(password)-1)]
    if a not in password2:
        password2 +=a
    else:
      password=  password.replace(a,'')
    

print(password2)
print(len(password2))


print(list(password2).shuffle())
"""
# list version hard version  ***shuffle***

password=[]

for i in range(num_letters):
    dig= letters[randint(0,len(letters)-1)]
    password+=dig

for i in range(num_numbers):
    dig= numbers[randint(0,len(numbers)-1)]
    password+=dig

for i in range(num_symbol):
    dig= symbols[randint(0,len(symbols)-1)]
    password+=dig

print(password)
random.shuffle((password))
print(password)

new_pass=''
for char in password:
    new_pass += char

print(new_pass)