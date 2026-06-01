```python
import pandas as pd
import numpy as np
```

DATA DESCRIPTION
```
file name -> Columns
quater-i.csv -> ['order_id', 'quantity', 'item_id', 'choice_description_id' 'item_price']
items.csv -> ['item_id', 'item_name']
```
Dataset Link - https://drive.google.com/drive/folders/1Z0kaFybvgFeczeUj4dldUnhTdloLqLsL?usp=share_link


```python
# import like this
items_path = "data-20260507T064033Z-3-001/data/items.csv"
q1_path = "data-20260507T064033Z-3-001/data/quarter-1.csv"
q2_path = "data-20260507T064033Z-3-001/data/quarter-2.csv"
q3_path = "data-20260507T064033Z-3-001/data/quarter-3.csv"


q1= pd.read_csv(q1_path)
q2 = pd.read_csv(q2_path)
q3 = pd.read_csv(q3_path)

items = pd.read_csv(items_path)
```

### `Q:1-5`
1. You are given three quater files, your job is to append these three files and make a single dataframe.
2. Have a index as Q-1 Q-2 Q-3 for respective quater files in the dataframe
3. Your are given a file items.csv which has item_id and item_name. Find out most sold items in each quarter.
4. Find out items which has made most revenue in each quarter.
5. Find out avg order price of each quarter.

***Note: item_price is given as str with $ sign, in earlier task you have converted this to rupees, here too first convert item_price field in rupees.***


```python

exchange_rate = 83.5
price_series1 = q1['item_price'].astype(str)  # fixed: item_price (not item_prices)
price_series2 = q2['item_price'].astype(str)
price_series3 = q3['item_price'].astype(str)
clean_prices1 = price_series1.str.replace('$', '', regex=False).str.strip()
clean_prices2 = price_series2.str.replace('$', '', regex=False).str.strip()
clean_prices3 = price_series3.str.replace('$', '', regex=False).str.strip()


q1['item_price'] = pd.to_numeric(clean_prices1, errors='coerce') * exchange_rate
q2['item_price'] = pd.to_numeric(clean_prices2, errors='coerce') * exchange_rate
q3['item_price'] = pd.to_numeric(clean_prices3, errors='coerce') * exchange_rate

temp = pd.concat([q1,q2,q3],ignore_index=True)

print("i.Final dataframe after append every quater and rate coversion from $ to Rupee:\n")
temp
```


```python
# Combine with Q-1, Q-2, Q-3 as index

indexed_quarters = pd.concat([q1, q3, q2], keys=['Q-1', 'Q-3', 'Q-2'])
pd.concat([q1, q3, q2], keys=['Q-1', 'Q-3', 'Q-2'])
# print("ii.Have a index as Q-1 Q-2 Q-3 for respective quater files in the dataframe\n",indexed_quarters)

```


```python
df = indexed_quarters.reset_index().rename(columns={'level_0': 'Quarter'})

# 1. Most sold items per quarter
most_sold = df.groupby(['Quarter', 'item_id'])['quantity'].sum().reset_index()
most_sold = most_sold.loc[most_sold.groupby('Quarter')['quantity'].idxmax()]
most_sold = most_sold.merge(items, on='item_id')[['Quarter', 'item_name', 'quantity']].set_index('Quarter')
print("iii.Most Sold Items:\n", most_sold)

# 2. Highest revenue items per quarter
df['revenue'] = df['quantity'] * df['item_price']
most_revenue = df.groupby(['Quarter', 'item_id'])['revenue'].sum().reset_index()
most_revenue = most_revenue.loc[most_revenue.groupby('Quarter')['revenue'].idxmax()]
most_revenue = most_revenue.merge(items, on='item_id')[['Quarter', 'item_name', 'revenue']].set_index('Quarter')
print("\niv.Highest Revenue Items:\n", most_revenue)

# 3. Average order price per quarter
avg_order = df.groupby('Quarter').agg(total_revenue=('revenue','sum'), total_orders=('order_id','nunique'))
avg_order['avg_order_price'] = avg_order['total_revenue'] / avg_order['total_orders']
print("\nv.Average Order Price:\n", avg_order[['avg_order_price']])
```

### `Q-6` From the IPL wala dataset you have to find the Purple cap holder each season.

*Note: Bowler with most no wickets in a season gets purple cap. If more than one bowler have same no of wickets in the season, one with least ecomnomy among them is purple cap holder.*

