# Question 2(i)

# Define a function named calculate_bmi that takes a person's weight (in kilograms) and height (in 
# meters) as parameters and returns their BMI. (BMI = weight/height) 
# Calculate and sen their BMI category: 
# Below 18.5: "Underweight" 
# 18.5 to 24.9: "Normal weight" 
# 25 to 29.9: "Overweight" 
# 30 or above: "Obese" 

# Answers





# Question 2(ii)

# Use a function to calculate the volume of a cylinder V = π r2 h.
#  Choose a function name in line with what you want to 
# achieve. Radius r and height h should be in parameters.
#  Make sure you use the real pie value (import math)

# Answers

import math
radius = int(input("Enter the radius of the cylinder: "))
height = int(input("Enter the height of the cylinder: "))
pie = math.pi
volume = pie * radius**2 * height
print(volume)


