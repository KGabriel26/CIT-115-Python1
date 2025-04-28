# AUTHOR: KASHA GABRIEL
# DATE: 4/26/2025
# PURPOSE: PAINT JOB W/ FUNCTIONS AND OUTPUT FILES

# Import the Ceil Function from the Math Module
from math import ceil

# Define the Floating Point Input Function
def getFloatInput(sPrompt):
    while True:
        try:
            fValue = float(input(sPrompt))
            if fValue <= 0:
                raise ValueError
            return fValue
        except ValueError:
            print("Please enter a valid number that is > 0.")

# Define Functions for Gallons of Paint, Labor Hours, Labor Cost, Paint Cost, & Tax Rate using the specified parameters
# Use Ciel to round the number of paint gallons up to the next whole number if applicable

def getGallonsOfPaint(fSqFtOfWall, fFeetPerGallon):
    return ceil(fSqFtOfWall / fFeetPerGallon)

def getLaborHours(fHoursPerGallon, iTotalGallons):
    return fHoursPerGallon * iTotalGallons

def getLaborCost(fHoursPerGallon, fHourlyLaborCharge):
    return fHoursPerGallon * fHourlyLaborCharge

def getPaintCost(iTotalGallons, fPaintPrice):
    return iTotalGallons * fPaintPrice

def getSalesTax(sState):
    if sState == "CT" or sState == "VT":
        return 0.06
    elif sState == "MA":
        return 0.0625
    elif sState == "ME":
        return 0.085
    elif sState == "RI":
        return 0.07
    else:
        return 0.0

# Define showCostEstimate Function to include final calculations and introduce file name
def showCostEstimate(iTotalGallons, fTotalLaborHrs, fTotalPaintCost, fTotalLaborCharge, fTaxRate, sLastName):
    fTotalTax = fTaxRate * (fTotalLaborCharge + fTotalPaintCost)
    fTotalCost = fTotalTax + fTotalLaborCharge + fTotalPaintCost
    sFileName = f"{sLastName}_PaintJobOutput.txt"

# Output results to screen
    print(f"Gallons of paint: {iTotalGallons}")
    print(f"Hours of labor: {fTotalLaborHrs:.1f}")
    print(f"Paint charges: ${fTotalPaintCost:,.2f}")
    print(f"Labor charges: ${fTotalLaborCharge:,.2f}")
    print(f"Tax: ${fTotalTax:,.2f}")
    print(f"Total cost: ${fTotalCost:,.2f}")

# Open file and write results using the file alias ¨k¨
    with open(sFileName, "w") as k:

        k.write(f"Gallons of paint: {iTotalGallons}\n")
        k.write(f"Hours of labor: {fTotalLaborHrs:.1f}\n")
        k.write(f"Paint charges: ${fTotalPaintCost:,.2f}\n")
        k.write(f"Labor charges: ${fTotalLaborCharge:,.2f}\n")
        k.write(f"Tax: ${fTotalTax:,.2f}\n")
        k.write(f"Total cost: ${fTotalCost:,.2f}\n")

    print(f"File: {sFileName} was created.")

#Define the Main Function - Include prompts and Function calculations
def main():
    fSqFtOfWall = getFloatInput("Enter wall space in square feet: ")
    fPaintPrice = getFloatInput("Enter paint price per gallon: ")
    fFeetPerGallon = getFloatInput("Enter feet per gallon: ")
    fHoursPerGallon = getFloatInput("How many labor hours per gallon: ")
    fHourlyLaborCharge = getFloatInput("Labor charge per hour: ")

# Utilize the Main Function to also prompt for strings
    sState = input("State job is in (initials): ").upper()
    sLastName = input("Customer Last Name: ").title()

# Assign Variables that include Function calculations
    iTotalGallons = getGallonsOfPaint(fSqFtOfWall, fFeetPerGallon)
    fTotalLaborHrs = getLaborHours(fHoursPerGallon, iTotalGallons)
    fTotalPaintCost = getPaintCost(iTotalGallons, fPaintPrice)
    fTotalLaborCharges = getLaborCost(fHoursPerGallon, fHourlyLaborCharge) * iTotalGallons
    fTaxRate = getSalesTax(sState)

# Call showCostEstimate Function and receive necessary variables
    showCostEstimate(
        iTotalGallons,
        fTotalLaborHrs,
        fTotalPaintCost,
        fTotalLaborCharges,
        fTaxRate,
        sLastName
    )
# Call Main Function
main()
