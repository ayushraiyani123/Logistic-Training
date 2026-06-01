```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import re

pd.options.display.max_columns = None
```

### `Question-1:`

The dataset is based on NFTs. This is quite large. So, when you will read the dataset, you have to wait. The link of the dataset: https://tinyurl.com/2pfhncqw

Your task is to make a pivote table by using the columns "verification_status", "contract_type", "rarity_score" and "last_sale_price" to find out the total values.


```python
df = pd.read_csv('archive/sales.csv')
# df.info()
 
df2 = pd.read_csv('archive/assets.csv')

# Create pivot table with totals
pivot = pd.pivot_table(
    df,
    values=['payment_usd_price'],
    index=['nft_is_disabled', 'nft_token_standard'],
    aggfunc='sum',
    margins=True,        # Adds grand total row and column
    margins_name='Total'
)

print(pivot)
```

### `Question-2:`

You are given a dataset about the cars' price and miles driven of different cars throughout the different years. The link of the dataset: https://tinyurl.com/2r24n45l. Your tasks are
- make a pivot table of the brands (the required brands are given below) from the "Year" 2018 to the year 2022 in which the "Price" is shown as average values and "Miles" are in median values. In this pivote table, every row represents a particular brand and each column represents either average "Price" of a partucular year or median values of "Miles" of a particular year.
- At the end plot a kde chart for the "Price" and "Miles" by using your pivot table.

There are some challenges to solve this task:
- There is no column that is represented to the brand name of the car. You have to find out on your own.
- Some values of "Years" column are misleading. You have to reset this column too that every value should tell a valid meaning.


```python
cars = pd.read_csv("carvana - carvana.csv")
cars.info()
```

### `Question-3:`

You are given a dataset of **Daily Power Generation in India** of regional wise of all Power Stations. Link of the dataset: https://tinyurl.com/2nq6kugt

Task
- In this dataset, there are many columns. Two of them are `Actual(MU)` and `Excess(+) / Shortfall (-)`. `Actual(MU)` represents the actual power generation. `Excess(+) / Shortfall (-)` tells is that generated power is excess or shortfall for that particular day of a power station. You have to find out what should be the actual power generation required for that day by the power stations that there would not be any excess or shorfall power. For the result, make a new column.
- Find out the month of the day and store it as a new column.
- Find out top 10 frequently appeared power stations in this dataframe.
- Next create a pivot table of which every row represents a power station and every column represents a month in a order. Like January, February, March...
- It is hard to get inside if you look through the only pivot table. So plot the pivot table.


```python
dataf = pd.read_csv("PowerGeneration - PowerGeneration.csv")
dataf
dataf['Required_Generation'] = dataf['Actual(MU)'] - dataf['Excess(+) / Shortfall (-)']
dataf.head()



date_col = [col for col in dataf.columns if 'date' in col.lower()][0]
dataf[date_col] = pd.to_datetime(dataf[date_col])
print(dataf[['Actual(MU)', 'Excess(+) / Shortfall (-)', 'Required_Generation']].head(10))

dataf['Month'] = dataf[date_col].dt.month_name()
dataf['Month_Num'] = dataf[date_col].dt.month
print(dataf[[date_col, 'Month']].head())

station_col = [col for col in dataf.columns if 'station' in col.lower()][0]

top_10_stations = dataf[station_col].value_counts().head(10)
print("\nTop 10 Most Frequent Power Stations:")
print(top_10_stations)

month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']

pivot_table = dataf.pivot_table(
    index=station_col,
    columns='Month',
    values='Required_Generation',
    aggfunc='mean',
    fill_value=0
)

# Reorder columns
pivot_table = pivot_table.reindex(columns=month_order)

print("\nPivot Table (first 5 rows):")
print(pivot_table.head())

# Save to CSV
# pivot_table.to_csv('power_generation_pivot_table.csv')

plt.figure(figsize=(16, 12))

sns.heatmap(pivot_table, 
            cmap='YlOrRd',
            annot=False,
            fmt='.1f',
            cbar_kws={'label': 'Required Generation (MU)'},
            linewidths=0.5)

plt.title('Monthly Required Power Generation by Power Station (MU)', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Month', fontsize=12, fontweight='bold')
plt.ylabel('Power Station', fontsize=12, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.savefig('power_generation_heatmap.png', dpi=300, bbox_inches='tight')
plt.show()

# ============================================================
# BONUS: Line Plot for Top 10 Stations
# ============================================================
top_10_names = top_10_stations.index.tolist()
df_top10 = dataf[dataf[station_col].isin(top_10_names)]

monthly_top10 = df_top10.groupby([station_col, 'Month_Num'])['Required_Generation'].mean().reset_index()

plt.figure(figsize=(16, 10))
for station in top_10_names:
    station_data = monthly_top10[monthly_top10[station_col] == station]
    plt.plot(station_data['Month_Num'], station_data['Required_Generation'], 
             marker='o', label=station, linewidth=2)

plt.title('Monthly Required Power Generation - Top 10 Stations', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12, fontweight='bold')
plt.ylabel('Required Generation (MU)', fontsize=12, fontweight='bold')
plt.xticks(range(1, 13), month_order, rotation=45, ha='right')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig('power_generation_lineplot.png', dpi=300, bbox_inches='tight')
plt.show()
```

