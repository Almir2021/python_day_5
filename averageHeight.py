# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

avrageHeight = 0   
numberOfStudents = 0



for height in student_heights :
  avrageHeight += height
  numberOfStudents += 1




avrageHeight /= numberOfStudents

roundNumber = round(avrageHeight,0)

roundNumber= str(roundNumber)
print(roundNumber[0]+roundNumber[1]+ roundNumber[2])