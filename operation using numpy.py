import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print("Original Array:", arr)

added_arr = arr + 5
print("Array after adding 5:", added_arr)

multiplied_arr = arr * 2
print("Array after multiplying by 2:", multiplied_arr)

print("Sum of all elements:", np.sum(arr))
print("Mean (Average):", np.mean(arr))
print("Maximum value:", np.max(arr))
print("Minimum value:", np.min(arr))

print("First element:", arr[0])
print("Elements from index 1 to 3:", arr[1:4])
