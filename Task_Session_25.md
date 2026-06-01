```python
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("ggplot")
```

### `Q-1:` Using Gapminder Data
1. Create a scatter plot of 'gdpPercap' against 'lifeExp' for the year 2007, with the size of the markers determined by 'pop' and the color determined by 'continent'.


```python
import plotly.express as px
df = px.data.gapminder()
df.head()
```


```python
sample = df[df['year'] == 2007]
sns.relplot(data=sample, x='gdpPercap', y='lifeExp',kind = 'scatter',hue = 'continent',size = 'pop')
plt.show()
```

### `Q-2-3:` Using `flights` dataset of seaborn.

2. Using the "flights" dataset that comes with seaborn, create a heatmap that shows the average number of passengers per month for each year.

3. Using the seaborn's flight dataset, create a clustermap to visualize the relationship between the number of passengers, months, and year.



```python
flights = sns.load_dataset('flights')
flights.tail()
```


```python

pivot = flights.pivot_table(values='passengers',index='year',columns='month',aggfunc='mean',observed=False)

plt.figure(figsize=(15,15))
sns.heatmap(pivot,annot=True,fmt='.0f',cmap='YlOrRd',linewidths=0.5,cbar_kws={'label': 'Average Passengers'})
plt.show()


```


```python

pivot = flights.pivot(index='year', columns='month', values='passengers')

g = sns.clustermap(pivot,cmap='YlOrRd',annot=True,fmt='d', annot_kws={'size': 9}, linewidths=0.5,figsize=(14, 10))             # 'd' = integer format (112 instead of 1.1e+02)
g.fig.suptitle('Clustermap: Passengers by Year and Month',fontsize=16, fontweight='bold', y=1.02)
# plt.savefig('flights_clustermap.png', dpi=300, bbox_inches='tight')
plt.show()
```

## For questions 4-8:

For these qestions, an insurance dataset is used. You can get details from [here](https://www.kaggle.com/datasets/thedevastator/insurance-claim-analysis-demographic-and-health). And if you want this dataset to use directly, then you can use this link: **https://docs.google.com/spreadsheets/d/e/2PACX-1vQVpcVtdYdZU4zU4-lqxt-iPHkyndDWs_aqEDUu9ZodlJ48Dku0PFgdXlj2N5RCmwXJrNtZLsI_wEVf/pub?gid=220677750&single=true&output=csv**

### **`Q-4:`** Draw a scatter plot based on the below conditions:
1. x-axis should be "age" and y-axis should be "bmi".
2. For hue, size and style parameters use "diabetic", "gender" and "smoker" column respectively.
3. Add title to your chart.
4. Age should be less than 70 percentiles.
5. BMI should be greater than the average value of the filtered age dataset.


```python
df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQVpcVtdYdZU4zU4-lqxt-iPHkyndDWs_aqEDUu9ZodlJ48Dku0PFgdXlj2N5RCmwXJrNtZLsI_wEVf/pub?gid=220677750&single=true&output=csv')
df.head()
```


```python

age_70th = df['age'].quantile(0.70)
age_filtered = df[df['age'] < age_70th].copy()
bmi_avg = age_filtered['bmi'].mean()
final_data = age_filtered[age_filtered['bmi'] > bmi_avg].copy()

b = sns.relplot(data = final_data,x='age',y='bmi',kind = 'scatter',hue = 'diabetic',style = 'smoker',size = 'gender')
b.fig.suptitle('Scatterplot: Age vs BMI',fontsize=16, fontweight='bold', y=1.02)
plt.show()
```

### **`Q-5:`** Draw a line plot by using the below informations

1. bloodpressure vs children
2. Blood-pressure values should be between 90 and 100. The upper and lower limit are included.
3. Show the details of "smoker".


```python
new_df = df[df['bloodpressure'] >= 90][df['bloodpressure'] <= 100]
sns.relplot(data = new_df,x = 'bloodpressure',y='children',hue = 'smoker')
plt.show()
```

### **`Q-6:`** Draw a histogram using displot

- based on "age" column.
- Show details of "smoker" (hue).
- Create 2 separate charts for the above 2 conditions based on "gender" side-by-side.


```python

sns.displot(data=df, x='age', kind='hist',col='gender',element='step',hue = 'smoker')
plt.show()
```

### **`Q-7:`** Draw a kde plot between "age" and "bloodpressure".


```python
sns.displot(data=df,x='age',y = 'bloodpressure',kind='kde')
plt.show()
```

### **`Q-8:`** Draw a clustermap between between "age", "bmi" and "bloodpressure".


```python
df['bmi_bin'] = pd.cut(df['bmi'], bins=5, labels=['Very Low', 'Low', 'Normal', 'High', 'Very High'])

p = df.pivot_table(index='age', columns='bmi', values='bloodpressure')
p = p.fillna(p.mean())

x = sns.clustermap(p,cmap='viridis', linewidths=0.5,figsize=(20, 15))      
x.fig.suptitle('Clustermap: Between "age", "bmi" and "bloodpressure',fontsize=16, fontweight='bold', y=1.02)
plt.show()


# print("NaN count:", p.isna().sum().sum())
```


```python

```


```python

```
