### `Problem 1`: Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:

> Salary(Lakhs) : Tax(%)

*   Below 5 : 0%
*   5-10 : 10%
*   10-20 : 20%
*   aboove 20 : 30%


```python
# monthly in-hand salary after deductions
# input: annual CTC in lakhs
ctc_lakhs = float(input("Enter your CTC"))

hra   = 0.10 * ctc_lakhs
da    = 0.05 * ctc_lakhs
pf    = 0.03 * ctc_lakhs
fixed = hra + da + pf

if ctc_lakhs < 5:
    tax_rate = 0.0
elif ctc_lakhs < 10:
    tax_rate = 0.10
elif ctc_lakhs < 20:
    tax_rate = 0.20
else:
    tax_rate = 0.30

tax        = tax_rate * ctc_lakhs
net_annual = ctc_lakhs - fixed - tax
monthly    = net_annual / 12

print("Monthly in hand salary",round(monthly, 2))
```

### `Problem 2`: Write a program that take a user input of three angles and will find out whether it can form a triangle or not.


```python
a = float(input("Enter degree of angle 1"))
b = float(input("Enter degree of angle 2"))
c = float(input("Enter degree of angle 3"))

if a > 0 and b > 0 and c > 0 and a + b + c == 180:
    print("Triangle")
else:
    print("Not Triangle")
```


### `Problem 3`: Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit.


```python
cp = float(input("Enter cost price"))
sp = float(input("Enter selling price"))

if sp > cp:
    print("Profit")
elif sp < cp:
    print("Loss")
else:
    print("Neither")
```

### `Problem 4`: Write a menu-driven program -
1. cm to ft
2. km to miles
3. USD to INR
4. exit


```python
while True:
    print("1. cm to ft\n2. km to miles\n3. USD to INR\n4. exit")
    choice = int(input())

    if choice == 1:
        cm = float(input("Enter value in cm"))
        print(cm / 30.48,'ft')
    elif choice == 2:
        km = float(input("Enter value in km"))
        print(km * 0.621371,"miles")
    elif choice == 3:
        usd = float(input("Enter value in USD"))
        print(usd * 83.5,'Rupee')          # approximate rate
    elif choice == 4:
        break
    else:
        print("Invalid choice")
```

### `Problem 5` - Exercise 12: Display Fibonacci series up to 10 terms.

*Note: The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34*


```python
a, b = 0, 1
for _ in range(10):
    print(a, end=' ')
    a, b = b, a + b
```


```python

```

### `Problem 6` - Find the factorial of a given number.

Write a program to use the loop to find the factorial of a given number.

The factorial (symbol: `!`) means to multiply all whole numbers from the chosen number down to 1.

For example: calculate the factorial of 5

```bash
5! = 5 × 4 × 3 × 2 × 1 = 120
```

Output:

```bash
120
```


```python
n = int(input())
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)
```

### `Problem 7` - Reverse a given integer number.

Example:

`Input:`

```bash
76542
```

`Output:`

```bash
24567
```


```python
n = int(input())
rev = 0
while n:
    rev = rev * 10 + n % 10
    n //= 10
print(rev)
```

### `Problem 8`: Take a user input as integer N. Find out the sum from 1 to N. If any number if divisible by 5, then skip that number. And if the sum is greater than 300, don't need to calculate the sum further more. Print the final result. And don't use for loop to solve this problem.

**Example 1:**

`Input:`

```bash
30
```

`Output:`

```bash
276
```


```python
n = int(input())
total = 0
i = 1
while i <= n and total <= 300:
    if i % 5 != 0:
        total += i
    i += 1
print(total)
```

### `Problem 9`: Write a program that keeps on accepting a number from the user until the user enters Zero. Display the sum and average of all the numbers.


```python
num = int(input("Write any number"))
count = 0
total = 0

while num != 0:
    total += num
    count += 1
    num = int(input("Enter 0 to end"))

if count > 0:
    print(total)
    print(total / count)
```