### `Q-4` You are given a file `question-answer.csv`. Your task is to make a dataframe from it with two columns - `question` and `answers`.

* Questions in the file start from `Q<number>`; E.g.  `Q1` denotes question no. `1`
* Answers starts from `Ans<number>`; Eg. `Ans1` denotes answer of question no `1`
* MAke sure you look at columns name carefully

CSV File - "https://drive.google.com/file/d/10rmV3XrVtzpDTtYZF3UtCdcU0ajBJjGY/view?usp=share_link"


```python
df_raw = pd.read_csv('data-20260507T064033Z-3-001/imdb-top-1000.csv', header=None)

text_col = df_raw[1]
questions = []
answers = []

i = 0
while i < len(text_col):
    val = str(text_col.iloc[i]).strip()
    
    # Skip empty rows
    if not val or val == 'nan':
        i += 1
        continue
    
    # Check if this is a question row (starts with Q, has dash, has number)
    if val.startswith('Q') and '-' in val:
        q_parts = val.split('-', 1)
        if len(q_parts) == 2 and q_parts[0][1:].isdigit():
            q_num = q_parts[0][1:]
            q_text = q_parts[1].strip()
            
            # Search forward for matching answer
            j = i + 1
            while j < len(text_col):
                a_val = str(text_col.iloc[j]).strip()
                if a_val.startswith('Ans') and '-' in a_val:
                    a_parts = a_val.split('-', 1)
                    if len(a_parts) == 2 and a_parts[0][3:].isdigit():
                        a_num = a_parts[0][3:]
                        a_text = a_parts[1].strip()
                        if q_num == a_num:
                            questions.append(q_text)
                            answers.append(a_text)
                            i = j  # Jump past the answer
                            break
                j += 1
    
    i += 1

df = pd.DataFrame({'question': questions, 'answers': answers})
df
```

### `Q-5`: Print Question and answer of those questions which does not contains any question mark (`?`).



```python

# ---- Q-5: Filter questions WITHOUT '?' ----
# regex=False treats '?' as literal character, not regex special character
df_no_qm = df[~df['question'].str.contains(' ?', regex=False)]

pk = df_no_qm.to_string(index=False)
print(pk)
```

### `Q 6-10` LOG and EMPLOYEE
6. Show `activity` details month wise. Show count for each `activity`
7. Find employee who did most `activity` in January month.
8. Employee who have worked most no of times on Weekends.
9. Which activity is logged most on buisness days.
10. Week Days wise activity table.
```
log_file = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vT-OMrmmNdOTM-B5f5F1EpCutMVG230UZiLvqlsg0NIKUKR3yrqiI2r1pEX-LvSEk-3WwySPYtvbBC-/pub?gid=1937029224&single=true&output=csv")
employee = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQ5AuFqRjSZVBKm5zyDxquX6utubq1DJKkYDI70vjeidAnyAu70KMSYpMYzeVSNVTeUIJBpfF6jU5E6/pub?gid=798824749&single=true&output=csv")

```

Note(for common field):- Employee file has `EMPLOYEE_ID` and LOG file has `emp_id`


