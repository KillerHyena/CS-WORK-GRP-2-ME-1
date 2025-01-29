def palindrome(n):
    string = n[::-1]
    print("Reversed String : " , string )
    if n == string :
        print(str , "is a palindrome string")
    else:
        print(str , "is not a palindrome string")

str = input("Enter a sring : ")
print("Original String : " , str )
palindrome(str)
'''string = str[::-1]
print("Reversed String : " , string )
if str == string :
    print(str , "is a palindrome string")
else:
    print(str , "is not a palindrome string")'''