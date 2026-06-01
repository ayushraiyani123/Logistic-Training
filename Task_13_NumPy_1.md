**Note: In Data Science googling is a very important skill. If you find some difficulties to solve the problem, google it and try to find some clues to solve.**


```python
import numpy as np
```

### `Q-1` Create a null vector of size 10 but the fifth value which is 1.




```python
a = np.nan + np.empty(10)
a[4] = 1
a
```

### `Q-2` Ask user to input two numbers a, b. Write a program to generate a random array of shape (a, b) and print the array and avg of the array.


```python
a =int(input("Pleasse enter first nummber"))
b =int(input("please enter second number"))

x=np.random.random((a,b))
print(x)
y=np.mean(x)
print(y)
```

### `Q-3`Write a function to create a 2d array with 1 on the border and 0 inside. Take 2-D array shape as (a,b) as parameter to function.

Eg.-
```
[[1,1,1,1],
[1,0,0,1],
[1,0,0,1],
[1,1,1,1]]
```


```python
def borderArray(a,b):
    x = np.ones((a,b))
    
    x[1:-1,1:-1] = 0
    return x.astype(np.int32)

borderArray(4,5)
```

### `Q-4` Create a vector of size 10 with values ranging from 0 to 1, both excluded.



```python
v=np.linspace(0,1,12)
v[1:-1]
```

### `Q-5` Can you create a identity mattrix of shape (3,4). If yes write code for it.


```python
# Identity matricx is a square mattrix, means no of rows and columns will always be same.
# Here shape given 3,4 so identuty matrix not possible.

print(np.identity(3))
print(np.eye(4))
```

### `Q-6:` Create a 5x5 matrix with row values ranging from 0 to 4.


```python
z=np.zeros((5,5))
z += np.arange((5))
z
```

### `Q-7:`  Consider a random integer (in range 1 to 100) vector with shape `(10,2)` representing coordinates, and coordinates of a point as array is given. Create an array of distance of each point in the random vectros from the given point. Distance array should be interger type.

```
point = np.array([2,3])
```



```python
point = np.array([2,3]) 
a=np.random.randint(1,100,(10,2))
p=np.array([2,3])
np.sqrt(np.sum((a-p)**2, axis=1)).astype(int)
```

### `Q-8:` Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?


```python
g=np.unravel_index((100), (6,7,8))
print(g)
```

### `Q-9:` Arrays

You are given a space separated list of numbers. Your task is to print a reversed NumPy array with the element type float.



**Input Format:**

A single line of input containing space separated numbers.

**Output Format:**

Print the reverse NumPy array with type float.

**Example 1:**

Input:

```bash
1 2 3 4 -8 -10
```

Output:

```bash
[-10.  -8.   4.   3.   2.   1.]
```


```python
a = input().strip().split()
np.array(a[::-1], dtype=np.float32)
```

### `Q-10:` Elements count

Count the number of elements of a numpy array.



**Example 1:**

Input:
```bash
np.array([])
```

Output:
```bash
elements_count :  0
```

**Example 2:**

Input:
```bash
np.array([1, 2])
```

Output:
```bash
elements_count :  2
```


```python
a = np.array([2,3])
b=np.zeros([2,3])
print(a)
print(np.size(a))
print("\n",b)
np.size(b)
```

### `Q-11:` Softmax function

Create a Python function to calculate the Softmax of the given numpy 1D array. The function only accepts the numpy 1D array, otherwise raise error.

$$\Large \sigma(\vec z)_i = \frac{e^{z_i}}{\sum_{j=i}^{K}{e^{z_j}}}$$

https://en.wikipedia.org/wiki/Softmax_function



**Example 1:**

Input:
```bash
[86.03331084 37.7285648  48.64908087 87.16563062 38.40852563 37.20006318]
```

Output:
```bash
[2.43733249e-01, 2.56112115e-22, 1.41628284e-17, 7.56266751e-01,
       5.05514197e-22, 1.50974911e-22]
```

**Example 2:**

Input:
```bash
[33.17344305 45.61961654 82.05405781 80.9647098  68.82830233 91.52064278]
```

Output:
```bash
[4.57181035e-26, 1.16249923e-20, 7.73872596e-05, 2.60358426e-05,
       1.39571531e-10, 9.99896577e-01]
```


```python
def softmax(arr):
    if type(arr) != np.ndarray:
        raise TypeError("Requires Numpy Array")
    elif arr.ndim > 1:
        raise TypeError("Requires 1D Array")
    s = np.sum(np.exp(arr))
    return np.exp(arr)/s
softmax(np.array([86.03331084, 37.7285648,  48.64908087, 87.16563062, 38.40852563, 37.20006318]))
```

### `Q-12:` Vertical stack

Write a python function that accepts infinite number of numpy arrays and do the vertical stack to them. Then return that new array as result. The function only accepts the numpy array, otherwise raise error.



**Example 1:**

Input:
```bash
a= [[0 1 2 3 4]
 [5 6 7 8 9]]

b= [[1 1 1 1 1]
 [1 1 1 1 1]]
```

Output:

```bash
[[0 1 2 3 4]
 [5 6 7 8 9]
 [1 1 1 1 1]
 [1 1 1 1 1]]
```

**Example 2:**

Input:
```bash
a= [[0 1 2 3 4]
 [5 6 7 8 9]]

b= [[1 1 1 1 1]
 [1 1 1 1 1]]

c= [[0.10117373 0.1677244  0.73764059 0.83166097 0.48985695]
 [0.44581567 0.13502419 0.55692335 0.16479622 0.61193593]]
```