```python
log_file = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vT-OMrmmNdOTM-B5f5F1EpCutMVG230UZiLvqlsg0NIKUKR3yrqiI2r1pEX-LvSEk-3WwySPYtvbBC-/pub?gid=1937029224&single=true&output=csv")
employee = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQ5AuFqRjSZVBKm5zyDxquX6utubq1DJKkYDI70vjeidAnyAu70KMSYpMYzeVSNVTeUIJBpfF6jU5E6/pub?gid=798824749&single=true&output=csv")

# # DEBUG: Print actual column names
# print("Log columns:", log_file.columns.tolist())
# print("Employee columns:", employee.columns.tolist())

# Auto-find date column (tries multiple common names)
date_col = None
for c in log_file.columns:
    if any(word in c.lower() for word in ['date', 'time', 'dt', 'timestamp', 'day']):
        date_col = c
        break
if date_col is None:
    # Try to detect which column contains dates
    for c in log_file.columns:
        try:
            converted = pd.to_datetime(log_file[c], errors='coerce')
            if converted.notna().sum() > len(log_file) * 0.5:
                date_col = c
                break
        except:
            continue

print(f"Date column found: {date_col}")

# Auto-find activity column
activity_col = [c for c in log_file.columns 
                if any(w in c.lower() for w in ['activity', 'type', 'action', 'task'])][0]
print(f"Activity column: {activity_col}")

# Auto-find employee ID columns
log_emp = [c for c in log_file.columns if 'emp' in c.lower() or 'id' in c.lower()][0]
emp_id = [c for c in employee.columns if 'emp' in c.lower() or 'id' in c.lower()][0]

# Process
log_file[date_col] = pd.to_datetime(log_file[date_col], errors='coerce')
log_file['month'] = log_file[date_col].dt.month_name()
log_file['weekday'] = log_file[date_col].dt.day_name()
log_file['is_weekend'] = log_file[date_col].dt.weekday >= 5
log_file['is_business_day'] = ~log_file['is_weekend']

# Merge
merged = log_file.merge(employee, left_on=log_emp, right_on=emp_id, how='left')


# 1. MONTH WISE ACTIVITY COUNT
print("\n6. MONTHLY ACTIVITY COUNT:")
monthly = log_file.groupby(['month', activity_col]).size().unstack(fill_value=0)
print(monthly)

# 2. MOST ACTIVE IN JANUARY
jan = log_file[log_file['month'] == 'January']
top_jan = jan.groupby(log_emp).size().idxmax()
print(f"\n7. Most active in January: Employee {top_jan}")

# 3. MOST WEEKEND WORKER
weekend = log_file[log_file['is_weekend']]
top_wk = weekend.groupby(log_emp).size().idxmax()
print(f"\n8. Most weekend worker: Employee {top_wk}")

# 4. TOP BUSINESS DAY ACTIVITY
biz = log_file[log_file['is_business_day']]
top_biz = biz[activity_col].value_counts().index[0]
print(f"\n9. Most logged on business days: {top_biz}")

# 5. WEEKDAY ACTIVITY TABLE
weekday_table = log_file.groupby(['weekday', activity_col]).size().unstack(fill_value=0)
day_order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
weekday_table = weekday_table.reindex([d for d in day_order if d in weekday_table.index])
print("\n10. WEEKDAY ACTIVITY TABLE:")
print(weekday_table)
```

### `Q-11`:

1. There are missing value in first name of employee. Fill it using email and last name field.

> E.g- `email` -> JMURMAN and `last_name` -> 'Urman' -> so make it's first name as 'JM', Sort of (Email- lastname).

> Email is constructed from initials of first name concate with lastname. Your Task is to fill first name initials in missing data.

2. You can see email field don't have any domain name. Change this to full email addreess with domain as 'campusx.com'.
E.g- Email field -> `JMURMAN`  result -> `JMURMAN@CAMPUSX.COM`

3. Show Full Name of all the employees whose name starts with 'A' and has done any of these activity ['Incpection', 'Cleaning', 'Checking]


```python

missing = employee['FIRST_NAME'].isna()

if missing.sum() > 0:
    for i in employee[missing].index:
        email = str(employee.loc[i, 'EMAIL']).strip().upper()
        last = str(employee.loc[i, 'LAST_NAME']).strip().upper()
        
        # Remove domain if present
        email = email.split('@')[0]
        
        # Remove last_name to get initials
        initials = email.replace(last, '')
        employee.loc[i, 'FIRST_NAME'] = initials.title()
    
    print("Filled missing first names:")
    print(employee[missing][['EMAIL', 'LAST_NAME', 'FIRST_NAME']])
else:
    print("No missing first names found.")

# Strip any existing domain first, then add fresh
employee['EMAIL'] = employee['EMAIL'].str.split('@').str[0]
employee['EMAIL'] = employee['EMAIL'].str.upper() + '@CAMPUSX.COM'

print("\nFixed emails:")
print(employee[['FIRST_NAME', 'EMAIL']].head())

a_employees = employee[employee['FIRST_NAME'].str.startswith('A', na=False)]

# Merge
merged = log_file.merge(
    a_employees, 
    left_on='emp_id', 
    right_on='EMPLOYEE_ID'
)

# Filter activities
target = ['Incpection', 'Cleaning', 'Checking']
activity_col = [c for c in log_file.columns if 'activity' in c.lower()][0]
result = merged[merged[activity_col].isin(target)]

# Use FULL_NAME from employee file
names = result['FULL_NAME'].unique()

print(f"\nFound {len(names)} employees:")
for name in sorted(names):
    print(f"  {name}")
```


```python

```
