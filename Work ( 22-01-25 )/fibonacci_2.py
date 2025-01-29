n1 , n2 = 0 , 1
n3 = 0
a=int(input("Enter the number of terms in fibonnaci series : "))
print("Fibonacci series : {} ,{} ,",)
for i in range(1,a-2):
    n3 = n1 + n2
    print("{}".format(n3,end=" "))
    n1 = n2
    n2 = n3