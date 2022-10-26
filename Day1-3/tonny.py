# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


nameM= name1#input("What is the male's name?\n> ")
nameF=name2#input("What is female's name?\n> ")
digitM=0
for m in 'love':
    
    digitM += nameM.lower().count(m)

digitF= 0
for f in 'love':
    
    digitF += nameF.lower().count(f)

loveScore= int(str(digitM) + str(digitF)) 

if loveScore < 10 or loveScore >90:
    print(f'Your score is {loveScore}, you go together like coke and mentos.')

elif loveScore > 40 and loveScore <=50:
    print(f'Your score is {loveScore}, you are alright together.')
else:
    print(f'Your score is {loveScore}')