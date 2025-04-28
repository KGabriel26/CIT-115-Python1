# AUTHOR: Kasha Gabriel
# DATE: 04/12/2025
# PURPOSE: Compound Interest with Loops

#Step 1: Input and Conversions

#Obtain Original Deposit Amount

#fOriginalDeposit = 0
while True:
    try:
        fOriginalDeposit = float(input("What is the Original Deposit (positive value): "))
        if fOriginalDeposit <= 0:
            print("Input must be > 0")
            continue
        break
    except ValueError:
        print("Input must be a positive numeric value")

#Obtain the Interest Rate

#fInterestRate = 0
while True:
    try:
        fInterestRate = float(input("What is the Interest Rate (positive value): "))
        if fInterestRate <= 0:
            print("Input must be > 0")
            continue
        break
    except ValueError:
        print("Input must be a positive numeric value")

#Obtain the number of months interest will be applied

#iMonth = 0
while True:
    try:
        iMonths = int(input("What is the Number of Months (positive value): "))
        if iMonths <= 0:
            print("Input must be > 0")
            continue
        break
    except ValueError:
        print("Input must be a positive numeric value")

#Obtain the amount desired to be saved after interest has accrued

#iGoalAmount = 0
while True:
    try:
        fGoalAmount = float(input("What is the Goal Amount (Can enter 0, but not negative): "))
        if fGoalAmount < 0:
            print("Input must be 0 or greater")
            continue
        break
    except ValueError:
        print("Input must be a 0 or positive numeric value")

#Step 2: Calculate

#Rename previously used variables and identify the monthly balance with the respective interest accrual calculated in

fAccountBalance = fOriginalDeposit
iMonthlyInterestRate = (fInterestRate / 100) / 12

for iMonth in range (1, iMonths + 1):
    fAccountBalance += fAccountBalance * iMonthlyInterestRate
    print(f"Month: {iMonth: >2}  Account Balance is: $ {fAccountBalance:,.2f}")
    iMonth += 1

if fOriginalDeposit < fGoalAmount and fGoalAmount > 0.0:
    iMonth = 0
    while fOriginalDeposit < fGoalAmount:
         fOriginalDeposit += fOriginalDeposit * iMonthlyInterestRate
         iMonth += 1
    print(f"It will take: {iMonth} months to reach a goal of $ {fGoalAmount:,.2f}")
