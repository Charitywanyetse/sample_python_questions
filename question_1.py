# Question 1(i)
# Temperature Classifier: Using a function, write a Python script that takes a temperature as input and classifies it into the 
# following categories: 
# Below 0°C: Freezing
# 0 to 10°C: Cold 
# 11 to 20°C; Moderate 
# 21 to 30°C: Warm 
# Above 30°C: Hot
# 
 def calculateTemperature():
    temperature= int(input("Enter the temperature:\t"))
    if temperature<0:
        print("Freezing")
    elif temperature>=0 and temperature<=10:
        print("Cold")

    elif temperature>=11 and temperature<=20:
        print("Moderate")

    elif temperature>=21 and temperature<=30:
        print("Warm")

    else:
        print("Hot")

# 
#  
# Question 1(ii)

# The volume of a sphere with radius r is (4/3)*pie*r**2. 
# What is the volume of the sphere with radius 8. 
# Use a function and make sure the radius is entered 
# from the keyboard and provide the answer in 1 decimal placedef volumeOfSphere():

 import math
 radius=int(input("Enter the radius of a sphere: "))
 pei=int(input("Enter the pei of a triangle: "))
 radius=(4/3) * pei * radius **2
 print(f"The voluma of a sphere {pei} and radius {radius} is {volumeOfSphere:.2f}")