### `Problem 10`: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a space-separated sequence on a single line.




```python
for i in range(1000, 3001):
    s = str(i)
    if int(s[0]) % 2 == 0 and int(s[1]) % 2 == 0 and int(s[2]) % 2 == 0 and int(s[3]) % 2 == 0:
        print(i, end=' ')
```

### `Problem 11`: A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The trace of robot movement is shown as the following:
```
UP 5
DOWN 3
LEFT 3
RIGHT 2
!
```
> The numbers after the direction are steps.

> `!` means robot stop there.

**Please write a program to compute the distance from current position after a sequence of movement and original point.**

*If the distance is a float, then just print the nearest integer.*

Example:

`Input`:
```
UP 5
DOWN 3
LEFT 3
RIGHT 2
!
```
`Output`:
```
2
```


```python
import math

x = 0
y = 0

while True:
    s = input().strip()
    if s == '!':
        break
    direction, step = s.split()
    n = int(step)
    
    if direction == 'UP' or 'up' or 'Up':
        y = y + n
    elif direction == 'DOWN' or 'down' or 'Down':
        y = y - n
    elif direction == 'LEFT' or 'Left' or 'left':
        x = x - n
    elif direction == 'RIGHT' or 'right' or 'Right':
        x = x + n

# Calculate distance from (0,0)
d = math.sqrt(x*x + y*y)
print(round(d))
```

### `Problem 12`:Write a program to print whether a given number is a prime number or not


```python
n = int(input())
flag = 0

for i in range(2, n):
    if n % i == 0:
        flag = 1
        break

if flag == 0 and n > 1:
    print("Prime")
else:
    print("Not Prime")
```

### `Problem 13`:Print all the Armstrong numbers in a given range.
Range will be provided by the user<br>
Armstrong number is a number that is equal to the sum of cubes of its digits. For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.


```python
start = int(input())
end = int(input())

for num in range(start, end + 1):
    temp = num
    s = 0
    while temp > 0:
        digit = temp % 10
        s = s + digit ** 3
        temp = temp // 10
    if s == num:
        print(num, end=' ')
```

### `Problem 14`:Calculate the angle between the hour hand and minute hand.

Note: There can be two angles between hands; we need to print a minimum of two. Also, we need to print the floor of the final result angle. For example, if the final angle is 10.61, we need to print 10.

Input:<br>
H = 9 , M = 0<br>
Output:<br>
90<br>
Explanation:<br>
The minimum angle between hour and minute
hand when the time is 9 is 90 degress.


```python
h = int(input())
m = int(input())

hour_pos = 30 * h + 0.5 * m
minute_pos = 6 * m
diff = abs(hour_pos - minute_pos)

if diff > 180:
    diff = 360 - diff

print(int(diff))
```

### `Problem 15`:Given two rectangles, find if the given two rectangles overlap or not. A rectangle is denoted by providing the x and y coordinates of two points: the left top corner and the right bottom corner of the rectangle. Two rectangles sharing a side are considered overlapping. (L1 and R1 are the extreme points of the first rectangle and L2 and R2 are the extreme points of the second rectangle).

Note: It may be assumed that the rectangles are parallel to the coordinate axis.

<img src='https://www.geeksforgeeks.org/wp-content/uploads/rectanglesOverlap.png' width='300' height='200'>


```python
l1x = int(input("Enter l1 x coordinate "))
l1y = int(input("Enter l1 y coordinate "))
r1x = int(input("Enter r1 x coordinate "))
r1y = int(input("Enter r1 y coordinate "))
l2x = int(input("Enter l2 x coordinate "))
l2y = int(input("Enter l2 y coordinate "))
r2x = int(input("Enter r2 x coordinate "))
r2y = int(input("Enter r2 y coordinate "))

if l1x <= r2x and l2x <= r1x and l1y <= r2y and l2y <= r1y:
    print("Overlap")
else:
    print("No Overlap")
```


```python

```
