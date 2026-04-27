name = input("What is your name? ")
year = input("Which grade are you in? ")

print("Hey " + name + "! Year " + year  + ".")
print("")

print("Enter your scores for 8 subjects (0 - 100)")
print("")

firstSubject = input("First subject name: ")
firstScore = float(input("Score for " + firstSubject + ": "))

secondSubject = input("Second subject name: ")
secondScore = float(input("Score for " + secondSubject + ": "))

thirdSubject = input("Third subject name: ")
thirdScore = float(input("Score for " + thirdSubject + ": "))

fourthSubject = input("Fourth subject name: ")
fourthScore = float(input("Score for " + fourthSubject + ": "))

fifthSubject = input("Fifth subject name: ")
fifthScore = float(input("Score for " + fifthSubject + ": "))

sixthSubject = input("Sixth subject name: ")
sixthScore = float(input("Score for " + sixthSubject + ": "))

seventhSubject = input("Seventh subject name: ")
seventhScore = float(input("Score for " + seventhSubject + ": "))

eightSubject = input("Eigth subject name: ")
eigthScore = float(input("Score for " + eightSubject + ": "))


subjects = [firstSubject, secondSubject, thirdSubject, fourthSubject, fifthSubject, sixthSubject, seventhSubject, eightSubject]
scores = [firstScore, secondScore, thirdScore, fourthScore, fifthScore, sixthScore, seventhScore, eigthScore]
grades = []
points = []

# convert each score to a letter grade and grade point
for i in range(len(scores)):
    if scores[i] >= 90:
        grades.append("A")
        points.append(4)
    elif scores[i] >= 80:
        grades.append("B")
        points.append(3)
    elif scores[i] >= 70:
        grades.append("C")
        points.append(2)
    elif scores[i] >= 60:
        grades.append("D")
        points.append(1)
    else:
        grades.append("F")
        points.append(0)

total = points[0] + points[1] + points[2] + points[3] + points[4] + points[5] + points[6] + points[7]
average = (scores[0] + scores[1] + scores[2] + scores[3] + scores[4] + scores[5] + scores[6] + scores[7]) / 8
average = round(average, 2)
gpa = total / 8
gpa = round(gpa, 2)
has_f = "F" in grades
all_passed = "F" not in grades
has_a = "A" in grades

print("")
print("YOUR GRADES:")
for i in range(len(subjects)):
    print(subjects[i] + ": " + str(scores[i]) + " — " + grades[i] + " (" + str(points[i]) + " pts)")

print("")
print("Average score: " + str(average) + " / 100")
print("Total points : " + str(total))
print("GPA          : " + str(gpa) + " / 4.0")
print("Has an F     : " + str(has_f))
print("All passed   : " + str(all_passed))
print("Has an A     : " + str(has_a))

print("")
if gpa >= 3.7:
    print("Rating: A - Amazing grades!")
elif gpa >= 3.0:
    print("Rating: B - Above average grades")
elif gpa >= 2.0:
    print("Rating: C - Average grades")
elif gpa >= 1.0:
    print("Rating: D - Below average grades")
else:
    print("Rating: F - Failing grades")

if has_f == True:
    print("Warning: you have a failing grade!")
else:
    print("No failing grades. Good job!")

print("")
print("IMPROVEMENT TIPS")
tips = []

for i in range(len(grades)):
    if grades[i] == "F" or grades[i] == "D":
        tips.append("Study more for " + subjects[i])
    elif grades[i] == "C":
        tips.append("A bit more effort in " + subjects[i] + " could get you a B")

if len(tips) == 0:
    print("No major issues - maintain your grades!")
else:
    for i in range(len(tips)):
        print(str(i + 1) + ". " + tips[i])

print("")
print("Good luck " + name + "!")