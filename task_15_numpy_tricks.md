### `Q-1:` Create a random 3x4 matrix with value between 0-100. And perform below tasks

    i. Sort this matrix. np.sort()
    ii. Sort this matrix based on values in 2nd column.
    iii. Sort this matrix based on max value in each row.
    iv. Sort based on elements value.


See examples:
```
arr =
    [[92 90 74]
    [ 6 63 93]
    [15 93 96]
    [70 60 48]]
```
```
i. np.sort
[[74 90 92]
 [ 6 63 93]
 [15 93 96]
 [48 60 70]]

ii. based on 2nd column
[[70 60 48]
 [ 6 63 93]
 [92 90 74]
 [15 93 96]]

iii. based on row max- ascending
[[15 93 96]
 [ 6 63 93]
 [92 90 74]
 [70 60 48]]

iv. based on elements value
[[ 6 15 48]
 [60 63 70]
 [74 90 92]
 [93 93 96]]

```


```python
import numpy as np

np.random.seed(42)  # For reproducibility (remove for truly random)
arr = np.random.randint(0, 101,12).reshape(3, 4)

print("Original Matrix:")
print(arr)

# i. Sort each row using np.sort()
sorted_rows = np.sort(arr)
print("\ni. np.sort() - sorts each row independently:")
print(sorted_rows)

# ii. Sort rows based on values in the 2nd column (index 1)
# np.argsort gives the indices that would sort the 2nd column
# We use those indices to reorder the entire rows
column_2_indices = np.argsort(arr[:, 1])
sorted_by_col2 = arr[column_2_indices]
print("\nii. Sort based on 2nd column (index 1):")
print(sorted_by_col2)

# iii. Sort rows based on max value in each row (ascending)
# First find the max of each row, then get sort indices for those maxes
row_max_values = np.max(arr, axis=1)
max_sort_indices = np.argsort(row_max_values)
sorted_by_row_max = arr[max_sort_indices]
print("\niii. Sort based on row max (ascending):")
print(sorted_by_row_max)

# iv. Sort all elements and reshape back to original shape
# Flatten the matrix, sort all values, then reshape to 3x4
flat_sorted = np.sort(arr.flatten())
sorted_elements = flat_sorted.reshape(arr.shape)
print("\niv. Sort based on all elements value:")
print(sorted_elements)
```

### `Q-2:` There is an array of marks of 5 students in 4 subjects. Further you are asked to perform below task.
    i. Add marks every student of an extra subject in the same array.
    ii. Add two new students marks in respective 5 subjects.(one subject added in above task)
    iii. Add extra column with sum of all subjects(5-subjects) marks
    iv. Sort the array(non-ascending order) on total marks column--one added in above task. Show top 2 rows.

Note: Change dimension of arrays during concatenation or appending if required.

Given Array-
```
marks = [[13, 10,  9, 33],
       [63, 46, 90, 42],
       [39, 76, 13, 29],
       [82,  9, 29, 78],
       [67, 61, 59, 36]]

extra_subject = [41, 87, 72, 36, 92]
#Two extra students record-
rec1 = [77, 83, 98, 95, 89]
rec2 = [92, 71, 52, 61, 53]
```


```python

marks = np.array([[13, 10,  9, 33],
                  [63, 46, 90, 42],
                  [39, 76, 13, 29],
                  [82,  9, 29, 78],
                  [67, 61, 59, 36]])

extra_subject = [41, 87, 72, 36, 92]
rec1 = [77, 83, 98, 95, 89]
rec2 = [92, 71, 52, 61, 53]

print("Original marks array (shape:", marks.shape, "):")
print(marks)

# i. Add extra subject marks as a new column
# Reshape extra_subject to column vector (5 rows, 1 column) for horizontal stacking
extra_col = np.array(extra_subject).reshape(-1, 1)
marks = np.hstack((marks, extra_col))

print("\ni. After adding extra subject (shape:", marks.shape, "):")
print(marks)

# ii. Add two new students as new rows
new_students = np.array([rec1, rec2])
marks = np.vstack((marks, new_students))

print("\nii. After adding 2 new students (shape:", marks.shape, "):")
print(marks)

# iii. Add total marks column (sum of all 5 subjects)
# Calculate row sums and reshape to column vector
row_totals = np.sum(marks, axis=1).reshape(-1, 1)
marks = np.hstack((marks, row_totals))

print("\niii. After adding total column (shape:", marks.shape, "):")
print(marks)

# iv. Sort by total marks in descending order, show top 2
# argsort gives ascending order, [::-1] reverses it to descending
sort_indices = np.argsort(marks[:, -1])[::-1]
marks = marks[sort_indices]

print("\niv. Sorted by total marks (descending), top 2 rows:")
print(marks[:2])
```

