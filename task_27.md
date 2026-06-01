```python
import pandas as pd
import requests
from io import StringIO
```

### Problem-1:

You are given a SQL file link: https://drive.google.com/file/d/1WFt7B84LTHhMueoKmz8W-PRo7xXqmZf3/view?usp=share_link. Read the data by using the file and store it in a excel file. In this data, there are 3 tables named "invoices", "order_leads" and "sales_sql". So create 3 sheets to your excel file.


```python
import pandas as pd, re
sql = open("supermarket.sql").read()

def parse(sql, t):
    cols = re.findall(r'`([^`]+)`', re.search(rf'CREATE TABLE `{t}` \((.+?)\) ENGINE', sql, re.S).group(1))
    rows = []
    for b in re.findall(rf'INSERT INTO `{t}` VALUES (.+?);', sql, re.S):
        for r in re.findall(r'\(([^)]+)\)', b):
            v, cur, q = [], "", False
            for c in r:
                if c == "'" and not q: q = True
                elif c == "'" and q: q = False
                elif c == ',' and not q: v.append(cur.strip()); cur = ""; continue
                cur += c
            v.append(cur.strip())
            rows.append([None if x=='NULL' else x.strip("'") if x.startswith("'") else int(x) for x in v])
    return pd.DataFrame(rows, columns=cols)

with pd.ExcelWriter("sales_data.xlsx") as w:
    for t in ['invoices','orderleads','salesteam']:
        parse(sql, t).to_excel(w, sheet_name=t, index=False)
        print(f"{t}: {len(parse(sql, t))} rows")
```


```python
# pd.read_excel("sales_data.xlsx")
xls = pd.ExcelFile("sales_data.xlsx")

print(f"Total sheets: {len(xls.sheet_names)}")
print(f"Names: {xls.sheet_names}")

for sheet in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet)
    print(f"\n{sheet}: {len(df)} rows x {len(df.columns)} cols")
```

### Problem-2

Go to the site: https://rapidapi.com/wirefreethought/api/geodb-cities. From here, you have to grab the API and have to choose proper routes to get the cities of different countries. After getting the right API, hit that API and create a dataframe of all the cities that you can get by using the API. Then store the dataframe to a SQL. If you need to create an account or have to subscribe, then do that (it has free subscription but has some limitations. Use that free subscription and modify your accordingly to get all the data).  


```python
import requests
import pandas as pd
import sqlite3
import time

API_KEY = "1f4d33c121mshad2d68f7b40418fp1daee6jsn930f98314d6a"

url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"
headers = {"X-RapidAPI-Key": API_KEY, "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"}

cities = []
offset = 0

# Fetch only 10,000 cities (enough for assignment)
while len(cities) < 1000:
    r = requests.get(url, headers=headers, params={"offset": offset, "limit": 10, "hateoasMode": "false"})
    data = r.json().get("data", [])
    if not data: break
    cities.extend(data)
    print(f"{len(cities)}/1000")
    offset += 10
    time.sleep(1.1)

pd.DataFrame(cities).to_sql("cities", sqlite3.connect("cities.db"), if_exists="replace", index=False)
print(f"Done! {len(cities)} cities saved.")
```

### Problem 3:

Go to this url: https://www.flipkart.com/search?q=smartphones. This is the url to find phones in flipkart website. You have to extract the below things:
1. image url of the phone
2. name of the image
3. average ratings
4. total ratings
5. total reviews
6. discounted price
7. actual price

Extract all the phones which are available in this website. So you have to use the pagination concept. **Also after requesting every page through the url, please wait for a while (minimum 2-3 seconds), otherwise your IP address can be banned to access the flipkart website later.**

After collecting all the data, save that in a JSON file.


```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import random

driver = webdriver.Chrome()
all_phones = []

for page in range(1, 4):
    print(f"\nPage {page}")
    driver.get(f"https://www.flipkart.com/search?q=smartphones&page={page}")
    time.sleep(5)
    
    # Using the working selector from debug
    products = driver.find_elements(By.CSS_SELECTOR, "div[data-id]")
    print(f"Found {len(products)} products")
    
    for p in products:
        try:
            img = p.find_element(By.TAG_NAME, "img")
            phone = {
                "image": img.get_attribute("src"),
                "name": img.get_attribute("alt"),
                "price": p.find_element(By.CSS_SELECTOR, "[class*='30jeq3']").text if p.find_elements(By.CSS_SELECTOR, "[class*='30jeq3']") else "N/A",
                "rating": p.find_element(By.CSS_SELECTOR, "[class*='LWZlK']").text if p.find_elements(By.CSS_SELECTOR, "[class*='LWZlK']") else "N/A"
            }
            all_phones.append(phone)
            print(f"  ✓ Added: {phone['name'][:50]}")
        except Exception as e:
            continue
    
    time.sleep(random.uniform(3, 4))

driver.quit()

with open("phones.json", "w", encoding="utf-8") as f:
    json.dump(all_phones, f, indent=2)

print(f"\n✅ Saved {len(all_phones)} phones to phones.json")
```


```python

```
