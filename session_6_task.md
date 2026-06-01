### **`Problem-1:`** Write a Python function that takes a list and returns a new list with unique elements of the first list.

**Exercise 1:**

Input:

```bash
[1,2,3,3,3,3,4,5]
```

Output:

```bash
[1, 2, 3, 4, 5]
```


```python
def get_unique_elements(input_list):
    """
    Returns a new list with unique elements from the input list,
    preserving the original order of first appearance.
    """
    seen = set()
    result = []
    
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result

get_unique_elements([1,2,3,3,3,3,4,5])
```

### **`Problem-2:`** Write a Python function that accepts a hyphen-separated sequence of words as parameter and returns the words in a hyphen-separated sequence after sorting them alphabetically.

**Example 1:**

Input:
```bash
green-red-yellow-black-white
```

Output:
```bash
black-green-red-white-yellow
```


```python
def sort_hyphenated_words(sequence):
    """
    Accepts a hyphen-separated sequence of words and returns them sorted alphabetically.
    """
    # Split the string by hyphen
    words = sequence.split('-')
    
    # Sort the list alphabetically (case-sensitive)
    words.sort()
    
    # Join back with hyphens
    return '-'.join(words)

sort_hyphenated_words('green-red-yellow-black-white')
```

### **`Problem 3:`** Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

```
Sample String : 'CampusX is an Online Mentorship Program fOr EnginEering studentS.'
Expected Output :
No. of Upper case characters :  9
No. of Lower case Characters :  47
```


```python
def count_case_characters(text):
    """
    Accepts a string and calculates the number of uppercase and lowercase letters.
    """
    upper_count = 0
    lower_count = 0
    
    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    
    print(f"No. of Upper case characters : {upper_count}")
    print(f"No. of Lower case Characters : {lower_count}")

# Test
sample_string = 'CampusX is an Online Mentorship Program fOr EnginEering studentS.'
count_case_characters(sample_string)
```

### **`Problem 4:`** Write a Python program to print the even numbers from a given list.
```
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
```


```python
def even_numers(input_list):
    ''' This function prints print the even numbers from a given list  '''
    result = []
    for num in input_list:
        if num%2==0:
            result.append(num)
    return result

even_numers([1, 2, 3, 4, 5, 6, 7, 8, 9])
```

### **`Problem 5:`** Write a Python function to check whether a number is perfect or not.

A Perfect number is a number that is half the sum of all of its positive divisors (including itself).

Example :

```
The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6.
Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6.

The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.
```



```python
def is_perfect_number(n):
    """
    Check if a number is perfect.
    A perfect number equals the sum of its proper positive divisors (excluding itself).
    """
    if n <= 1:
        return False
    
    divisor_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisor_sum == n

# # Alternative using the "half sum of all divisors" definition:
# def is_perfect_number_alt(n):
#     """
#     Check if number equals half the sum of all its positive divisors (including itself).
#     """
#     if n <= 0:
#         return False
    
#     all_divisors_sum = sum(i for i in range(1, n + 1) if n % i == 0)
#     return all_divisors_sum // 2 == n

is_perfect_number(496)
```

### **`Problem-6:`** Write a Python function to concatenate any no of dictionaries to create a new one.

```
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
```


```python
def concatenate_dictionaries(*dicts):
    """
    Concatenates any number of dictionaries into a new one.
    """
    result = {}
    for dictionary in dicts:
        result.update(dictionary)
    return result

# Usage with sample data
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

result = concatenate_dictionaries(dic1, dic2, dic3)
print(result)  
```

`Problem-7` Write a python function that accepts a string as input and returns the word with most occurence.

```
Input:
hello how are you i am fine thank you
```

```
Output
you -> 2
```


```python
def most_frequent_word(text):
    if not text or not text.strip():
        return None
    
    words = text.split()
    word_counts = {}
    
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    
    # Find word with max count
    max_word = max(word_counts, key=word_counts.get)
    return f"{max_word} -> {word_counts[max_word]}"

most_frequent_word('hello how are you i am fine thank you')
```

