studenScore = input ("Give me resolts. ").split()
for n in range(0, len(studenScore)):
    studenScore[n] = int(studenScore[n])
print(studenScore)

numberOfScores = 0
for x in studenScore :
        numberOfScores +=1 

print(numberOfScores)

smallestScore = studenScore[0]

for n in studenScore :
      if n < smallestScore:
            smallestScore = n

print(smallestScore)          
