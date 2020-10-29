eren = {
  "name": "Eren",
  "homework": [90.0,97.0,75.0,92.0],
  "quizzes": [88.0,40.0,94.0],
  "tests": [75.0,90.0]
}
mikasa = {
 "name": "Mikasa",
 "homework": [100.0, 92.0, 98.0, 100.0],
 "quizzes": [82.0, 83.0, 91.0],
 "tests": [89.0, 97.0]
}

armin = {
"name": "Armin",
"homework": [0.0, 87.0, 75.0, 22.0],
"quizzes": [0.0, 75.0, 78.0],
"tests": [100.0, 100.0]
}

student = [eren, mikasa, armin]

for student in student:
    print("\nStudent Data: ")
    for x in student:
        print("{}:{}".format(x,student[x]))

def average(z):
    total = sum(z)
    float(total)
    result = total / len(z)
    return result 
print("this is average for Eren",average(eren["homework"]))
print("this is average for Mikasa",average(mikasa["homework"]))
print("this is average for Armin",average(armin["homework"]))

Homework_Weight ={
  "Hw": [average(eren["homework"]),
  average(mikasa["homework"]),
  average(armin["homework"])]
  }
print("sum of all homework weighted: ",sum(Homework_Weight["Hw"])*.1)

quiz_weight = {
  "quiz": [average(eren["quizzes"]),
  average(mikasa["quizzes"]),
  average(armin["quizzes"])]
  }
print("sum of all quiz weighted: ",sum(quiz_weight["quiz"])*.3)

Test_wght = {
  "test": [average(eren["tests"]),
  average(mikasa["tests"]),
  average(armin["tests"])]
  }
print("sum of all test weighted: ",sum(Test_wght["test"])*.6)

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    
    homework = homework * 0.1
    quizzes = quizzes * 0.3
    tests = tests * 0.6
    return homework + quizzes + tests


print(get_letter_grade(int(get_average(mikasa))))
print(get_letter_grade(int(get_average(eren))))
print(get_letter_grade(int(get_average(armin))))