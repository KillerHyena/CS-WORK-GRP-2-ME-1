#Implement a simple calculator using conditional statements
num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number : "))
op1=input("Enter the arithimatic operation between first and second number : ")
if op1=='+' :
    print("The final result :", num1+num2)
elif op1=='-' :
    print("The final result :", num1-num2)
elif op1=='*' :
    print("The final result :", num1*num2)
elif op1=='/' :
    print("The final result :", num1/num2)
else:
    print("Invalid Input")