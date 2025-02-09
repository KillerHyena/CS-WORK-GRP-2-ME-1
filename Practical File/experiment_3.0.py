#Implement a function to check if a given string is a palindrome
string = input("Enter the string: ")
string_1 = string[::-1]
print(f"Original String : {string}")
print(f"Reversed String : {string_1}")
if string == string_1 :
    print(f"{string} is a palindrome")
elif string != string_1 :
    print(f"{string} is not a palindrome")
else :
    print(f"{string} is an invalid Input")