# Author: Kasha Gabriel
# Date: 02/25/2025
# Purpose: Compound Interest


# Step 1: Input and Conversions (Prompt user for variables)
fPrincipalValue = float(input("Enter the starting principal: ")) #PV
fInterestRate = float(input("Enter the annual interest rate: ")) #R
fCompounding = float(input("How many times per year is the interest compounded? ")) #M
iNumberOfPeriods = int(input("For how many years will the account earn interest? ")) #T

# Step 2: Calculate (FV = PV * (1 + (R/M)) ** MT)
fFutureValue = fPrincipalValue * (1 + (fInterestRate / 100) / fCompounding) ** (fCompounding * iNumberOfPeriods)

# Step 3: Output
print(f"At the end of {iNumberOfPeriods} years you will have $ {fFutureValue:,.2f}")