Bowler's Economy = runs-conceded per six balls


```python
import pandas as pd

delivery = pd.read_csv("data-20260507T064033Z-3-001/data/ipl_deliveries.csv")
matches = pd.read_csv("data-20260507T064033Z-3-001/data/IPL_Matches_2008_2022.csv")

# Assign the merged result to a variable
merged_df = matches.merge(delivery, on='ID', how='inner')

delivery

merged_df.groupby(['Season','bowler']).agg(wickets=('isWicketDelivery','sum'), runs=('total_run','sum'), balls=('ballnumber','count')).assign(economy=lambda x: (x['runs']/x['balls'])*6).reset_index().sort_values(['Season','wickets','economy'], ascending=[True,False,True]).groupby('Season').first().reset_index()[['Season','bowler','wickets','economy']]
# print(merged_df.groupby(['Season','bowler'])['isWicketDelivery'].sum().reset_index().sort_values('isWicketDelivery',ascending=False).drop_duplicates(subset=['Season'],keep='first').sort_values('Season'))
```

### `Q-7:` Best bowler in death overs.
*Note: Have taken most no of wickets in case of tie with least economy*

Death Overs - [16-20]


```python
death = merged_df[merged_df['overs'].between(16, 20)]
best = death.groupby('bowler').agg(wickets=('isWicketDelivery','sum'), runs=('total_run','sum'), balls=('ballnumber','count')).assign(economy=lambda x: (x['runs']/x['balls'])*6)
best[best['balls']>=120].sort_values(['wickets','economy'], ascending=[False,True]).head(1)
```

### `Q-8` Batsman record season wise

Make a function which takes a input `batsman_name` and it returns a dataframe.
Columns of the data frame are - `['Season','Innings', 'TotalRuns', 'Avg', 'HighestScore','StrikeRate']`.
* In result make `Season` column as index.

* Avg - total_runs/ no of time got out. - player_out column will help.
* StrikeRate -(total_runs/ balls faced) * 100- wides are not included in batsman ball faced counts. No balls are included. -> Extra_type column will help
* Batsman Can score runs on No Balls.
* Batsman can get out on No Ball or Wides. And even while being on non-striker. Keep these things in mind before masking.


```python
def batsman_record(batsman_name):
    
    bat_df = merged_df[(merged_df['batter'] == batsman_name) | (merged_df['non-striker'] == batsman_name)]
    balls_faced = bat_df[(bat_df['batter'] == batsman_name) & (bat_df['extra_type'] != 'wides')]
    runs_scored = bat_df[bat_df['batter'] == batsman_name]
    dismissals = bat_df[bat_df['player_out'] == batsman_name]
    season_states = []
    for season in sorted(runs_scored['Season'].unique()):
        season_runs = runs_scored[runs_scored['Season'] == season]
        season_balls = balls_faced[balls_faced['Season'] == season]
        season_dissmissal = dismissals[dismissals['Season'] == season]
        innings = season_runs[['ID','innings']].shape[0]
        total_runs = season_runs['batsman_run'].sum()
        outs = season_dissmissal['player_out'].notna().sum()
        avg = total_runs/ outs if outs > 0 else total_runs
        highest_score = season_runs.groupby(['ID','innings'])['batsman_run'].sum().max()
        balls_count = season_balls.shape[0]
        strike_rate = (total_runs/balls_count) * 100 if balls_count > 0 else 0
        season_states.append({
            'Season' :season,
            'Innings':innings,
            'TotalRuns':total_runs,
            'Avg': round(avg,2),
            'HighestScore':highest_score,
            'StrikeRate':round(strike_rate,2)
        })
        result = pd.DataFrame(season_states).set_index('Season')
    return result

print(batsman_record('JC Buttler'))
print(batsman_record('YBK Jaiswal'))
```

### `Q-9` Using both dataset, make a dataframe as described below

Data Frame columns-> `['PlayerOfThematch', 'BattingFigure', 'BowlingFigure']`

* BattingFigure->`<runs>/<balls>`
* BowlingFigure->`<wicket>/<runs-conceded>`

DataFrame should have one record for each match.

Say 'V Kohli' got POM award then in dataset include his batting figure of that match. Say he scored 112runs in 76 balls. And he hasn't bowled so Bowling Figure will be NaN
```
PlayerOfThematch BattingFigure BowlingFigure
V Kohli          112/76         nan  

```



