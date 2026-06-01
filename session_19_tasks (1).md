## **Questions based on Titanic Dataset:**

To read the dataset as csv, use the below code:

```python

```


```python
import pandas as pd

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQjh5HzZ1N0SU7ME9ZQRzeVTaXaGsV97rU8R7eAcg53k27GTstJp9cRUOfr55go1GRRvTz1NwvyOnuh/pub?gid=1562145139&single=true&output=csv"
titanic_df = pd.read_csv(url)
```

### `Q-1:` Using `groupby` make groups using the `"Pclass"` column and find out the average age and total number of missing values in the `"Age"` column for every group.


```python
import pandas as pd
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQjh5HzZ1N0SU7ME9ZQRzeVTaXaGsV97rU8R7eAcg53k27GTstJp9cRUOfr55go1GRRvTz1NwvyOnuh/pub?gid=1562145139&single=true&output=csv"
titanic_df = pd.read_csv(url)
avg_age = titanic_df.groupby('Pclass')['Age'].mean().reset_index()
print(avg_age)

missing_values = titanic_df['Age'].isna().sum()
print(f"\nTotal {missing_values} missing values in Age column")
```

### `Q-2:` Using `groupby` make groups using the `"Pclass"` column and fill every group's `"Embarked"` column's missing values with the mode value of that group. After that, print every group's `"Embarked"` column's value counts in ascending order.


```python
mode_value = titanic_df.groupby(['Pclass'])['Embarked'].agg(pd.Series.mode).values[0]
filled = titanic_df['Embarked'].fillna(mode_value, inplace = True)

titanic_df['New_Embark'] = titanic_df['Embarked']
titanic_df[titanic_df['Embarked'].fillna(mode_value).isna()]
titanic_df.groupby('Pclass')['New_Embark'].value_counts(ascending = True).reset_index()
```

### `Q-3:` Make groups based on `"Embarked"` column. And for each of this embarked group, make another group based on `"Pclass"` and find out the average fare (round off up to 2 decimal places) for each "Pclass" for each group of "Embarked".

**Sample Output:**

```bash
{'C': {1: 105, 2: 25, 3: 11},
 'Q': {1: 90, 2: 12, 3: 11},
 'S': {1: 70, 2: 20, 3: 15}}
```


```python
duo = titanic_df.groupby(['Embarked','Pclass'])
duo['Fare'].mean().round(2).reset_index()
```

## **Questions Based on Fifa Worldcup - 2022 Dataset:**

You can read the dataset by using the below sample code

```python

```


```python
import pandas as pd

fifa_df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vT3D_x_4DS6d51LKJ7ze1sxT5WpV5uiSVOFYHLwBiGru6vFyVv5h5-83AwFjxWYiWfCDjDAaarHAV-k/pub?gid=0&single=true&output=csv")
```

### `Q-4:` Perform `groupby` based on the `"Team"` column and then perform Z Normalization on top of the below columns of each group:
1. Passes
2. Passes Completed
3. Attempted Line Breaks
4. Completed Line Breaks

You have to make a python function named `z_normalization` which takes two arguments:

1. *group:* Every group that you have created
2. *cols_to_perform:* This parameter takes a list of columns on which you have to perform the Z-Normalization.

For this problem, you have to use th `apply()` method.

$\Large Z \ - \ Normalization = \frac{X_i - \mu}{std} $

After that find out the below values for each group:
- minimum "Passess"
- maximum "Passess"
- minimum "Yellow Cards"
- maximum "Yellow cards"
- average "Yellow Cards"
- maximum "Attempted Line Breaks"
- minimum "Attempted Line Breaks"
- standardard deviation of "Attempted Line Breaks"
- average Possession


```python

def z_normalization(group, cols_to_perform):

    result = group.copy()
    
    means = result[cols_to_perform].mean()
    stds = result[cols_to_perform].std().replace(0, 1)  # Replace 0 std with 1 to avoid div by zero
    
    result[cols_to_perform] = (result[cols_to_perform] - means) / stds
    
    return result

cols_to_normalize = [
    'Passes',
    'Passes Completed',
    'Attempted Line Breaks',
    'Completed Line Breaks'
]

result = fifa_df.groupby('Team').apply(lambda group: z_normalization(group, cols_to_normalize))

result
```


```python
print("Group Statistics for Each Team")
print("=" * 80)

team_stats = df.groupby('Team').agg({
    'Passes': ['min', 'max'],
    'Yellow Cards': ['min', 'max', 'mean'],
    'Attempted Line Breaks': ['min', 'max', 'std'],
    'Possession (%)': 'mean'
}).round(2)

# Flatten column names
team_stats.columns = ['_'.join(col).strip() for col in team_stats.columns.values]

team_stats
```

## **Questions on IPL wala dataset**

ball by ball dataset - https://drive.google.com/file/d/1-kvv_9KCSAFWcrhS9WgTxSrURkRh6GNt/view?usp=share_link





