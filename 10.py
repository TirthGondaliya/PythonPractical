import numpy as np

# 1. Create a NumPy array from a list or tuple
arr = np.array([1, 2, 3, 4, 5])
print("\n1. Array from list:", arr)

# 2. Create an array filled with zeros
zeros_arr = np.zeros((2, 3))  # 2 rows, 3 columns
print("\n2. Zeros array:\n", zeros_arr)

# 3. Create an array filled with ones
ones_arr = np.ones((3, 2))  # 3 rows, 2 columns
print("\n3. Ones array:\n", ones_arr)

# 4. Create an array with a range of values
range_arr = np.arange(0, 10, 2)  # Start, end (exclusive), step
print("\n4. Range array:", range_arr)

# 5. Create an array with evenly spaced values over a specified interval
linspace_arr = np.linspace(0, 10, 5)  # Start, end, number of points
print("\n5. Linspace array:", linspace_arr)

# 6. Change the shape of an array without changing its data
reshape_arr = np.arange(6).reshape(2, 3)  # Reshape to 2 rows, 3 columns
print("\n6. Reshaped array:\n", reshape_arr)

# 7. Convert a multi-dimensional array into a 1D array
flatten_arr = reshape_arr.flatten()
print("\n7. Flattened array:", flatten_arr)

# 8. Transpose an array (swap rows and columns)
transpose_arr = reshape_arr.T
print("\n8. Transposed array:\n", transpose_arr)

# 9. Join two or more arrays along an axis
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
concat_arr = np.concatenate((arr1, arr2))  # Default axis=0
print("\n9. Concatenated array:", concat_arr)

# 10. Split an array into multiple sub-arrays
split_arr = np.split(concat_arr, 3)  # Split into 3 equal parts
print("\n10. Split array:", split_arr)

# 11. Stack arrays vertically (row-wise)
vstack_arr = np.vstack((arr1, arr2))
print("\n11. Vertically stacked array:\n", vstack_arr)

# 12. Stack arrays horizontally (column-wise)
hstack_arr = np.hstack((arr1.reshape(3, 1), arr2.reshape(3, 1)))
print("\n12. Horizontally stacked array:\n", hstack_arr)

# 13. Append values to the end of an array
append_arr = np.append(arr1, [7, 8, 9])
print("\n13. Appended array:", append_arr)

# 14. Delete elements from an array along a specified axis
delete_arr = np.delete(arr1, 1)  # Delete element at index 1
print("\n14. Deleted array:", delete_arr)

# 15. Insert values into an array at specified positions
insert_arr = np.insert(arr1, 1, 99)  # Insert 99 at index 1
print("\n15. Inserted array:", insert_arr)

# 16. Access an element of an array at index i
print("\n16. Element at index 2:", arr[2])

# 17. Slice an array from index i to j (exclusive)
print("\n17. Sliced array (1:4):", arr[1:4])

# 18. Slice an array with a step between start and end
print("\n18. Sliced array with step (0:5:2):", arr[0:5:2])

# 19. Access all elements along rows and columns (for 2D arrays)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n19. Access all elements in 2D array:\n", arr_2d[:, :])