Output:
```bash
[[0.         1.         2.         3.         4.        ]
 [5.         6.         7.         8.         9.        ]
 [1.         1.         1.         1.         1.        ]
 [1.         1.         1.         1.         1.        ]
 [0.10117373 0.1677244  0.73764059 0.83166097 0.48985695]
 [0.44581567 0.13502419 0.55692335 0.16479622 0.61193593]]
```


```python

def vertical_stack(*arr):
    for i in arr:
        if type(i) != np.ndarray:
            raise TypeError("Requires Numpy Array")
    return np.vstack(arr)

a = np.arange(10).reshape(2, -1)
print("a=",a)
b = np.repeat(1, 10).reshape(2, -1)
print("b=",b)
print(vertical_stack(a,b))
c = np.random.random((2,5))
print("c=", c)
vertical_stack(a,b,c)
```

### `Q-13:` Dates

Create a python function named **date_array** that accepts two dates as string format and returns a numpy array of dates between those 2 dates. The function only accept 2 strings, otherwise raise error. The date format should be like this only: `2022-12-6`. The end date should be included and for simplicity, choose dates from a same year.



**Example 1:**

Input:
```bash
date_array(start = '2020-09-15', end = '2020-09-25')
```

Output:
```bash
['2020-09-15', '2020-09-16', '2020-09-17', '2020-09-18',
 '2020-09-19', '2020-09-20', '2020-09-21', '2020-09-22',
 '2020-09-23', '2020-09-24', '2020-09-25']
```

**Example 2:**

Input:
```bash
date_array(start = '2022-12-01', end = '2022-12-06')
```

Output:
```bash
['2022-12-01', '2022-12-02', '2022-12-03', '2022-12-04', '2022-12-05', '2022-12-06']
```

**Example 3:**

Input:
```bash
date_array(start = '2020-11-25', end = '2020-11-30')
```

Output:
```bash
['2020-11-25', '2020-11-26', '2020-11-27', '2020-11-28',
 '2020-11-29', '2020-11-30']
```


```python
def date_array(start: str, end: str):
    if type(start) != str or type(end) != str:
        raise TypeError
        
    total_days_of_month = {"01": 31, "02": 28, "03": 31, "04":30, "05": 31, "06":30, "07":31, "08":31, "09":30, "10": 31, "11":30, "12":31}

    end = end.split("-")
    end_last = int(end[-1]) + 1
    
    # If the next day of end falls in the next month, account for that
    if total_days_of_month[end[-2]] < end_last:
        days_diff = end_last - total_days_of_month[end[-2]]
        end[-1] = f'0{days_diff}' if days_diff< 10 else f'{days_diff}'
        next_month = int(end[-2]) + 1
        end[-2] = f'0{next_month}' if next_month< 10 else f'{next_month}'
    else:
        end[-1] = f'0{end_last}' if end_last < 10 else f'{end_last}'
    end = "-".join(end)
    return np.arange(start, end, dtype="datetime64[D]")    # Use arange() to generate all dates between start and end 
date_array(start = '2020-11-25', end = '2020-11-30')
```

### `Q-14:` Subtract the mean of each row from a matrix.


```python
m = np.random.random((3,4))
m-np.mean(m,axis=1, keepdims = True)

```

### `Q-15:` Swap column-1 of array with column-2 in the array.


```python

a = np.arange(9).reshape(3,3)
a[:, [1, 0, 2]]
```

### `Q-16:` Replace odd elements in arrays with -1.


```python
w = np.arange((10))
w[w%2 == 1] = -1
w
```

### `Q-17:` Given two arrays of same shape make an array of max out of two arrays. (Numpy way)
```
a=np.array([6,3,1,5,8])
b=np.array([3,2,1,7,2])

Result-> [6 3 1 7 8]
```


```python
a=np.array([6,3,1,5,8])
b=np.array([3,2,1,7,2])
a[b>a] = b[a<b]
a
```

### `Q-18` Answer below asked questions on given array:
1. Fetch Every alternate column of the array
2. Normalise the given array

https://en.wikipedia.org/wiki/Normalization_(statistics)

There are different form of normalisation for this question use below formula.

$$\large X_{normalized} = \frac{X - X_{min}}{X_{max} - X_{min}}$$

```python
arr1=np.random.randint(low=1, high=10000, size=40).reshape(8,5)
```



```python
# Given
arr1=np.random.randint(low=1, high=10000, size=40).reshape(8,5)
arr1
```


```python
arr1[:,::2]
```


```python
(arr1 - arr1.min())/(arr1.max() - arr1.min())
```

### `Q-19:` Write a function which will accept 2 arguments.
First: A 1D numpy array arr

Second: An integer n {Please make sure n<=len(arr)}

Output: The output should be the nth largest item out of the array
```
# Example1 : arr=(12,34,40,7,1,0) and n=3, the output should be 12
# Example2 : arr=(12,34,40,7,1,0) and n=1, the output should be 40
```


```python
def nthmax(arr,n):
    if n>len(arr):
        raise IndexError("n is way out of limit")

    arr.sort()
    return arr[-n]

int(nthmax(np.array([12,34,40,7,1,0]),2))
```

### `Q-20:` Create the following pattern without hardcoding. Use only numpy functions and the below input array a.
```
# Input: a = np.array([1,2,3])
# Output: array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])
```


```python
a = np.array([1,2,3])
np.hstack([np.repeat(a, 3), np.tile(a, 3)])
```


```python

```
