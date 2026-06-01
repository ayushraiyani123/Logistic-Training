### `Q-1:` Find the nearest element in the array to a given integer.
```
Ex:-
a=23 and array - [10 17 24 31 38 45 52 59].
Nearest element is 24
```
Hint: Read about this function `argmin()`


```python
import numpy as np

def find_nearest(array, target):
    # Convert to numpy array just in case
    arr = np.array(array)
    
    # Find absolute differences from target
    differences = np.abs(arr - target)
    
    # Get index of smallest difference
    nearest_index = np.argmin(differences)
    
    # Return the actual element
    return arr[nearest_index]


# Test with the example
a = 23
my_array = [10, 17, 24, 31, 38, 45, 52, 59]

result = find_nearest(my_array, a)
print(result)  

# Quick sanity check - let's see the differences
print(np.abs(np.array(my_array) - a)) 
```

### `Q-2:` Replace multiples of 3 or 5 as 0 in the given array.
```
arr=[1 2 3 4 5 6 7 9]

result-> [1 2 0 4 0 0 7 0]
```


```python
def replace_with_zero(array):
    arr = np.array(array)
    # arr[arr%3 == 0] = 0
    # arr[arr%5 == 0] = 0
    arr[(arr % 3 == 0) | (arr % 5 == 0)] = 0
    print(arr)
arr=[1,2,3,4,5,6,7,9]
replace_with_zero(arr)
```

### `Q-3:` Use Fancy Indexing.
1. Double the array elements at  given indexes
```
arr = np.arrange(10)
indexes = [0,3,4,9]
```
Result -> `[ 0  1  2  6  8  5  6  7  8 18]`

2. Using a given array make a different array as in below example
```
array = [1,2,3]
result array -> [1 1 1 2 2 2 3 3 3]
```
* Internal-repetion should be as length of the array.

Hint:
```
if a is an array
a = [2,4]
a[[1,1,0,1]] will result in-> [4 4 2 4]
```


```python
arr = np.arange(10)
indexes = [0,3,4,9]

arr[indexes] = arr[indexes]*2

print(arr)
```


```python
array = [1,2,3]
arr = np.array(array)
n = len(array)
idx = np.repeat(np.arange(n), n)
print(arr[idx])
```

### `Q-4:` Your are given an array which is havig some nan value. You job is to fill those nan values with most common element in the array.
```
arr=np.array([[1,2,np.nan],[4,2,6],[np.nan,np.nan,5]])

```


```python
arr = np.array([[1, 2, np.nan], [4, 2, 6], [np.nan, np.nan, 5]])

# Get valid values
valid = arr[~np.isnan(arr)]

# Find most common using np.bincount (works for non-negative integers)
# For floats/strings, you'd need a different approach
values, counts = np.unique(valid, return_counts=True)
most_common = values[np.argmax(counts)]

print(f"Most common: {most_common}")  

# Fill NaNs
arr[np.isnan(arr)] = most_common
print(arr)
```

### `Q-5:` Write a NumPy program

- to find the missing data in a given array. Return a boolean matrix.
- also try to fill those missing values with 0. For that, you can use `np.nan_to_num(a)`

```python
import numpy as np

np.array([[3, 2, np.nan, 1],
          [10, 12, 10, 9],
          [5, np.nan, 1, np.nan]])
```


```python
arr = np.array([[3, 2, np.nan, 1],
                [10, 12, 10, 9],
                [5, np.nan, 1, np.nan]])

# Find missing data - returns boolean matrix
missing_mask = np.isnan(arr)
print("Boolean matrix (True = missing):")
print(missing_mask)

# Count how many missing values
print(f"\nTotal missing: {np.sum(missing_mask)}")  # 3

# Fill missing values with 0
arr_filled = np.nan_to_num(arr, nan=0.0)
print("\nArray with NaNs replaced by 0:")
print(arr_filled)

```

### `Q-6:` Given two arrays, X and Y, construct the Cauchy matrix C.
`Cij =1/(xi - yj)`

http://en.wikipedia.org/wiki/Cauchy_matrix
```
x = numpy.array([1,2,3,4]).reshape((-1, 1)
y = numpy.array([5,6,7])
```


```python

x = np.array([1, 2, 3, 4]).reshape((-1, 1))  # column vector (4, 1)
y = np.array([5, 6, 7])                       # row vector (3,1)

# Broadcasting: x - y gives a 4x3 matrix of all pairwise differences
differences = x - y
print("Differences (x_i - y_j):")
print(differences)
# Cauchy matrix: element-wise reciprocal
C = 1 / differences
print("\nCauchy matrix C:")
print(C)
```

### `Q-7:` Plot this below equation.

$$\large y = \frac{e^x - e^{-x}}{e^x + e^{-x}}$$

**Note: This equation is called tanh activation function. In deep learning, many times this function is used. If you find some difference between the sigmoid function and this tanh function, note that to your notebook.**


```python
import matplotlib.pyplot as plt
x = np.linspace(-10,10,100)
y = (np.exp(x) - np.exp(-x))/(np.exp(x) + np.exp(-x))  

plt.plot(x,y)
```


```python
x = np.linspace(-10,10,100)
y = 1/(1+(np.exp(-x)))
# y = sigmoid_functon(x)

plt.plot(x,y)
```

### `Q-8:` Plot the below equation.

$$\large y = \sqrt{36 - (x - 4)^2} + 2$$

The range of x should be between -2 to 10. $x ∈ [-2, 10]$




```python
x = np.linspace(-2,10,100)
y = np.sqrt(36 - ((x-4)**2) + 2)

plt.plot(x,y)
```

### `Q-9:` Write a program implement Boradcasting Rule to check if two array can be added or not.
Given tuples of shapes.
```
shape of a- (3,2,2)
shape of b- (2,2)

check_broadcast(a, b) -> return Boolean (True if can broadcasted, False other wise.)
```


```python
def check_broadcast(a, b):

    # Convert to lists for manipulation
    a = list(a)
    b = list(b)
    
    # Pad the shorter shape with 1s on the left
    while len(a) < len(b):
        a.insert(0, 1)
    while len(b) < len(a):
        b.insert(0, 1)
    
    # Check each dimension pair
    for dim_a, dim_b in zip(a, b):
        if dim_a != dim_b and dim_a != 1 and dim_b != 1:
            return False
    
    return True
    
shape_a = (3, 2, 2)
shape_b = (2, 2)
print(f"check_broadcast({shape_a}, {shape_b}) -> {check_broadcast(shape_a, shape_b)}")

print(check_broadcast((3, 2, 2), (3, 2)))      
print(check_broadcast((4, 3, 2), (3, 1)))      
print(check_broadcast((2, 3), (3, 2)))         
print(check_broadcast((1, 5), (3, 5)))         
print(check_broadcast((6, 7, 1, 8), (7, 8)))   
```


```python

```