```python

records = []

for match_id in matches['ID'].unique():
    # Get POM for this match
    pom = matches[matches['ID'] == match_id]['Player_of_Match'].values[0]
    
    # Batting figure
    bat_data = merged_df[(merged_df['ID'] == match_id) & (merged_df['batter'] == pom)]
    runs = bat_data['batsman_run'].sum()
    balls = bat_data[bat_data['extra_type'] != 'wides'].shape[0]
    batting = f"{runs}/{balls}" if balls > 0 else np.nan
    
    # Bowling figure
    bowl_data = merged_df[(merged_df['ID'] == match_id) & (merged_df['bowler'] == pom)]
    wickets = bowl_data['isWicketDelivery'].sum()
    runs_given = bowl_data['total_run'].sum()
    bowling = f"{int(wickets)}/{runs_given}" if len(bowl_data) > 0 else np.nan
    
    records.append([pom, batting, bowling])

result = pd.DataFrame(records, columns=['PlayerOfThematch', 'BattingFigure', 'BowlingFigure'])
print(result.head(10))
```

## **Questions Based on Iris Dataset**

- **Sepal All:** https://docs.google.com/spreadsheets/d/e/2PACX-1vT58ekmHTwptX7Bs4QOy6YByA1HMvYTACeeIjrKhHE0Pg1K_3egewHMKMh02zN9D5-yHVXfvuaa3s5u/pub?gid=2028782809&single=true&output=csv
    - **Unnamed: 0:** Unused column. This column is created when creating this sub-dataset.
    - **Id:** Id of the records.
    - **SepalLengthCm:** Sepal length of flowers in cm
    - **SepalWidthCm:** Sepal width of flowers in cm

- **Petal All:** https://docs.google.com/spreadsheets/d/e/2PACX-1vQinLXShrOz4ExNaW1bSQVuvbbhIzJW7G0kkkD2SvqSD6STjLrQQiftgI7BGe10sBZi0CNr2_sJpQAz/pub?gid=1580010789&single=true&output=csv
    - **Unnamed: 0:** Unused column. This column is created when creating this sub-dataset.
    - **Id:** Id of the records.
    - **PetalLengthCm:** Petal length of flowers in cm
    - **PetalWidthCm:** Petal width of flowers in cm

- **Iris Virginica:** https://docs.google.com/spreadsheets/d/e/2PACX-1vSK39MwduGPHYNgw5yViezoLYCVDKMCWIHzjnt3GZNaxHPFOQLr2q6no_tyqTsOk-VfXleslfGVe9eJ/pub?gid=314231613&single=true&output=csv
    - **Unnamed: 0:** Unused column. This column is created when creating the sub-dataset.
    - **Id:** Id of the records.
    - **Species:** Name of this species.

- **Iris Versicolor:** https://docs.google.com/spreadsheets/d/e/2PACX-1vTcSFgLnabqIrgIc5WlwvnbbvyyJsgZjR-0E0-4TR-5aHgv_0EP6yNWglkkls3AXM2qHCR5VYzWCoTM/pub?gid=715607857&single=true&output=csv
    - **Unnamed: 0:** Unused column. This column is created when creating the sub-dataset.
    - **Id:** Id of the records.
    - **Species:** Name of this species.

- **Iris Setosa:** https://docs.google.com/spreadsheets/d/e/2PACX-1vSjqJpdgy2X_oDUUqQ0sSaFKqnnf8MYU4KgJSYgHaHmq0Wb1weMOsJXh-rICHmkLcaTkOwzMYLeh959/pub?gid=2003684803&single=true&output=csv
    - **Unnamed 0:** Unused column. This column is created when creating the sub-dataset.
    - **Id:** Id of the records.
    - **Species:** Name of this species.


