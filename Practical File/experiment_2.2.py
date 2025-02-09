#Write a Python program to print the Fibonacci series using a for loop
a , b = 0 , 1
n = int(input("Enter the number of terms in the fibonacci series : "))
for i in range(n):
    print(a)
    a , b = b , a + b