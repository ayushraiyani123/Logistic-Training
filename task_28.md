**Problem:**

You are given the following dataset:
1. **Audible Data** : https://1drv.ms/u/s!AiqdXCxPTydhoog8ckLN-6Cw55fzIg?e=EWgZ5d

Your task is to:
- Find the problems with the datasets.
- Define the Data Quality Dimensions.
- Try to clean the datasets.

### 1. Summary for your data

With the trend toward audiobooks growing, I gathered this data to understand how the audiobook market has been growing over the years. From authors of audiobooks to release dates, the data represents the important details of audiobooks from 1998 till 2025 (pre-planned releases).

I have yet to find a great audiobooks dataset and hence the urge to make a dataset that provides us with information on the basics and the history of audiobooks. I look to improve the dataset with more details in the near future.




Unique Identifiers:

The combination of name and author serves as a natural unique identifier, though the raw data contains 851 duplicate rows (exact copies) that must be removed before analysis. Some titles also appear multiple times with different narrators.



### 2. Column descriptions

#### **Table** -> `Audio Books`:

- `name`: Title of the audiobook or story.
- `author`: Writer(s) who created the original book.
- `narrator`: Performer(s) who voice the audiobook.
- `time`: Total listening length (usually in hours/minutes).
- `releasedate`: Date the audiobook was published or made available.
- `language`: Primary language of the audiobook narration.
- `stars`: Average user rating (typically on a 1–5 scale).
- `price`: Cost to purchase or rent the audiobook.

### Issues with the dataset

1. Dirty Data

    - laanguage should starts with capital latter `consistency`
    - duplicate entries in name column `accuracy`
    - incorrect data type assinged with col time,releasedate stars and price `validity`

2. Messy Data

    - author col and narrator col should only consist author name and narrator name
    - time col should be in integer format displaying total minutes
    - stars col should be independent from rating count


```python
import pandas as pd
# cleaned = pd.read_csv('audible/audible_cleaned.csv')
uncleaned = pd.read_csv('audible/audible_uncleaned.csv')
with pd.ExcelWriter('audibles_uncleaned.xlsx') as writer:
  uncleaned.to_excel(writer,sheet_name='audible_uncleaned')
```


```python
# uncleaned[uncleaned.duplicated(subset = ['author','name','narrator'])]
# uncleaned.duplicated(subset = ['author','name','narrator']).sum()
uncleaned_df = uncleaned.copy()
df = uncleaned_df
```


```python
import pandas as pd
import numpy as np
import re

# Load data
# df = pd.read_csv('audible_uncleaned.csv')

print(f"Loaded {df.shape[0]} rows, {df.shape[1]} columns")
print(df.dtypes)
print("\nFirst few rows:")
print(df.head(3))

# --- Initial look at issues ---
# stars column is a mess - "5 out of 5 stars123 ratings"
# author has "Writtenby:" prefix, narrator has "Narratedby:"
# time is string like "8 hrs 12 mins"
# price has commas and "Free"
# releasedate is string, needs to be actual dates
# language is lowercase sometimes

# Drop rows where we can't identify the book at all
df = df.dropna(subset=['name', 'author']).copy()
print(f"\nAfter dropping missing names/authors: {len(df)} rows")

# --- Fix the stars column ---
# Need to split into rating and number of ratings

def parse_stars(s):
    if pd.isna(s) or s == 'Not rated yet':
        return pd.Series([np.nan, np.nan])
    
    m = re.search(r'([\d\.]+)\s+out of 5 stars\s*(\d+)\s+ratings', str(s))
    if m:
        return pd.Series([float(m.group(1)), int(m.group(2))])
    return pd.Series([np.nan, np.nan])

df[['star_rating', 'num_ratings']] = df['stars'].apply(parse_stars)
df = df.drop('stars', axis=1)

# Quick check
print(f"\nStar parsing sample:")
print(df[['star_rating', 'num_ratings']].head(3))

# --- Convert time to minutes ---
def time_to_minutes(t):
    if pd.isna(t):
        return np.nan
    
    t = str(t).lower()
    hrs = re.search(r'(\d+)\s*hrs?', t)
    mins = re.search(r'(\d+)\s*mins?', t)
    
    total = 0
    if hrs:
        total += int(hrs.group(1)) * 60
    if mins:
        total += int(mins.group(1))
    
    return total

df['duration_minutes'] = df['time'].apply(time_to_minutes)
df = df.drop('time', axis=1)

# --- Clean price ---
def clean_price(p):
    if pd.isna(p):
        return np.nan
    
    p = str(p).strip().strip('"')
    if p.lower() == 'free':
        return 0.0
    
    try:
        return float(p.replace(',', ''))
    except ValueError:
        return np.nan

df['price_inr'] = df['price'].apply(clean_price)
df = df.drop('price', axis=1)

# --- Fix language capitalization ---
df['language'] = df['language'].str.capitalize()

# --- Release date ---
# Format appears to be dd-mm-yy
df['release_date'] = pd.to_datetime(df['releasedate'], format='%d-%m-%y', errors='coerce')
df = df.drop('releasedate', axis=1)

# Check how many failed to parse
bad_dates = df['release_date'].isna().sum()
if bad_dates > 0:
    print(f"\nWarning: {bad_dates} dates couldn't be parsed")

# --- Clean author/narrator names ---
# Remove prefixes and add spaces between camelCase names

df['author'] = df['author'].str.replace('Writtenby:', '', regex=False)
df['author'] = df['author'].apply(lambda x: re.sub(r'([a-z])([A-Z])', r'\1 \2', str(x)) if pd.notna(x) else x)

df['narrator'] = df['narrator'].str.replace('Narratedby:', '', regex=False)

# --- Remove duplicates ---
before = len(df)
df = df.drop_duplicates()
print(f"\nRemoved {before - len(df)} duplicate rows")

# --- Final column selection and type enforcement ---
df = df[[
    'name', 'author', 'narrator', 'duration_minutes',
    'release_date', 'language', 'star_rating', 'num_ratings', 'price_inr'
]]

# Make sure numeric columns are actually numeric
df['duration_minutes'] = pd.to_numeric(df['duration_minutes'], errors='coerce')
df['star_rating'] = pd.to_numeric(df['star_rating'], errors='coerce')
df['num_ratings'] = pd.to_numeric(df['num_ratings'], errors='coerce')
df['price_inr'] = pd.to_numeric(df['price_inr'], errors='coerce')

# --- Final check ---
print("\n--- Final dtypes ---")
print(df.dtypes)

print("\n--- Sample data ---")
print(df.head())

print("\n--- Numeric summary ---")
print(df[['duration_minutes', 'star_rating', 'num_ratings', 'price_inr']].describe())

# Save
df.to_csv('audible_cleaned.csv', index=False)
print(f"\nSaved to audible_cleaned.csv ({len(df)} rows)")
```


```python
pd.read_csv('audible_cleaned.csv')
```


```python

```


```python

```


```python

```
