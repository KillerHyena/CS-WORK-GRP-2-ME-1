def palindrome(n):
    char_list = list(n)
    reversed_list = char_list[::-1]
    reversed_string = "".join(reversed_list)
    print("Reversed String:", reversed_string)
    if n == reversed_string:
        print(n, "is a palindrome string")
    else:
        print(n, "is not a palindrome string")
string = input("Enter a string: ")
print("Original String:", string)
palindrome(string)