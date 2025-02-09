#Write a Python program to check if a number is even or odd
def odd_even(n):
    if n % 2 == 0:
        print(f"{n} is an even number")
    elif n % 2 != 0:
        print(f"{n} is an odd number")
    else:
        print("Wnter a valid number")
def  main():
    m=int(input("Enter a number : "))
    odd_even(m)
main()