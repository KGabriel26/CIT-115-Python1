#Author: Kasha Gabriel
#Date: 3/5/2025
#Purpose: Code Temperature Converter


# Step 1: Input and Conversions

sWelcome = input("Kasha's Temp Converter: \n")
fTemp = float(input("Enter a temperature: "))
sType = input("Is the temp F for Fahrenheit or C for Celsius? ")

# Step 2: Calculations - Formulas for Converting Fahrenheit to Celsius and vice vera

fCelsius = (5.0 / 9) * (fTemp - 32)
fFahrenheit = ((9.0 / 5.0) * fTemp) + 32

# Step 3: Output 

if sType == "F" or sType == "f":
    if fTemp > 212:
        print("Temp can not be > 212")
    if fTemp <= 212:
        print(f"The Celsius equivalent is: {fCelsius:,.1f} ")
elif sType == "C" or sType == "c":
    if fTemp > 100:
        print("Temp can not be > 100")
    if fTemp <= 100:
        print(f"The Fahrenheit equivalent is: {fFahrenheit:,.1f}")
else:
    print('Enter a F or C')