### `Q-3:` Find unique arrays from a 2D array column wise and row wise.
```
arr = np.array([[1,2,3,3,1,1],
                [0,9,1,2,8,8],
                [1,2,3,8,8,8],
                [1,2,3,3,1,1]])
```
Expected Result-
```
Row Wise
[[0 9 1 2 8 8]
 [1 2 3 3 1 1]
 [1 2 3 8 8 8]]

Col Wise
[[1 1 2 3 3]
 [0 8 9 1 2]
 [1 8 2 3 8]
 [1 1 2 3 3]]
```


```python
arr = np.array([[1,2,3,3,1,1],
                [0,9,1,2,8,8],
                [1,2,3,8,8,8],
                [1,2,3,3,1,1]])

print("Row Wise:")
print(np.unique(arr, axis = 0))

print("\nColumn Wise:")
print(np.unique(arr, axis = 1))
```

### `Q-4:` Flip given 2-D array along both axes at the same time.


```python

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Flip both horizontally and vertically
flipped = np.flip(arr)

print("Original:")
print(arr)
print("\nFlipped both axes:")
print(flipped)
```

### `Q-5:` Get row numbers of NumPy array having element larger than X.
```
arr = [[1,2,3,4,5],
      [10,-3,30,4,5],
      [3,2,5,-4,5],
      [9,7,3,6,5]]

X = 6
```


```python

arr = np.array([[1, 2, 3, 4, 5],
                [10, -3, 30, 4, 5],
                [3, 2, 5, -4, 5],
                [9, 7, 3, 6, 5]])

X = 6

# Find rows where ANY element is greater than X
row_numbers = np.where(np.any(arr > X, axis=1))[0]

print("Row numbers with element >", X, ":", row_numbers)

```

### `Q-6:` How to convert an array of arrays into a flat 1d array?



```python
# These arrays are given.
arr1 = np.arange(3)
arr2 = np.arange(3,7)
arr3 = np.arange(7,10)
```


```python

# Concatenate all arrays into one flat array
flat_array = np.concatenate([arr1, arr2, arr3])

print(flat_array)
```

### `Q-7:` You are given a array. You have to find the minimum and maximum array element and remove that from the array.

```python
import numpy as np

np.random.seed(400)
arr = np.random.randint(100, 1000, 200).reshape((1, 200))
```


```python

np.random.seed(400)
arr = np.random.randint(100, 1000, 200).reshape((1, 200))

# Find min and max values
min_val = np.min(arr)
max_val = np.max(arr)

print("Min:", min_val)   
print("Max:", max_val)   

# Remove both min and max using boolean mask
filtered = arr[(arr != min_val) & (arr != max_val)]

print("Original shape:", arr.shape)      
print("After removal:", filtered.shape)  
```

### `Q-8:` You are given an arrays. You have to limit this array's elements between 100 to 200. $arr ∈ [100, 700]$. So replace those values accordingly with the minimum and maximum value. Then sort the array and perform the cumulative sum of that array.


```python

np.random.seed(42)
arr = np.random.randint(100, 701,15)

print("Original array:")
print(arr)
print()

# Step 1: Clip values to range [100, 200]
# Values below 100 → 100, values above 200 → 200
clipped = np.clip(arr, 100, 200)
print("After clipping to [100, 200]:")
print(clipped)
print()

# Step 2: Sort the array
sorted_arr = np.sort(clipped)
print("Sorted array:")
print(sorted_arr)
print()

# Step 3: Cumulative sum
cumsum = np.cumsum(sorted_arr)
print("Cumulative sum:")
print(cumsum)
```

### `Q-9:` You are given a array ($arr ∈ [0, 1]$). First you have round off the elements upto 3 decimal places and compare that
- 0th percentile == minimum value of the array
- 100th percentile == maximum value of the array
- also find the difference betwen 51th percenile and 50th percentile values


```python
np.random.seed(42)
arr = np.random.rand(20)

print("Original array:")
print(arr)

# Step 1: Round off to 3 decimal places
rounded = np.round(arr, 3)
print("\nRounded to 3 decimal places:")
print(rounded)

# Step 2: Compare 0th percentile with minimum value
percentile_0 = np.percentile(rounded, 0)
min_val = np.min(rounded)

print("\n0th percentile:", percentile_0)
print("\nMinimum value: ", min_val)
print("\nAre they equal?", np.isclose(percentile_0, min_val))

# Step 3: Compare 100th percentile with maximum value
percentile_100 = np.percentile(rounded, 100)
max_val = np.max(rounded)

print("\n100th percentile:", percentile_100)
print("\nMaximum value:  ", max_val)
print("\nAre they equal?", np.isclose(percentile_100, max_val))

# Step 4: Difference between 51st and 50th percentile
p51 = np.percentile(rounded, 51)
p50 = np.percentile(rounded, 50)
diff = p51 - p50

print("\n51st percentile:", p51)
print("\n50th percentile:", p50)
print("\nDifference (51st - 50th):", diff)
```


```python

```
