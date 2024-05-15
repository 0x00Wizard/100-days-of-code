print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

full_name = name1 + name2

countT, countL = 0, 0
letterT, letterL = "TRUE", "LOVE"


for i in full_name.lower():
    for j in letterT.lower():
        if j == i:
            countT += 1

for i in full_name.lower():
    for j in letterL.lower():
        if j == i:
            countL += 1

score = int(str(countT) + str(countL))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")

elif 40 >= score <= 50:
    print(f"Your score is {score}, you are alright together.")

else:
    print(f"Your score is {score}.")