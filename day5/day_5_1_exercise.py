#Don't change the code below 
student_heights= input('Enter a list of student heigths\n> ').split()
# len 

n=0
for i in student_heights:
    n+=1
print(n)


for n in range(0, len(student_heights)):
    student_heights[n] =int(student_heights[n])


# total=0
# for i in student_heights:
#     total+=i

total= sum(student_heights)


mean =round(total/len(student_heights))
print(f"The average hight is: {mean}")