#Use lambda functions, map, and filter to perform operations on a list
# Taking user input for the list
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
# Using map() to square each number
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared Numbers:", squared_numbers)
# Using filter() to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)
# Using filter() to get odd numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("Odd Numbers:", odd_numbers)
# Using map() to double each number
doubled_numbers = list(map(lambda x: x * 2, numbers))
print("Doubled Numbers:", doubled_numbers)
# Using filter() to get numbers greater than 10
greater_than_ten = list(filter(lambda x: x > 10, numbers))
print("Numbers Greater Than 10:", greater_than_ten)