row1=['#','#','#']
row2=['#','#','#']
row3=['#','#','#']
map= [row1,row2,row3]
print(f'{row1}\n{row2}\n{row3}')
position=input('Where do you want to put the treasure?\n>')
y=int(position[0])
x= int(position[1])
print(x,y)
print(map)
map[y][x]='X'



# #Do not change the code above
# #Write down your code bellow 

choice= input('Which package you would like to try?\n> ')

if map[int(choice[0])][int(choice[1])]=='X':
    # print(map[int(choice[0])][int(choice[1])])
    print(map)
    print()
    print('Well done, You won!!')
else: 
    print('You lost!')