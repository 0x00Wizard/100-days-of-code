student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
student_grades = {}


for key, val in student_scores.items():
    if val > 90:
      student_grades[key] = "Outstanding"

    elif 80 < val <= 90:
      student_grades[key] = "Exceeds Expectations"

    elif 71 < val <= 80:
      student_grades[key] = "Acceptable"

    else:
      student_grades[key] = "Fail"





# 🚨 Don't change the code below 👇
print(student_grades)