`Problem-8` Write a python function that receives a list of integers and prints out a histogram of bin size 10

```
Input:
[13,42,15,37,22,39,41,50]
```

```
Output:
{11-20:2,21-30:1,31-40:2,41-50:3}
```


```python
def create_histogram_sorted(data):
    ''' Creates a histogram with bin size 10 from a list of integers.
    Bins are formatted as '11-20', '21-30', etc. '''
    histogram = {}
    for num in data:
        bin_start = ((num - 1) // 10) * 10 + 1
        bin_end = bin_start + 9
        bin_key = f"{bin_start}-{bin_end}"
        histogram[bin_key] = histogram.get(bin_key, 0) + 1
    
    # Return sorted dictionary by bin start value
    return dict(sorted(histogram.items(), key=lambda x: int(x[0].split('-')[0])))
create_histogram_sorted([13,42,15,37,22,39,41,50])
```

`Problem-9` Write a python function that accepts a list of 2D co-ordinates and a query point, and then finds the the co-ordinate which is closest in terms of distance from the query point.

```
List of Coordinates
[(1,1),(2,2),(3,3),(4,4)]
Query Point
(0,0)
```

```
Output
Nearest to (0,0) is (1,1)
```


```python
def find_nearest_coordinate(coordinates, query_point):
    ''' 
    Finds the coordinate closest to the query point. '''
    nearest = min(coordinates, 
                  key=lambda c: (c[0] - query_point[0])**2 + (c[1] - query_point[1])**2)
    return f"Nearest to {query_point} is {nearest}"
    
List_of_coordinates=[(1,1),(2,2),(3,3),(4,4)]
Query_points = (0,0)
find_nearest_coordinate(List_of_coordinates,Query_points)

# def find_nearest_coordinate(coordinates, query_point):
#     """
#     Finds the coordinate closest to the query point.
#     Uses squared distance to avoid sqrt calculation.
#     """
#     if not coordinates:
#         return None
    
#     # Initialize with first coordinate
#     nearest = coordinates[0]
#     qx, qy = query_point
    
#     # Calculate squared distance for first point (dx² + dy²)
#     min_dist_sq = (coordinates[0][0] - qx)**2 + (coordinates[0][1] - qy)**2
    
#     # Check remaining coordinates
#     for i in range(1, len(coordinates)):
#         cx, cy = coordinates[i]
#         dist_sq = (cx - qx)**2 + (cy - qy)**2
        
#         if dist_sq < min_dist_sq:
#             min_dist_sq = dist_sq
#             nearest = coordinates[i]
    
#     return "Nearest to " + str(query_point) + " is " + str(nearest)

# # Usage
# coords = [(1, 1), (2, 2), (3, 3), (4, 4)]
# query = (0, 0)
# print(find_nearest_coordinate(coords, query))
# # Output: Nearest to (0, 0) is (1, 1)
```

# `Problem-10`:Write a python program that receives a list of strings and performs bag of word operation on those strings

https://en.wikipedia.org/wiki/Bag-of-words_model


```python
from sklearn.feature_extraction.text import CountVectorizer

def bag_of_words(documents):
    """
    Performs Bag of Words operation on a list of strings.
    Returns the vocabulary and document-term matrix.
    """
    # Initialize CountVectorizer
    vectorizer = CountVectorizer()
    
    # Fit and transform the documents
    X = vectorizer.fit_transform(documents)
    
    # Get vocabulary (feature names)
    vocabulary = vectorizer.get_feature_names_out()
    
    # Convert to array for display
    vectors = X.toarray()
    
    return vocabulary, vectors, vectorizer

# Example usage
if __name__ == "__main__":
    # Input: List of strings
    documents = [
        "The cat sat on the mat",
        "The dog sat on the log", 
        "Cats and dogs are friends"
    ]
    
    print("Input Documents:")
    for i, doc in enumerate(documents, 1):
        print(f"  Doc {i}: {doc}")
    
    # Perform Bag of Words
    vocab, vectors, vectorizer = bag_of_words(documents)
    
    print(f"\nVocabulary ({len(vocab)} words):")
    print(f"  {list(vocab)}")
    
    print("\nDocument-Term Matrix:")
    print("  ", end="")
    for word in vocab:
        print(f"{word:>8}", end="")
    print()
    
    for i, vec in enumerate(vectors):
        print(f"Doc{i+1}:", end="")
        for count in vec:
            print(f"{count:>8}", end="")
        print()
```

