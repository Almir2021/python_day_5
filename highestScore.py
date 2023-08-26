# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
sequence = student_scores


lenghtOflist = 0

for x in student_scores :
  lenghtOflist += 1

 

   
if lenghtOflist ==1:
     sequence = student_scores[0]
else :
    sequence =  student_scores
 
   
largest = sequence[0]  

for item in sequence:
 if  item > largest:
   largest = item

print(f"The highest score in the class is:{largest}")


  
  