# Author: Kasha Gabriel
# Date: 3/29/2025
# Purpose: Grade Analyzer

# Step 1: Receive test scores
sName = input("Name of person that we are calculating the grades for: ")
iTest1= int(input("Test 1: "))
iTest2= int(input("Test 2: "))
iTest3= int(input("Test 3: "))
iTest4= int(input("Test 4: "))
sDropLowest= input("Do you wish to drop the lowest grade Y or N? ").upper()

# Step 2: Determine score validity
if iTest1 < 0 or iTest2 < 0 or iTest3 < 0 or iTest4 < 0:
    print("Test scores must be greater than 0")
    exit()

#Step 3: Identify the lowest grade, calculate average and assign letter grade

#Drop the lowest grade
if sDropLowest == "Y" :
    if iTest1 <= iTest2 and iTest1 <= iTest3 and iTest1 <= iTest4:
        iLowestGrade = iTest1
    elif iTest2 <= iTest3 and iTest2 <= iTest4:
        iLowestGrade = iTest2
    elif iTest3 <= iTest4:
        iLowestGrade = iTest3
    else:
        iLowestGrade = iTest4
elif sDropLowest == "N":
    fAverage = (iTest1 + iTest2 + iTest3 + iTest4 - iLowestGrade) / 4
else:
    print("Enter Y or N to Drop the Lowest Grade.")
    exit()

# Assign a Letter Grade to the average
if fAverage >= 97.0:
    sLetterGrade = "A+"
elif fAverage >= 94.0:
    sLetterGrade = "A"
elif fAverage >= 90.0:
    sLetterGrade = "A-"
elif fAverage >= 87.0:
    sLetterGrade = "B+"
elif fAverage >= 84.0:
    sLetterGrade = "B"
elif fAverage >= 80.0:
    sLetterGrade = "B-"
elif fAverage >= 77.0:
    sLetterGrade = "C+"
elif fAverage >= 74.0:
    sLetterGrade = "C"
elif fAverage >= 70.0:
    sLetterGrade = "C-"
elif fAverage >= 67.0:
    sLetterGrade = "D+"
elif fAverage >= 64.0:
    sLetterGrade = "D"
elif fAverage >= 60.0:
    sLetterGrade = "D-"
else:
    sLetterGrade= "F"

print(f"{sName} test average is: {fAverage:.1f}")
print(f"Letter Grade for the test is: {sLetterGrade}")
