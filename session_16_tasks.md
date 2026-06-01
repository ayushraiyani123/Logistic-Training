### ` Q-1:` Write a program to create an empty series.


```python
import pandas as pd

empty_series = pd.Series(dtype='float64')

print("Empty Series:")
print(empty_series)
print(f"\nType: {type(empty_series)}")
print(f"Length: {len(empty_series)}")
```

### `Q-2:` Write a Pandas program to add, subtract, multiple and divide two Pandas Series.


```python

s1 = pd.Series([10, 20, 30, 40, 50])
s2 = pd.Series([2, 4, 5, 8, 10])

print("Series 1:")
print(s1)
print("\nSeries 2:")
print(s2)

# Addition
print("\n--- Addition (s1 + s2) ---")
add_result = s1 + s2
print(add_result)

# Subtraction
print("\n--- Subtraction (s1 - s2) ---")
sub_result = s1 - s2
print(sub_result)

# Multiplication
print("\n--- Multiplication (s1 * s2) ---")
mul_result = s1 * s2
print(mul_result)

# Division
print("\n--- Division (s1 / s2) ---")
div_result = s1 / s2
print(div_result)
```

### `Q-3` Write a Pandas program to compare the elements of the two Pandas Series.
Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 10]




```python
import pandas as pd

# Create sample Series
s1 = pd.Series([2, 4, 6, 8, 10])
s2 = pd.Series([1, 3, 5, 7, 10])

print("Series 1:", s1)
print("Series 2:", s2)
print()

# Element-wise comparisons
print("--- Equal (s1 == s2) ---")
print(s1 == s2)

print("\n--- Greater Than (s1 > s2) ---")
print(s1 > s2)

print("\n--- Less Than (s1 < s2) ---")
print(s1 < s2)

print("\n--- Greater Than or Equal (s1 >= s2) ---")
print(s1 >= s2)

print("\n--- Less Than or Equal (s1 <= s2) ---")
print(s1 <= s2)

print("\n--- Not Equal (s1 != s2) ---")
print(s1 != s2)
```

### `Q-5.`Write a function to change the data type of given a column or a Series. Function takes series and data type as input, returns the converted series.
```
series = pd.Series([1,2,'Python', 2.0, True, 100])
change to float type data
```
Note: Read about pd.to_numeric()


```python

def convert_series_dtype(series, dtype):

    if dtype in [int, float, 'int', 'float']:
        # pd.to_numeric handles mixed types gracefully
        # errors='coerce' turns bad values (like 'Python') into NaN
        return pd.to_numeric(series, errors='coerce')
    
    return series.astype(dtype)
    
data = pd.Series([1, 2, 'Python', 2.0, True, 100])
print("Original:")
print(data)
print(f"Type: {data.dtype}")
print()

# Convert to float
result = convert_series_dtype(data, float)
print("After conversion to float:")
print(result)
print(f"Type: {result.dtype}")
```

Download data - https://drive.google.com/file/d/1LRhXwbEodeWXtzPhJCX0X9Lf_BECzvqb/view?usp=share_link
All Batsman runs series in IPL 2008 to 2022.

Below questions are based on this data.

### `Q-6` Find top 10 most run getter from the series.


```python
ipl = pd.read_csv('batsman_runs_series.csv', index_col = 'batter').squeeze()

ipl.sort_values(ascending=False).head(10)
```

### `Q-7` No of players having runs above 3000


```python

players=ipl[ipl>3000]
no_of_players=ipl[ipl > 3000].shape[0]

print(f"Total player are:\n{no_of_players} \n \n\nPlayers above 3000 runs are:\n{ players}")
```

### `Q-8` No of players having runs above mean value?


```python
mean = ipl.mean()
number = ipl[ipl > mean].shape[0]

print(f"Mean Value is:\n {mean}\nTotal Players above mean value is:\n{number}")
```

Download data - https://drive.google.com/file/d/1QZuZ5bypUInfVvarHACLAi8tXXHvb8xd/view?usp=share_link

file name - items.csv



### `Q-9`
    i. Read `items.csv` making `item_name` as index.
    ii. Show no of nan values
    ii. Item price is given in $, so convert it to rupees without currency symbol.
    iii. Make data type of newly made series as float.
    iv. Fill nan with mean of the series


How csv file looks

```
item_name	item_price
Chips and Fresh Tomato Salsa	$2.39
Izze	$3.39
Nantucket Nectar	$3.39
Chips and Tomatillo-Green Chili Salsa	$2.39
Chicken Bowl	$16.98

```


```python
items = pd.read_csv('items.csv', index_col = 'item_name')
print("i.Read `items.csv` making `item_name` as index.\n",items.head())
nan = items[items.isnull()].shape[0]
print(f"\nii.No. of nan values: {nan}")

exchange_rate = 83.5


price_series = items['item_price'].astype(str)  # fixed: item_price (not item_prices)

clean_prices = price_series.str.replace('$', '', regex=False).str.strip()
items['item_price'] = pd.to_numeric(clean_prices, errors='coerce') * exchange_rate

print("\niii.After converting to INR (no symbol):")
print(items.head())
print(f"\niv.Data type: {items['item_price'].dtype}")
print()

mean_price = items['item_price'].mean()
items['item_price'] = items['item_price'].fillna(mean_price)

print("v. After filling NaN with mean:")
print(items.head())
print(f"Mean used for filling: {mean_price:.2f}")

```

### `Q-10`:
    i. Find mean price
    ii. Find 30th and 6th percentile value
    iii. Plot Histogram on price with bin size 50
    iv. No of items price lies between [1000 to 2000]




```python
# i. Find mean price
mean_price = items['item_price'].mean()
print(f"i. Mean price: {mean_price:.2f}")
print()

# ii. Find 30th and 60th percentile value
percentile_30 = items['item_price'].quantile(0.30)
percentile_60 = items['item_price'].quantile(0.60)
print(f"ii. 30th percentile: {percentile_30:.2f}")
print(f"    60th percentile: {percentile_60:.2f}")
print()

# iii. Plot Histogram on price with bin size 50
# Using pandas built-in plotting (requires matplotlib backend but called via pandas)
print("iii. Generating histogram...")
items['item_price'].plot.hist(bins=50, title='Price Distribution', figsize=(10, 6))
print("    (Histogram displayed)")
print()

# iv. No of items price lies between [1000 to 2000]
count_range = items[(items['item_price'] >= 1000) & (items['item_price'] <= 2000)].shape[0]
print(f"iv. Items with price between 1000-2000: {count_range}")
```


```python

```
