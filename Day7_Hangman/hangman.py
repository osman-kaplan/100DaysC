from random import randint

                                    # GENERATE WORDS POOL IN THE FORM OF LIST 

# f= open('Day7_Hangman\seawood.txt', 'r')
print()
myList= []
with open('Day7_Hangman\seawood.txt', 'r') as txt_file:
    file_content= txt_file.readlines() #ad all the contents of the file
    # x=0
    # while x< 10:
    #     file_content= txt_file.readline().strip()
    #     print(file_content, end='')
    #     x += 1

    # for line in txt_file:
    #     print(line.strip(), end='')
    #     myList.append(line.split())
    
    for line in file_content:
        line= line.strip()
        for word in line.split():
            if len(word)>=5:
                myList.append(word)


            # GENERATE A RONDOM NUMBER 
index= randint(0, len(myList))

            # SELECT A RANDOM WORD FROM THE LIST

random_word= (myList[index].lower())
word= ''.join(letter for letter in random_word if letter.isalpha())
# word='kaplanaaaa'

blanks='_'*len(word)
print(' '.join(c for c in blanks))

while True:
    user_letter=input('Guess a letter\n>')

    if user_letter in word:
        if word.count(user_letter)==1:

        
            index2= word.find(user_letter)

            blanks= blanks[:index2]+user_letter+blanks[index2+1:]
        elif word.count(user_letter)==2:

            

            index1= word.find(user_letter)

            blanks= blanks[:index1]+user_letter+blanks[index1+1:]
            
            index2= word.find(user_letter,index1+1)

            blanks= blanks[:index2]+user_letter+blanks[index2+1:]

        elif word.count(user_letter)==3:
        
            

            index1= word.find(user_letter)

            blanks= blanks[:index1]+user_letter+blanks[index1+1:]
            
            index2= word.find(user_letter,index1+1)

            blanks= blanks[:index2]+user_letter+blanks[index2+1:]
        
            index3= word.find(user_letter,index2+1)

            blanks= blanks[:index3]+user_letter+blanks[index3+1:]

        else:
            print('The word is not valid. Stopping the code excecution...')
            exit()

        



    print(' '.join(l for l in blanks))
 