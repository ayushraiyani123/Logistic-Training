```python
import pandas as pd
```

### `Q-1:` You are given a Multi index DataFrame. You task is to swap level-0 index with level-0 column.
* Change Branch -> ('cse', 'ece') as columns at level-0 and ('delhi'	'mumbai') as level-0 Index
* And Sort on row index level-0


```python
# Given Code Snippets
index_val = [('cse',2019),('cse',2020),('cse',2021),('cse',2022),('ece',2019),('ece',2020),('ece',2021),('ece',2022)]
multiindex = pd.MultiIndex.from_tuples(index_val)
df = pd.DataFrame(
    [
        [1,2,0,0],
        [3,4,0,0],
        [5,6,0,0],
        [7,8,0,0],
        [9,10,0,0],
        [11,12,0,0],
        [13,14,0,0],
        [15,16,0,0],
    ],
    index = multiindex,
    columns = pd.MultiIndex.from_product([['delhi','mumbai'],['avg_package','students']])
)

df
```


```python
df.unstack(level = 0).stack(level = 0).sort_index(level=0,ascending=False)  
```

### `Q-2:` Covid Cases Data Set Problem
 Make a DataFrame Using both Covid Dataset. With Country name as Level-0 and Provinance/State as Level-1 Index and date, No of cases and No of Deaths as Columns.


```python
confirm = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTmqT3kxd0i0RUFiEnwA1Hboiunv28MeNTatZsIEqlPPB7mHrl0ttJL7utZ23_1s5FW8ZjODmB8jHIi/pub?gid=2142019845&single=true&output=csv')

deaths = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQn4nLCKIVZMw4e89YeRqgKaSAAwRFaZ6ILMW_FUejZ2tkv3Np1f9gD4QOl3ASHeLzWjOjfmLDKcCOF/pub?gid=212966958&single=true&output=csv")

confirm_table = confirm.melt(id_vars=['Province/State','Country/Region','Lat','Long'],var_name = 'Date', value_name = 'confirm_case', ignore_index=True)[['Province/State','Country/Region','Date','confirm_case']]
deaths_table = deaths.melt(id_vars=['Province/State','Country/Region','Lat','Long'],var_name = 'Date', value_name = 'Total_deaths', ignore_index=True)[['Province/State','Country/Region','Date','Total_deaths']]
final_deaths_table = deaths_table.melt(id_vars = ['Date','Total_deaths'],ignore_index = True)
final_deaths_table
# temp_table = final_deaths_table.merge(confirm_table,on=['Province/State','Country/Region','Date'])[['Province/State','Country/Region','Date','confirm_case','Total_deaths']]
# deaths_table.groupby('Province/State') #.melt(id_vars = ['Date','Total_deaths'],ignore_index = True)

death_table_copy = pd.merge(confirm_table,deaths_table,on=['Province/State','Country/Region','Date'])[['Province/State','Country/Region','Date','confirm_case','Total_deaths']]
final = death_table_copy.reset_index(drop=True)

df_final = (final.set_index(['Country/Region','Province/State','Date']).stack().unstack())
    #.rename(columns={'confirm_case':'No of cases','Total_deaths':'No of Deaths'}))
df_final

```

### `Q-3:` Show Country with Heighest death percent out of confirmed Cases.


```python
percentage = (final.groupby('Country/Region').agg({'confirm_case':'max', 'Total_deaths':'max'}).assign(Death_Percent=lambda x: (x['Total_deaths'] / x['confirm_case'] * 100).round(2)).fillna({'Death_Percent': 0}).sort_values('Death_Percent', ascending=False))
percentage
```

### `Q-4` : Make a dataframe for India from Covid Data with one extra column representing no of new cases.

* Just for Assumption "No of new cases" will be equal to difference of "no of cases" with previous day.
* First day new cases will be NaN or equal to no of cases

Say on 12/30/22 No of cases is - 44679608	and a day previous (12/29/22) no of cases is - 44679382.

Then for 12/30/22 -> No of New Cases  = 44679608 - 44679382 =

Note:- Try using shift Function

Try using the shift function

```
s = pd.Series([1,2,3,4,5,6])
s #-> [1,2,3,4,5,6]
s.shift(1) #-> [NaN, 1,2,3,4,5]
s.shift(-1) #-> [2,3,4,5,6, NaN]
```


```python
df_india = pd.DataFrame(df_final.loc['India']).reset_index()

# Convert Date to datetime and sort
df_india['Date'] = pd.to_datetime(df_india['Date'], format='%m/%d/%y')
df_india = df_india.sort_values('Date').reset_index(drop=True)

df_india['No of New Cases'] = df_india['confirm_case'] - df_india['confirm_case'].shift(1)
print("\nNo of New Cases in India:")
df_india[['Date','confirm_case','No of New Cases']]
```

### `Q-5:` Read the Dataset using the below given link and create a multi-index dataframe using the columns "Country" and "City/Town".

This dataset is about the most polluted cities in the world. You can get details from [here](https://www.kaggle.com/datasets/rajkumarpandey02/worlds-most-air-polluted-countries-cities).

**Dataset link:** https://tinyurl.com/2fe6vz4u Directly use this link to read.

**Task:**
1. Find out the name of the city of India which is most poluted based on PM10.
2. Find out the name of the city of India which has minumum pollution level based on PM10.
3. Do same operations (like 1 and 2) with the country China.
4. Make a pie chart based on the column "PM10" of the country Poland.
5. Make a bar chart based on the columns "PM2.5" and "PM10" of the countries Israel and Qatar.
6. Convert this MultiIndex DataFrame to Series by retaining the informations.


```python
df = pd.read_csv('https://tinyurl.com/2fe6vz4u').set_index(['Country', 'City/Town'])

# India - most and least polluted by PM10
india_max = df.loc['India']['PM10'].idxmax()
india_min = df.loc['India']['PM10'].idxmin()
print(f"1.India most polluted (PM10): {india_max}")
print(f"2.India least polluted (PM10): {india_min}")

# China - most and least polluted by PM10
china_max = df.loc['China']['PM10'].idxmax()
china_min = df.loc['China']['PM10'].idxmin()
print(f"3.China most polluted (PM10): {china_max}")
print(f"4.China least polluted (PM10): {china_min}")

# Poland PM10 pie chart
df.loc['Poland']['PM10'].plot(kind='pie', autopct='%1.1f%%', title='4.Poland - PM10 by City')

# Israel & Qatar bar chart
df.loc[['Israel', 'Qatar']][['PM2.5', 'PM10']].plot(kind='bar', title='5.Israel & Qatar - PM2.5 vs PM10')

# MultiIndex DataFrame to Series
series = df.stack()
print("\n6.Restored Series\n",series)
```