### `Problem 11:` Write a Python program to add three given lists using Python map and lambda.


```python
# Three input lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

# Add corresponding elements using map and lambda
result = list(map(lambda x, y, z: x + y + z, list1, list2, list3))

print("List 1:", list1)
print("List 2:", list2)
print("List 3:", list3)
print("Result: ", result)

# # Alternative with variable arguments
# lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 1, 1]]
# result = list(map(lambda *all_lists: sum(all_lists), *lists))
# print(result)  
```

### `Problem-12:`Write a Python program to create a list containing the power of said number in bases raised to the corresponding number in the index using Python map.
`Input:`
```
list1 = [1,2,3,4,5,6]
```
`Output:`
```
[1,2,9,64,625,-]
```



```python
# list1 = [1,2,3,4,5,6]
# result = map(lambda x: x[1]**x[0], enumerate(list1) )

# print(list(result))

list1 = [1, 2, 3, 4, 5, 6]

result = list(map(lambda base, idx: base ** idx, list1, range(len(list1))))

print(result)
```

### `Problem-13` Using filter() and list() functions and .lower() method filter all the vowels in a given string.




```python
# Input string
text = "Hello World"

# Filter all vowels using filter() and list()
# Using .lower() to handle both uppercase and lowercase vowels
vowels = list(filter(lambda char: char.lower() in 'aeiou', text))

print(f"Original string: {text}")
print(f"Filtered vowels: {vowels}")

consonants = list(filter(lambda char: char.lower() not in 'aeiou', text))
print(consonants)  
```

`Problem-14`: Use reduce to convert a 2D list to 1D


```python
from functools import reduce

# 2D list (list of lists)
list_2d = [[1, 2, 3], [4, 5], [6, 7, 8], [9, 10]]

# Using reduce to flatten the list
list_1d = reduce(lambda x, y: x + y, list_2d)

print("2D List:", list_2d)
print("1D List:", list_1d)

# import itertools for large lists (more memory efficient)
# list_1d = list(itertools.chain.from_iterable(list_2d))
```

`Problem 15`- A dictionary contains following information about 5 employees:
- First name
- Last name
- Age
- Grade(Skilled,Semi-skilled,Highly skilled)<br>
Write a program using map/filter/reduce to a list of employees(first name + last name) who are highly skilled


```python
employees = [
    {
        'fname':'Nitish',
        'lname':'Singh',
        'age' : 33,
        'grade':'skilled'
    },
    {
        'fname':'Ankit',
        'lname':'Verma',
        'age' : 34,
        'grade':'semi-skilled'
    },
    {
        'fname':'Neha',
        'lname':'Singh',
        'age' : 35,
        'grade':'highly-skilled'
    },
    {
        'fname':'Anurag',
        'lname':'Kumar',
        'age' : 30,
        'grade':'skilled'
    },
    {
        'fname':'Abhinav',
        'lname':'Sharma',
        'age' : 37,
        'grade':'highly-skilled'
    }

]
```


```python
list(map(lambda x:x['fname'] + ' ' + x['lname'],list(filter(lambda x:True if x['grade'] == 'highly-skilled' else False,employees))))
```


```python
from functools import reduce

result_reduce = reduce(
    lambda acc, emp: acc + [f"{emp['fname']} {emp['lname']}"] 
                     if emp['grade'] == 'highly-skilled' 
                     else acc,
    employees,
    []
)
print("Using reduce:", result_reduce)
```


```python

```
