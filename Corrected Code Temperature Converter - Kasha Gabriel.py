#Author: Kasha Gabriel
#Date: 3/14/2025
#Purpose: Code Temperature Converter


# Step 1: Input and Conversions

sWelcome = input("Kasha's Temp Converter: \n")
fTemp = float(input("Enter a temperature: "))
sType = input("Is the temp F for Fahrenheit or C for Celsius? ")

# Step 2: Output - Calculations for converting Fahrenheit to Celsius and vice versa

if sType == "F" or sType == "f":
    if fTemp > 212:
        print("Temp can not be > 212")
    else:
        print(f"The Celsius equivalent is: {(5.0 / 9) * (fTemp - 32):,.1f} ")
elif sType == "C" or sType == "c":
    if fTemp > 100:
        print("Temp can not be > 100")
    else:
        print(f"The Fahrenheit equivalent is: {((9.0 / 5.0) * fTemp) + 32:,.1f}")
else:
    print('Enter a F or C')
