gpa = float(input("Please input your GPA ! "))

lowest_grade = input("Please input your lowest grade !! ")

lowest_grade= float(lowest_grade)

# if gpa >= .085:
#     if lowest_grade >= 0.70:
#         print("You made honour roll")

# if gpa >= .085 and lowest_grade >= 0.70:
#         print("You made honour roll")


if gpa>=.85 and lowest_grade >=.70:
    honour_roll=True
else:
    honour_roll=False

if honour_roll:
    print("You made honour roll!")


