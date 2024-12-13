import math

student_scores = [150, 142, 185, 120, 171, 184, 149,
                  24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# 1 option
print(max(student_scores))
# 2 second
maxValue = 0
for score in student_scores:
    if score > maxValue:
        maxValue = score
print(maxValue)
