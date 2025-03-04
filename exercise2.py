# Get user input for grade percentage
gradePercentage = float(input("Enter your grade percentage from 0 - 100: "))

# Classify the grade inpuuted from the promth
if gradePercentage >= 90:
    print("A (Excellent)")
elif gradePercentage >= 80:
    print("B (Good)")
elif gradePercentage >= 70:
    print("C (Average)")
elif gradePercentage >= 60:
    print("D (Needs Improvement)")
else:
    print("F (Fail)")