#Create and manipulate NumPy arrays . Perform basic operations and indexing on arrays
import numpy as np

# Creating a NumPy array from user input
arr = np.array(list(map(int, input("\nEnter space-separated numbers for NumPy array: ").split())))
print("\nOriginal NumPy Array:", arr)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data Type:", arr.dtype)
# Operations on array
print("\nArray Operations:")
print("Array Squared:", arr ** 2)
print("Array Cubed:", arr ** 3)
print("Array Multiplied by 2:", arr * 2)
print("Array plus 5:", arr + 5)
# Statistical operations
print("\nStatistical Functions:")
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))
# Indexing and slicing
print("\nIndexing and Slicing:")
print("First Element:", arr[0])
print("Last Element:", arr[-1])
print("First Three Elements:", arr[:3])
print("Last Three Elements:", arr[-3:])
print("Reversed Array:", arr[::-1])
# Reshaping array
rows = int(input("\nEnter number of rows to reshape: "))
cols = int(input("Enter number of columns to reshape: "))
if rows * cols == arr.size:
    reshaped_arr = arr.reshape(rows, cols)
    print("Reshaped Array:\n", reshaped_arr)
else:
    print("Error! Reshape size does not match the total elements.")
# Matrix operations
print("\nCreating and Manipulating Matrices:")
matrix1 = np.random.randint(1, 10, (3, 3))
matrix2 = np.random.randint(1, 10, (3, 3))
print("Matrix 1:\n", matrix1)
print("Matrix 2:\n", matrix2)
print("Matrix Addition:\n", matrix1 + matrix2)
print("Matrix Multiplication:\n", np.dot(matrix1, matrix2))
print("Matrix Transpose:\n", matrix1.T)
# Special arrays
print("\nSpecial NumPy Arrays:")
print("Zeros Array:\n", np.zeros((3, 3)))
print("Ones Array:\n", np.ones((3, 3)))
print("Identity Matrix:\n", np.eye(3))
print("Random Matrix:\n", np.random.rand(3, 3))