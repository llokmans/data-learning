import numpy as np

numbers = np.array([1, 2, 3, 4, 5])
print(numbers)
print(type(numbers))
print(numbers * 2)
print(numbers + 10)
print(numbers.sum())
print(numbers.mean())
print(numbers.max())


print(numbers[numbers > 2])