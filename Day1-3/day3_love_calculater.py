nameM=input("What is the male's name?\n> ")
nameF=input("What is female's name?\n> ")
digitM=0
# for m in 'love':
    
#     digitM += (nameF + nameM).lower().count(m)
# digitF= 0
# for f in 'true':
#     digitF += (nameF + nameM).lower().count(f)
    
# loveScore= int(str(digitM) + str(digitF)) 

def giveScope(name, name2,term):
    myNames= name +' '+name2
    dig= 0
    for i in term:
       dig += myNames.lower().count(i)
    return dig


loveScore1 = giveScope(nameM,nameF,'love')
loveScore2 = giveScope(nameM,nameF,'true')

loveScore= int(str(loveScore1)+str(loveScore2))



if loveScore < 10 or loveScore >90:
    print(f'Your score is {loveScore}, you go together like coke and mentos.')

elif loveScore > 40 and loveScore <=50:
    print(f'Your score is {loveScore}, you are alright together.')
else:
    print(f'Your score is {loveScore}')



