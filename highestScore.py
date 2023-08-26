# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
sequence = 0
print(student_scores)

lenghtOflist = 0

for x in student_scores :
  lenghtOflist += 1

print(lenghtOflist)  

def maxFuction(*args):
   
  if lenghtOflist ==1:
     sequence = args[0]
  else :
    sequence = args
 
   
largest = sequence[0]  

for item in sequence:
 if  item > largest:
   largest = item

return largest

number = 
  
  