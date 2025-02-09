#Write a Python program to print the Fibonacci series using a for loop
a, b = 0, 1
n = int(input("Enter the number of terms in the Fibonacci series: "))
print(f"Fibonacci series with {n} terms is:", end=" ")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()