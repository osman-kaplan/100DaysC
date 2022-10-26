import random
myString= input('Write down the names?\n>')
myList=myString.split(', ')
generator= random.randint(0,(len(myList)-1))

bill_payer=myList[generator]
print(f'The person to pay the bill is:\n>{bill_payer.capitalize()}')


























# myString= "osman, ahmet, kürşat, kemal, aylin, rümeysa, sinan, ebubekir"
# myList=myString.split(', ')
# thePayers=[]
# x=0
# index=[]
# while x<25:
#     generator =random.randint(0,(len(myList)-1))
#     index.append(generator)
#     print('Here is the person that gonna to pay the bill!!!')
    
#     payer= myList[generator]
#     print(payer)
#     thePayers.append(payer)
#     x+=1
# print(thePayers)
# print(index)
# print(len(thePayers))