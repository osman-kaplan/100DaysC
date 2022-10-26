students_scores=input('Enter the student\'s scores: > ')

# # find the max or of the scores

# for i in students_scores:
#     for n in range(0,(len(students_scores))):
#         if i < students_scores[n]:

#Creating a list of the scores
students_scores= students_scores.split()

# type conversiton from str to int
for n in range(0,(len(students_scores)-1) ):
    students_scores[n]=int(students_scores[n])
print(students_scores)
print(type(students_scores))
print(type(students_scores[0]))





# find the max or of the scores
higher_score=0
for score in students_scores:
    if int(score) > higher_score:
        higher_score=score

print(f"The highest score in the class is: {higher_score}.")
            
        
    
      










# find the min of the scores
