#Import and use functions from external packages (e.g., math, random)
import math
import random
import datetime
import statistics
# Using math module
num = float(input("\nEnter a number for mathematical operations: "))
print("\nMath Module Functions:")
print(f"Square root of {num}: {math.sqrt(num)}")
print(f"Logarithm (base 10) of {num}: {math.log10(num)}")
print(f"Sine of {num}°: {math.sin(math.radians(num))}")
# Using random module
print("\nRandom Module Functions:")
print("Random integer (1-100):", random.randint(1, 100))
print("Random choice from list:", random.choice(["Apple", "Banana", "Cherry", "Mango"]))
# Using datetime module
current_time = datetime.datetime.now()
print("\nDatetime Module Functions:")
print("Current Date & Time:", current_time)
print("Current Year:", current_time.year)
print("Current Month:", current_time.strftime("%B"))
# Using statistics module
data = list(map(int, input("\nEnter a list of numbers separated by spaces: ").split()))
print("\nStatistics Module Functions:")
print(f"Mean (Average): {statistics.mean(data)}")
print(f"Median: {statistics.median(data)}")
print(f"Mode: {statistics.mode(data)}")
print(f"Standard Deviation: {statistics.stdev(data)}")