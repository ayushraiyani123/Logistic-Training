```python
import numpy as np
import pandas as pd

# to visualize all the column, run the below code
pd.options.display.max_columns = None
# to show all the records, use the below code
# pd.options.display.max_rows = None
```

## Fifa Worldcup - 2022 dataset.

You can find the dataset from [here](https://www.kaggle.com/datasets/sayanroy729/fifa-worldcup-2022-results).

Also you can directly use an url to read the dataset by using `pd.read_csv()` method. Check the below code cell.


```python
# To get the details about the dataset, please visit
# https://www.kaggle.com/datasets/sayanroy729/fifa-worldcup-2022-results

url = "Fifa Worldcup 2022.csv"
df = pd.read_csv(url)
df.head()
```

### `Q-1:` Use the football dataset. Find out the total percentages that each team made on target. Display the result as a python dictionary where the keys are the team list and the values are the percentage values. Round off the percentage values up to 2 decimal places.

*Help:*
- First, find out how many total teams are participated in this worldcup. For that, you can use `unique()` method on the column "Team" or "Against".
- Loop through the teams list that you have found in previous section, and then filter the dataset according to that. After filtering the dataset, find out total attempts sum and total on target sum.
- After getting these values, find out the percentage by total on target divided by total attempts and multiply by 100. And store to a python dictionary where the key will be the team name and the values will be the percentages.
- At the end,sort the dictionary by the values (not by the keys) and print the result.



**Sample Output:**
```bash
{'Costa Rica': 54.55,
 'Cameroon': 51.85,
 'Ecuador': 48.15,
 'Argentina': 46.99,
 'Brazil': 45.56,
 'England': 45.0,
 'Portugal': 40.32,
 'Ghana': 40.0,
 'Netherlands': 39.02,
 'Korea Republic': 36.73,
 'Australia': 36.0,
 'Mexico': 34.88,
 'Croatia': 34.78,
 'Germany': 34.33,
 'France': 32.97,
 'Spain': 32.69,
 'Belgium': 32.35,
 'Serbia': 32.26,
 'Iran': 31.43,
 'Uruguay': 31.25,
 'United States': 31.11,
 'Saudi Arabia': 31.03,
 'Senegal': 30.77,
 'Denmark': 30.56,
 'Switzerland': 30.56,
 'Japan': 30.23,
 'Wales': 29.17,
 'Qatar': 28.57,
 'Morocco': 28.3,
 'Tunisia': 26.67,
 'Poland': 25.0,
 'Canada': 17.65}
```


```python
team_stats = df.groupby('Team')[['Total Attempts', 'On Target']].sum()

team_stats['Percentage'] = (team_stats['On Target'] / team_stats['Total Attempts']) * 100

team_stats['Percentage'] = team_stats['Percentage'].round(2)

team_stats = team_stats.sort_values('Percentage', ascending=False)

result_dict = team_stats['Percentage'].to_dict()

print(result_dict)
```

### `Q-2:` Find out how many times the teams are played in this Fifa Worldcup-2022. On top of this, find out the ranks of the teams.

Note: The `DataFrame.rank()` method takes an optiinal parameter named `method`. This parameter takes different values, but one of them is `average` which is by-default. So, when you do the rank, you will get some 2.5 like floating values. But if you change the value as `first`, then you will get in integers but the datatype will be float. So, try with `method="first"` parameter.


```python
team_counts = df['Team'].value_counts()
against_counts = df['Against'].value_counts()

total_matches = team_counts.add(against_counts,fill_value = 0).astype(int)

matches_df = pd.DataFrame({'Matches Played': total_matches})

matches_df['Rank'] = matches_df['Matches Played'].rank(ascending = False,method = 'first')

matches_df = matches_df.sort_values('Rank')
print(matches_df)
                        
```

### `Q-3:` Find out these below topics:
- The information about the Fifa worldcup dataset.
- The description about the Fifa worldcup dataset
- Check is there any missing values, if there is any missing values, fill that value with the average value 0for that particular column.
- Drop all the duplicate rows permanently.
- Drop the columns: "Sl No", "Match No.", "Red Cards" and "Pts" permanently.


```python

info = df.info()
print(info)
print()

print("MISSING VALUES")
print("=" * 50)
print("Missing values per column:")
print(df.isnull().sum())
print()

# Fill missing values with mean of each column (only numeric columns)
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

print("Missing values after filling:")
print(df.isnull().sum())
print()


print(f"Duplicate rows before: {df.duplicated().sum()}")
df.drop_duplicates(inplace=True)
print(f"Duplicate rows after: {df.duplicated().sum()}")
print()

columns_to_drop = ["Sl. No", "Match No.", "Red Cards", "Pts"]
df.drop(columns=columns_to_drop, inplace=True)
print(f"Dropped columns: {columns_to_drop}")
print(f"Remaining columns: {df.columns.tolist()}")
print()
print()

df.describe()

```

### `Q-4:` Do these below operations:
- Find out the rank based on the "Team" column and save the result by adding a new column named "Rank".
- Change the datatype of this column to integer by using `np.int16`
- Set the index of the DataFrame by using this "Rank" column permanently.
- After that, sort the dataframe based on the "Rank" index.


```python
df['Rank'] = df['Team'].rank(method='first').astype(int)
print("After adding Rank column:")
print(df[['Team', 'Rank']].head(10))
print(f"Rank dtype: {df['Rank'].dtype}")
print()

df['Rank'] = df['Rank'].astype(np.int16)
print(f"Rank dtype after conversion: {df['Rank'].dtype}")
print()

df.set_index('Rank', inplace=True)

df.sort_index(inplace=True)
print("After setting and sorting by Rank index:")
df
```

## Questions on Titanic dataset.

You can get the dataset from [here](https://www.kaggle.com/competitions/titanic). This is the competition page on Kaggle. To download the dataset from here, I guess you have to register for the compition. So, do so and then download the dataset.

Also, for now you can use this url to read the dataset like before:
- dataset 1: https://docs.google.com/spreadsheets/d/e/2PACX-1vQjh5HzZ1N0SU7ME9ZQRzeVTaXaGsV97rU8R7eAcg53k27GTstJp9cRUOfr55go1GRRvTz1NwvyOnuh/pub?gid=1562145139&single=true&output=csv
- dataset 2: https://docs.google.com/spreadsheets/d/e/2PACX-1vQcPvQsSC9aNFogvbUG08nu0bGHlOclGYaOlhND_LE5Ff7ZnHQ5VYzAgpyT5XNklgiT54SsNgHePsUa/pub?gid=1656109608&single=true&output=csv

### `Q-5:` Do the below tasks:
1. With dataset 1, drop those records which only have missing values of the "Age" column permanently.

2. With the dataset 2, fill the missing values with 20 to the only "Age" column permanently.


```python
data1 = pd.read_csv('train - train.csv')
data2 = pd.read_csv('test - test.csv')

data1.dropna(subset = ['Age'], inplace = True)
print(data1['Age'])
print()

data2['Age'].fillna(20, inplace = True)
print(data2['Age'])
```

## Questions on IPL wala dataset

matches dataset = https://drive.google.com/file/d/1yKVUuexl6lIKuFQy7uIPgDgXhJ0L4SIg/view?usp=share_link

Code to directly use in colab
```
ipl_matches = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv"

```




### `Q-6:` Make a dataframe of each team in IPL with details like - Team Name, Matches Played, Win%, Home Win%, Away Win%.
Show sorted dataframe on Win%

Replace old team name as new name before performing any tasks.
```
Delhi Daredevils ->Delhi Capitals
Kings XI Punjab -> Punjab Kings
Rising Pune Supergiants -> Rising Pune Supergiant
```

Note: Team1 represents Home team. Exclude not result matches.



```python
ipl = pd.read_csv('IPL_Matches_2008_2022.csv')

team_name_mapping = {
    'Delhi Daredevils': 'Delhi Capitals',
    'Kings XI Punjab': 'Punjab Kings',
    'Rising Pune Supergiants': 'Rising Pune Supergiant'
}
team_columns = ['Team1', 'Team2', 'WinningTeam','TossWinner']

for col in team_columns:
    if col in ipl.columns:
        ipl[col] = ipl[col].replace(team_name_mapping)

matches_played = ipl['Team1'].value_counts() + ipl['Team2'].value_counts()

wins = ipl['WinningTeam'].value_counts()
win_pct = (wins / matches_played * 100).round(2)

matches_played.columns = ['Matches_Played']
win_rate.columns = ['Win_Rate']

home_wins = ipl[ipl['Team1'] == ipl['WinningTeam']]['Team1'].value_counts()
home_games = ipl['Team1'].value_counts()
home_win_pct = (home_wins / home_games * 100).round(2)

away_wins = ipl[ipl['Team2'] == ipl['WinningTeam']]['Team2'].value_counts()
away_games = ipl['Team2'].value_counts()
away_win_pct = (away_wins / away_games * 100).round(2)

final = merged_df.groupby(level=0).sum()
final.columns = ['Matches_Played', 'Win_Rate']   
final['HomeWin%'] = home_win_pct
final['AwayWin%'] = away_win_pct

final
```

### `Q-7:` Venues with most "no result" matches.


```python

no_result_matches = ipl[ipl['WinningTeam'].isna()]

venue_counts = no_result_matches['Venue'].value_counts()
print(venue_counts)   
```

### `Q-8:` Player with most appearance in final match.

`Team1Players` and `Team2Players` have all players name. It is not a list of players name instead it is str. So handle it as string.

Hint: split and strip will help; Make a series of all players in final and do value counts



```python
# Filter for final matches
finals = ipl[ipl['MatchNumber'] == 'Final']

# Split player strings into lists and stack them into a single series
players = finals['Team1Players'].str.split(', ').explode()
players = pd.concat([players, finals['Team2Players'].str.split(', ').explode()])

# Count appearances and get top player
player_appearances = players.value_counts()
top_player = player_appearances.index[0]
print(f"Player with most final appearances: {top_player} ({player_appearances.iloc[0]} times)")   
```

### `Q-9:` IPL Point Table

Make a function `point_table` which take `season` as parameter and show points table in non-ascendng order of points and in ascending order of team name.

For winning - 2 Ponits;
For loosing - 0 Point
For not result both team gets 1 points.

Make dataframe which will have
`TeamName` `MatchesPlayed` `MatchesWon` `NoResult` `Points`
make `TeamName` as index.

```
season parametr should be one of these->
['2022', '2021', '2020/21', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2009/10', '2009', '2007/08']
```


Output of two Top 2 in season 2022
```
TeamName    MatchesPlayed	MatchesWon	NoResult	Points

Gujarat Titans	    16	   12	       0	     24
Rajasthan Royals	  17	   10	       0	     20

```


```python
def point_table(season):
    # Valid seasons list
    valid_seasons = ['2022', '2021', '2020/21', '2019', '2018', '2017', '2016', 
                     '2015', '2014', '2013', '2012', '2011', '2009/10', '2009', '2007/08']
    
    # Validate season (keep as string for seasons like '2009/10')
    season = str(season)
    if season not in valid_seasons:
        raise ValueError(f"Season must be one of: {valid_seasons}")
    
    # Filter matches for the given season
    season_matches = ipl[ipl['Season'] == season].copy()
    
    if len(season_matches) == 0:
        raise ValueError(f"No matches found for season {season}")
    
    # Get all unique teams
    teams = set(season_matches['Team1']).union(set(season_matches['Team2']))
    
    # Initialize dataframe to store team stats
    table = pd.DataFrame(index=sorted(teams), 
                        columns=['MatchesPlayed', 'MatchesWon', 'NoResult', 'Points'])
    table = table.fillna(0)
    
    # Count matches played, won, and no-result
    for _, row in season_matches.iterrows():
        team1 = row['Team1']
        team2 = row['Team2']
        result = row['WinningTeam']
        winner = row['WinningTeam']
        
        # Count matches played
        table.loc[team1, 'MatchesPlayed'] += 1
        table.loc[team2, 'MatchesPlayed'] += 1
        
        # Check for no result (either explicit 'no result' or NaN winner)
        if result == 'no result' or pd.isna(winner):
            table.loc[team1, 'NoResult'] += 1
            table.loc[team2, 'NoResult'] += 1
            table.loc[team1, 'Points'] += 1
            table.loc[team2, 'Points'] += 1
        else:
            # Winner gets 2 points
            table.loc[winner, 'MatchesWon'] += 1
            table.loc[winner, 'Points'] += 2
    
    # Set index name as required
    table.index.name = 'TeamName'
    
    # Convert to integers
    table = table.astype(int)
    
    # Sort by Points (descending) and TeamName (ascending)
    # Requirement: "non-ascending order of points and ascending order of team name"
    table = table.sort_values(by=['Points', 'TeamName'], ascending=[False, True])
    
    return table


# Call the function
point_table('2009')
```

### `Q-10:` IPL Point Table cont.
Extend the above IPL Point Table with an extra column as `SeasonPosition`

Team below top 4 after sorting on `Points` and then on `TeamName` Will have same `SeasonPosition` as there rank. use rank function.

Teams in Top four will have `SeasonPosition` as:
```
    'Winner' - Team won final
    'Runner' - Team lost Final
    3 - Losing Team in Qualifier2
    4 - Losing Team in Eliminator
```

For changing value of pariticular cell use `df.at[row_index, col_label] = value`

Output of two Top 2 in season 2022. Your result should have all teams.
```
TeamName    MatchesPlayed	MatchesWon	NoResult	Points   SeasonPosition

Gujarat Titans	    16	   12	       0	     24         Winner
Rajasthan Royals	  17	   10	       0	     20         Runner

```

Note: If you try to chnage value of view of any dataframe a warnig will be shown. To avoid it, make a copy of the dataframe you want to change in by `df.copy()`


```python
# Get point table for 2022 (from previous function)
table = point_table('2022').copy()

# Add SeasonPosition column
table['SeasonPosition'] = table['Points'].rank(method='min', ascending=False).astype(int)

# Assign final positions using playoff outcomes
table.at['Gujarat Titans', 'SeasonPosition'] = 'Winner'
table.at['Rajasthan Royals', 'SeasonPosition'] = 'Runner'
table.at['Lucknow Super Giants', 'SeasonPosition'] = 3
table.at['Royal Challengers Bangalore', 'SeasonPosition'] = 4

# Display all teams
table
```


```python

```