### `Q-5:` Find batsman in below category-
* Highest score while chasing
* Best Strike rate while chasing and have faced 100+ balls


> Chasing mean team batting in second inning


```python
ipl = pd.read_csv('ipl_deliveries - ipl_deliveries.csv')
chase = ipl[ipl['innings'] == 2].copy()

batsman_scores = chase.groupby(['ID', 'batter'])['batsman_run'].sum().reset_index()
batsman_scores.columns = ['ID', 'batter', 'batsman_run']

highest_score = batsman_scores['batsman_run'].max()
highest_scorer = batsman_scores[batsman_scores['batsman_run'] == highest_score].reset_index()

print(f"Highest scorer while chasing is : \n {highest_scorer}")


batsman_stats = chase.groupby('batter').agg({
        'batsman_run': 'sum',      # Total runs while chasing
        'ballnumber': 'count'             # Balls faced while chasing
    }).reset_index()
batsman_stats.columns = ['batsman', 'total_runs', 'balls_faced']
    
    # Filter for 100+ balls
qualified = batsman_stats[batsman_stats['balls_faced'] >= 100].copy()
    
    # Calculate strike rate
qualified['strike_rate'] = (qualified['total_runs'] / qualified['balls_faced'] * 100).round(2)
    
    # Sort by strike rate descending
best_sr = qualified.sort_values('strike_rate', ascending=False)
print(best_sr[best_sr['batsman'] == 'PC Valthaty'])
best_sr.head(40)
```

### `Q-6` Most Successful bowler against any batsman. Find that pair of bowler and batsman.
> Most Successful in terms of dissmissal. A bowler who have dissmissed any batsman most no of times. If any two pairs have same no of dissmisal, consider runs conceded by bowler to that batsman. Those who have concede lesser runs is more successful.


```python
bowler = 'bowler'
batsman = 'batter'
wicket = 'isWicketDelivery'
runs = 'batsman_run'

wickets = ipl[ipl[wicket] == 1]

dismissals = wickets.groupby([bowler, batsman]).size().reset_index(name='dismissals')

runs_conceded = ipl.groupby([bowler, batsman])[runs].sum().reset_index(name='runs_conceded')

stats = dismissals.merge(runs_conceded, on=[bowler, batsman], how='left')
stats = stats.sort_values(['dismissals', 'runs_conceded'], ascending=[False, True]).reset_index(drop=True)

print("Most Successful Pair:")
print(f"Bowler: {stats.iloc[0]['bowler']}")
print(f"Batsman: {stats.iloc[0]['batter']}")
print(f"Dismissals: {stats.iloc[0]['dismissals']}")
print(f"Runs Conceded: {stats.iloc[0]['runs_conceded']}")

print("\nTop 10 Pairs:")
print(stats.head(10))
```

### `Q-7`: Most successful batting pair in IPL. Batting pair who have scored most runs playing together.



```python

pair = ipl.groupby(['ID', 'batter', 'non-striker'])['batsman_run'].sum().reset_index()
pair = pair.groupby(['batter', 'non-striker'])['batsman_run'].sum().reset_index()
pair = pair.sort_values('batsman_run', ascending=False)

print(pair.iloc[0])
print(pair.head(10))
```

### `Q-8:` Make a dataframe for all batting pairs played together.
```
Batsman1 Batsman2 Runs Avg StrikeRate
```

> Just to ease this question you can count wide-balls for strike rate.


```python
# create batting pairs (order doesn't matter: A+B same as B+A)
ipl['pair'] = ipl.apply(lambda x: tuple(sorted([x['batter'], x['non-striker']])), axis=1)

# calculate runs and balls per pair per match
match_stats = ipl.groupby(['ID', 'pair']).agg({
    'batsman_run': 'sum',
    'ballnumber': 'count'
}).reset_index()

match_stats.columns = ['match_id', 'pair', 'runs', 'balls']

# aggregate across all matches
pair_stats = match_stats.groupby('pair').agg({
    'runs': ['sum', 'mean'],
    'balls': 'sum',
    'match_id': 'count'
}).reset_index()

# flatten column names
pair_stats.columns = ['pair', 'Runs', 'Avg', 'Balls', 'Innings']

# calculate strike rate
pair_stats['StrikeRate'] = (pair_stats['Runs'] / pair_stats['Balls'] * 100).round(2)

# split pair into two batsman columns
pair_stats[['Batsman1', 'Batsman2']] = pd.DataFrame(pair_stats['pair'].tolist(), index=pair_stats.index)

# select final columns
result = pair_stats[['Batsman1', 'Batsman2', 'Runs', 'Avg', 'StrikeRate']]
result = result.sort_values('Runs', ascending=False).reset_index(drop=True)

result = result[result['Runs'] > 0]

print(result)
```


```python

```