```python
import pandas as pd
sepal_all = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vT58ekmHTwptX7Bs4QOy6YByA1HMvYTACeeIjrKhHE0Pg1K_3egewHMKMh02zN9D5-yHVXfvuaa3s5u/pub?gid=2028782809&single=true&output=csv")
petal_all = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQinLXShrOz4ExNaW1bSQVuvbbhIzJW7G0kkkD2SvqSD6STjLrQQiftgI7BGe10sBZi0CNr2_sJpQAz/pub?gid=1580010789&single=true&output=csv")

virginica = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSK39MwduGPHYNgw5yViezoLYCVDKMCWIHzjnt3GZNaxHPFOQLr2q6no_tyqTsOk-VfXleslfGVe9eJ/pub?gid=314231613&single=true&output=csv")
versicolor = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vTcSFgLnabqIrgIc5WlwvnbbvyyJsgZjR-0E0-4TR-5aHgv_0EP6yNWglkkls3AXM2qHCR5VYzWCoTM/pub?gid=715607857&single=true&output=csv")
setosa = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSjqJpdgy2X_oDUUqQ0sSaFKqnnf8MYU4KgJSYgHaHmq0Wb1weMOsJXh-rICHmkLcaTkOwzMYLeh959/pub?gid=2003684803&single=true&output=csv")

```

### `Q-9:` Plot a bar chart of the average Sepal Length  of Virginica and average Petal length of Setosa flower.


```python

print("Virginica columns:", virginica.columns.tolist())
print("Setosa columns:", setosa.columns.tolist())

# Example if columns are lowercase:
avg_sepal_virginica = sepal_all['SepalLengthCm'].mean()
avg_petal_setosa = petal_all['PetalLengthCm'].mean()

# Plot
data = {
    'Virginica Avg Sepal Length': avg_sepal_virginica,
    'Setosa Avg Petal Length': avg_petal_setosa
}

plt.bar(data.keys(), data.values(), color=['green', 'blue'])
plt.ylabel('Length (cm)')
plt.title('Average Sepal Length of Virginica vs Average Petal Length of Setosa')
plt.show()
```

### `Q-10:` Create the complete dataset by uisng the below datasets:
- virginica
- versicolor
- setosa
- sepal all
- petal all

This dataset should have these below column names in order:
1. Id
2. Species
3. SepalLengthCm
4. SepalWidthCm
5. PetalLengthCm
6. PetalWidthCm

Also, the dataset should be shuffled means the `Id` column should not be in increasing or decreasing order. So, make a dataset which has the shuffled Id column. You can use `DataFrame.sample()` method to shuffle.


```python
virginica['Species'] = 'Iris-virginica'
versicolor['Species'] = 'Iris-versicolor'
setosa['Species'] = 'Iris-setosa'

all_species = pd.concat([virginica, versicolor, setosa], ignore_index=True)

complete = all_species.merge(sepal_all, on='Id', how='inner')
complete = complete.merge(petal_all, on='Id', how='inner')

complete = complete[['Id', 'Species', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]

complete_shuffled = complete.sample(frac=1, random_state=42).reset_index(drop=True)

print(complete_shuffled.head(10))
print(f"\nTotal rows: {len(complete_shuffled)}")
```

### `Q-11:` Find out the maximum and minimum sepal width and petal width of Setosa and Versicolor. To do this:
- First create a dataset with merging the required datasets
- After that, use `groupby` to create groups based on the "Species" column.
- Then find out which are asked in this question.


The output should be like this:
```bash
Minimum Sepal width of Setosa is 2.3
Maximum Sepal width of Setosa is 4.4

**************************************************

Minimum Sepal width of Versicolor is 2.0
Maximum Sepal width of Versicolor is 3.4

**************************************************
```


```python
setosa['Species'] = 'Iris-setosa'
versicolor['Species'] = 'Iris-versicolor'

setosa_versicolor = pd.concat([setosa, versicolor], ignore_index=True)

merged = setosa_versicolor.merge(sepal_all, on='Id', how='inner')
merged = merged.merge(petal_all, on='Id', how='inner')

result = merged.groupby('Species').agg(
    min_sepal_width=('SepalWidthCm', 'min'),
    max_sepal_width=('SepalWidthCm', 'max'),
    min_petal_width=('PetalWidthCm', 'min'),
    max_petal_width=('PetalWidthCm', 'max')
)

print(result)

print(f"\nMinimum Sepal width of Setosa is {result.loc['Iris-setosa', 'min_sepal_width']}")
print(f"Maximum Sepal width of Setosa is {result.loc['Iris-setosa', 'max_sepal_width']}")
print("\n**************************************************\n")
print(f"Minimum Sepal width of Versicolor is {result.loc['Iris-versicolor', 'min_sepal_width']}")
print(f"Maximum Sepal width of Versicolor is {result.loc['Iris-versicolor', 'max_sepal_width']}")
```


```python

```
