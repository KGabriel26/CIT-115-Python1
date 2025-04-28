# Author: Kasha Gabriel
# Date: 02/20/2025
# Purpose: Inter Planetary Weights

# CONSTANTS (Surface Gravity for each planet)
fSURFACE_GRAVITY_MERCURY= 0.38
fSURFACE_GRAVITY_VENUS= 0.91
fSURFACE_GRAVITY_MOON= 0.165
fSURFACE_GRAVITY_MARS= 0.38
fSURFACE_GRAVITY_JUPITER= 2.34
fSURFACE_GRAVITY_SATURN= 0.93
fSURFACE_GRAVITY_URANUS= 0.92
fSURFACE_GRAVITY_NEPTUNE= 1.12
fSURFACE_GRAVITY_PLUTO= 0.066

# Step 1: Input and Conversion
sName= input("What is your name: ")
fEarthWeight= float(input("What is your weight: "))

# Step 2: Calculate
fTotalWeight1= fEarthWeight * fSURFACE_GRAVITY_MERCURY
fTotalWeight2= fEarthWeight * fSURFACE_GRAVITY_VENUS
fTotalWeight3= fEarthWeight * fSURFACE_GRAVITY_MOON
fTotalWeight4= fEarthWeight * fSURFACE_GRAVITY_MARS
fTotalWeight5= fEarthWeight * fSURFACE_GRAVITY_JUPITER
fTotalWeight6= fEarthWeight * fSURFACE_GRAVITY_SATURN
fTotalWeight7= fEarthWeight * fSURFACE_GRAVITY_URANUS
fTotalWeight8= fEarthWeight * fSURFACE_GRAVITY_NEPTUNE
fTotalWeight9= fEarthWeight * fSURFACE_GRAVITY_PLUTO

# Step 3: Output
print(f"{sName} here are your weights on our Solar System's planets:")
print(f"{'Weight on Mercury:':21s} {fTotalWeight1:10,.2f}")
print(f"{'Weight on Venus:':21s} {fTotalWeight2:10,.2f}")
print(f"{'Weight on our Moon:':21s} {fTotalWeight3:10,.2f}")
print(f"{'Weight on Mars:':21s} {fTotalWeight4:10,.2f}")
print(f"{'Weight on Jupiter:':21s} {fTotalWeight5:10,.2f}")
print(f"{'Weight on Saturn:':21s} {fTotalWeight6:10,.2f}")
print(f"{'Weight on Uranus:':21s} {fTotalWeight7:10,.2f}")
print(f"{'Weight on Neptune:':21s} {fTotalWeight8:10,.2f}")
print(f"{'Weight on Pluto:':21s} {fTotalWeight9:10,.2f}")
