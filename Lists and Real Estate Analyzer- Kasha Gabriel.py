#AUTHOR: KASHA GABRIEL
#DATE: 5/10/2025
#PURPOSE: LISTS AND REAL ESTATE ANALYZER

# Define the Floating Point Input Function
def getFloatInput(sPrompt):
    while True:
        try:
            fValue = float(input(sPrompt))
            if fValue <= 0:
                raise ValueError
            return fValue
        except ValueError:
            print("Input a number that is greater than 0.")

#Define the getMedian Function to calculate the median of a list whose length is even or odd

def getMedian(SalePriceList):
    iMiddleIndex = len(SalePriceList) // 2

    if len(SalePriceList) % 2 == 0:
        return (SalePriceList[iMiddleIndex] + SalePriceList[iMiddleIndex - 1]) / 2
    else:
        return SalePriceList[iMiddleIndex]

#Define Main Function to obtain the property values and add them to the list
#Call the getFloatInput Function
#Create an empty list, so I can build it
def main():
    SalePriceList = []

    while True:
        fSalePrice = getFloatInput("Enter property sales value: ")
        SalePriceList.append(fSalePrice)
        while True:
            sAddToList = input("Enter another value Y or N:").upper()
            if sAddToList in ["Y", "N"]:
                break
            print("Please enter a Y or N.")
        if sAddToList == "N":
            break
#i = Index
#Sort the list from least to greatest and assign variables for the desired outputs

    SalePriceList.sort()
    fMinimum = SalePriceList[0]
    fMaximum = SalePriceList[-1]
    fTotal = sum(SalePriceList)
    fAverage = fTotal / len(SalePriceList)
    fMedian = getMedian(SalePriceList)
    fCommission = fTotal * 0.03

#OUTPUT
    for i in range(len(SalePriceList)):
        print(f"Property {i + 1} ${SalePriceList[i]: 13,.2f}")
    print(f"Minimum:     ${fMinimum: 15,.2f}")
    print(f"Maximum:     ${fMaximum: 15,.2f} ")
    print(f"Total:       ${fTotal: 15,.2f}")
    print(f"Average:     ${fAverage: 15,.2f}")
    print(f"Median:      ${fMedian: 15,.2f}")
    print(f"Commission:  ${fCommission: 15,.2f}")

#Call the Main Function
main()

