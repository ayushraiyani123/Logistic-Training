```python
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("ggplot")
```

### `Q 1-3` Using the 'diamonds' dataset - sns.load_dataset('diamonds')
1. Create a violinplot of 'price' grouped by 'cut'.
2. Create regplot on `carat` vs `price`. and give hue on 'cut'
3. Create boxplot on 'color' and 'price'


```python
diamond.head()
```


```python
diamond = sns.load_dataset('diamonds')
sns.catplot(data = diamond, x = 'cut',y='price',kind = 'violin')
plt.show()
```


```python
sns.lmplot(data=diamond,x='carat',y='price',hue='cut')
plt.show()
```


```python

sns.catplot(data = diamond, x = 'color',y='price',kind = 'box')
plt.show()
```

### `Q 4` Using the 'Taxis' dataset - sns.load_dataset('taxis')
4.1. Create a categorical estimate plot of the totl fare - 'total' for each payment type - 'payment'.

4.2. Create a regression plot on time of ride  vs total fare. You will need to calculate ride time using pickup and dropoff column.

4.3 Give hue on payment type. and Another plot hue on taxi 'color'. Observe the plot.


```python
taxies.head()
```


```python
taxies = sns.load_dataset('taxis')
sns.barplot(data=taxies, x='payment', y='total')
plt.show()
```


```python
# 4.2. Create a regression plot on time of ride vs total fare. You will need to calculate ride time using pickup and dropoff column.

taxies['pickup'] = pd.to_datetime(taxies['pickup'])
taxies['dropoff'] = pd.to_datetime(taxies['dropoff'])

# Calculate ride time (dropoff - pickup)
taxies['time_of_ride'] = taxies['dropoff'] - taxies['pickup']
taxies['ride_minutes'] = taxies['time_of_ride'].dt.total_seconds() / 60

sns.regplot(data=taxies,x='ride_minutes',y='total')
plt.show()
```


```python
# 4.3 Give hue on payment type. and Another plot hue on taxi 'color'. Observe the plot.
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# Plot 1: Hue on payment type
sns.scatterplot(data=taxies,x='distance',y='total',hue='payment',palette='Set1',alpha=0.7,s=80,ax=ax1)
ax1.set_title('Fare vs Distance\n(Hue: Payment Type)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Distance (km)', fontsize=12, fontweight='bold')
ax1.set_ylabel('Fare ($)', fontsize=12, fontweight='bold')

# Plot 2: Hue on taxi color
sns.scatterplot(data=taxies,x='distance',y='total',hue='color',palette='Set2',alpha=0.7,s=80,ax=ax2)
ax2.set_title('Fare vs Distance\n(Hue: Taxi Color)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Distance (km)', fontsize=12, fontweight='bold')
ax2.set_ylabel('Fare ($)', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()
```

## Problem 5-12:


```python
ins
```

### **`Problem 5:`** Draw a strip plot and swarm plot between "gender" and "bloodpressure" w.r.t "smoker" (use as hue parameter). Also add title to the charts.


```python
# ins = pd.read_csv('insurance_data - insurance_data.csv')
fig, (g, f) = plt.subplots(1, 2, figsize=(14, 6))

sns.stripplot(data = ins, x = 'gender', y = 'bloodpressure',hue = 'smoker',ax = g)
g.set_title('Strip Plot', fontsize=14, fontweight='bold')
sns.swarmplot(data = ins, x = 'gender', y = 'bloodpressure',hue = 'smoker',s=5,ax= f)
f.set_title('Swarm Plot', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

### **`Problem 6:`** Draw a Box-plot and a Violin plot of which x-axis represents the "region" and the y-axis represents the "bmi". Also add extra information of the column "diabetic".


```python
# ins = pd.read_csv('insurance_data - insurance_data.csv')
fig, (b, v) = plt.subplots(1, 2, figsize=(14, 6))

sns.boxplot(data = ins, x = 'region', y = 'bmi',hue = 'diabetic',ax = b)
b.set_title('Box Plot', fontsize=14, fontweight='bold')
sns.violinplot(data = ins, x = 'region', y = 'bmi',ax= v,hue = 'diabetic')
v.set_title('Violin Plot', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

### **`Problem  7:`** Draw a bar plot and point plot of which x-axis represents the "gender" and y-axis represents "claim". Also add extra information about "smoker" column.


```python
# ins = pd.read_csv('insurance_data - insurance_data.csv')
fig, (b, p) = plt.subplots(1, 2, figsize=(14, 6))

sns.boxplot(data = ins, x = 'gender', y = 'claim',hue = 'smoker',ax = b)
b.set_title('Bar Plot', fontsize=14, fontweight='bold')
sns.pointplot(data = ins, x = 'gender', y = 'claim',ax= p,hue = 'smoker')
p.set_title('Point Plot', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

### **`Problem 8:`** Draw a reg plot between "age" and "bmi" columns.


```python
sns.regplot(data = ins,x='bmi',y='age')
plt.show()
```

### **`Problem 9:`** Draw a pair plot of the insurance data. Use "gender" as hue parameter.


```python
sns.pairplot(ins,hue='gender')
plt.show()
```

### **`Problem 10:`** Draw a pair grid of the insurance data and use "diabetic" column as a hue parameter. Also, make the diagonal plots as box-plot, upper parts as scatter plot and the lower parts as kde plot.


```python
# vars
o = sns.PairGrid(data=ins,hue='diabetic')
o.map_diag(sns.boxplot)
o.map_upper(sns.scatterplot)
o.map_lower(lambda x, y, **kw: None if len(x[~(np.isnan(x)|np.isnan(y))]) < 3 or np.std(x[~(np.isnan(x)|np.isnan(y))]) == 0 or np.std(y[~(np.isnan(x)|np.isnan(y))]) == 0 else sns.kdeplot(x=x[~(np.isnan(x)|np.isnan(y))], y=y[~(np.isnan(x)|np.isnan(y))], fill=True, cmap='viridis',warn_singular=False, alpha=0.7, **kw))
plt.show()


```

### **`Prolem 11:`** Draw a joint plot as scatter between "bloodpressure" and "bmi". Use "smoker" as hue parameter.


```python
sns.jointplot(data=ins,x='bloodpressure',y='bmi',kind='scatter',hue='smoker')
plt.show()
```

### **`Problem 12:`** Draw a joint grid of which x-axis represents "age" and y-axis represents "claim". Draw


```python
g = sns.JointGrid(data=ins,x='age',y='claim')
g.plot(sns.scatterplot,sns.histplot)
```


```python

```
