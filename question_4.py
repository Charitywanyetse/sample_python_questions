#Question 4(i)

# Create a list of five of your favorite foods. Write a Python program to:
# Add two more items to the list.
# Remove one item from the list.
# Print the updated list.

# Answers
favorite_foods = [
    "Pizza",
    "Rice",
    "Mattoke",
    "Ice Cream",
    "Chicken"
]
print(favorite_foods)

favorite_foods.append("Irish potatoes")
favorite_foods.append("posho")
print(favorite_foods)

favorite_foods.remove("posho")
print(favorite_foods)




#Question 4(ii)

# Given the list numbers = [2, 5, 8, 10, 3, 6], write a Python program to:
# Print the first and last elements of the list.
# Print the list in reverse order.
# Calculate and print the sum of all the elements in the list.

# Answers

numbers = [2, 5, 8, 10, 3, 6]
print("First element:", numbers[0])
print("Last element:", numbers[-1])

print("\nReverse list:", numbers[::-1])

sum_of_numbers = sum(numbers)
print("\nsum of elements:", sum_of_numbers)


