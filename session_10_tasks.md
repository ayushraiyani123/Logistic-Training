### `Q-1:` Write a function `get_final_line(filename)`, which takes filename as input and return final line of the file.

Note: You can choose any file of your choice.


```python
def get_final_line(filename):

    with open(filename, 'r') as file:
        lines = file.readlines()
        if lines:
            return lines[-1].strip()  # strip removes trailing newline
        else:
            return ""  # return empty string if file is empty


result = get_final_line("samplee.txt")
print(result)
```

### `Q-2:` Read through a text file, line by line. Use a dict to keep track of how many times each vowel (a, e, i, o, and u) appears in the file. Print the resulting tabulation -- dictionary.


```python
def count_vowels(filename):
   
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    with open(filename, 'r') as file:
        for line in file:
            for char in line.lower():
                if char in vowels:
                    vowels[char] += 1
    
    return vowels

filename = "samplee.txt"
result = count_vowels(filename)

print("Vowel counts:")
print(result)
```

### `Q-3:` Create a text file (using an editor, not necessarily Python) containing two tab separated columns, with each column containing a number. Then use Python to read through the file you’ve created. For each line, multiply each first number by the second and include it in the file in third column. In last add a line Total, by summing the value of third column



Input File example: That you need to create
```
1   2
3   4
5   6
7   8
9   10

```

Output File Example:
```
1   2   2
3   4   12
5   6   30
7   8   56
9   10  90
Total   190
```



```python
# Step 1: Create the input file (you'd normally do this in a text editor)
input_data = """1\t2
3\t4
5\t6
7\t8
9\t10"""

with open("input_numbers.txt", "w") as f:
    f.write(input_data)


# Step 2: Read input, multiply columns, add third column, and append Total
input_file = "input_numbers.txt"
output_file = "output_numbers.txt"

total = 0
output_lines = []

with open(input_file, "r") as f:
    for line in f:
        line = line.strip()
        if line:
            num1, num2 = line.split("\t")
            product = int(num1) * int(num2)
            total += product
            output_lines.append(f"{num1}\t{num2}\t{product}\n")

# Add the Total line at the end
output_lines.append(f"Total\t\t{total}\n")

with open(output_file, "w") as f:
    f.writelines(output_lines)

print("Done! Output file created.")
```

### `Q-4:` Create line wise reverse of a file
Write a function which takes two arguments: the names of the input file (to be read from) and the output file (which will be created).

For example, if a file looks like
 ```
abc def
ghi jkl
```
then the output file will be
```
fed cba
lkj ihg
```
**Notice**: The newline remains at the end of the string, while the rest of the characters are all reversed.


```python
def reverse_lines(input_file, output_file):
    
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Strip the trailing newline, reverse the string, then add newline back
            reversed_line = line.rstrip('\n')[::-1] + '\n'
            outfile.write(reversed_line)

reverse_lines("input.txt", "output.txt")
print("Done! Lines reversed successfully.")

```

### `Q-5:` Create a Serialized dict of frequency of words in the file. And from given list of words, using serialized dict show word count.

* List of word will be given



Given String

```
strings = """Alice was beginning to get very tired of sitting by her sister
            on the bank, and of having nothing to do:  once or twice she had
            peeped into the book her sister was reading, but it had no
            pictures or conversations in it, `and what is the use of a book,'
            thought Alice `without pictures or conversation?'

            So she was considering in her own mind (as well as she could,
            for the hot day made her feel very sleepy and stupid), whether
            the pleasure of making a daisy-chain would be worth the trouble
            of getting up and picking the daisies, when suddenly a White
            Rabbit with pink eyes ran close by her.

            There was nothing so VERY remarkable in that; nor did Alice
            think it so VERY much out of the way to hear the Rabbit say to
            itself, `Oh dear!  Oh dear!  I shall be late!'  (when she thought
            it over afterwards, it occurred to her that she ought to have
            wondered at this, but at the time it all seemed quite natural);
            but when the Rabbit actually TOOK A WATCH OUT OF ITS WAISTCOAT-
            POCKET, and looked at it, and then hurried on, Alice started to
            her feet, for it flashed across her mind that she had never
            before seen a rabbit with either a waistcoat-pocket, or a watch to
            take out of it, and burning with curiosity, she ran across the
            field after it, and fortunately was just in time to see it pop
            down a large rabbit-hole under the hedge."""

word_list = ['alice', 'wonder', 'natural']
```


```python
import pickle

# Given text
strings = """Alice was beginning to get very tired of sitting by her sister
            on the bank, and of having nothing to do:  once or twice she had
            peeped into the book her sister was reading, but it had no
            pictures or conversations in it, `and what is the use of a book,'
            thought Alice `without pictures or conversation?'

            So she was considering in her own mind (as well as she could,
            for the hot day made her feel very sleepy and stupid), whether
            the pleasure of making a daisy-chain would be worth the trouble
            of getting up and picking the daisies, when suddenly a White
            Rabbit with pink eyes ran close by her.

            There was nothing so VERY remarkable in that; nor did Alice
            think it so VERY much out of the way to hear the Rabbit say to
            itself, `Oh dear!  Oh dear!  I shall be late!'  (when she thought
            it over afterwards, it occurred to her that she ought to have
            wondered at this, but at the time it all seemed quite natural);
            but when the Rabbit actually TOOK A WATCH OUT OF ITS WAISTCOAT-
            POCKET, and looked at it, and then hurried on, Alice started to
            her feet, for it flashed across her mind that she had never
            before seen a rabbit with either a waistcoat-pocket, or a watch to
            take out of it, and burning with curiosity, she ran across the
            field after it, and fortunately was just in time to see it pop
            down a large rabbit-hole under the hedge."""

word_list = ['alice', 'wonder', 'natural']


# Step 1: Clean text and extract words 
text = strings.lower()

words = []
current_word = ""

for char in text:
    if char.isalpha() or char == '-':
        current_word += char
    else:
        if current_word:
            words.append(current_word)
            current_word = ""

# Don't forget the last word if text ends with a letter
if current_word:
    words.append(current_word)

# Build frequency dictionary
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1


# Step 2: Serialize the dictionary
with open('word_freq.pkl', 'wb') as f:
    pickle.dump(word_freq, f)

print("Dictionary serialized to 'word_freq.pkl'")


# Step 3: Deserialize and look up word counts
with open('word_freq.pkl', 'rb') as f:
    loaded_freq = pickle.load(f)

print("\nWord counts from serialized dictionary:")
print("-" * 40)
for word in word_list:
    count = loaded_freq.get(word, 0)
    print(f"  '{word}' -> {count}")
print("-" * 40)
```

### **`Q-6:`** Given a string calculate length of the string using recursion.

**Example 1:**

Input:
```bash
"abcd"
```

Output:

```bash
4
```

**Example 2:**

Input:
```bash
DataScience
```

Output:

```bash
11
```



```python
def string_length(s):
    
    # Base case: empty string
    if s == "":
        return 0
    else:
    # Recursive case: count 1 for current char + recurse on rest
        return 1 + string_length(s[1:])


# Test cases
print(string_length("abcd"))       
print(string_length("DataScience")) 
print(string_length(""))            
print(string_length("a"))           
```

### **`Q-7:`** Write a function that accepts two numbers and returns their greatest common divisior. Without using any loop

def gcd(int, int) => int

```
gcd(16,24) will give 8
```


```python
def gcd(x,y):
    # Base case: if b is 0, return a
    if y == 0:
        return x
    else:
    # Recursive case: gcd(a, b) = gcd(b, a % b)
        return gcd(y, x % y)


# Test cases
print(gcd(16, 24))   
print(gcd(48, 18))   
print(gcd(7, 13))    
print(gcd(100, 25)) 
print(gcd(0, 5))     
```

 ### `Q-8:` String Edit Distance

 Use your recursive function to write a program that reads two strings from the
user and displays the edit distance between them.

*The edit distance between two strings is a measure of their similarity—the smaller the edit distance, the more similar the strings are with regard to the minimum number of insert, delete and substitute operations needed to transform one string into the other.*

Consider the strings `kitten` and `sitting`. The first string can be transformed
into the second string with the following operations:
* Substitute the `k` with an `s`,
* substitute the `e` with an `i`,
* and insert a `g` at the end of the string.

This is the smallest number of operations that can be performed to transform kitten into sitting. As a result, the edit distance is `3`.


Write a recursive function that computes the edit distance between two strings.

Use the following algorithm:

```
Let s and t be the strings
    If the length of s is 0 then
        Return the length of t
    Else if the length of t is 0 then
        Return the length of s
    Else
        Set cost to 0
        If the last character in s does not equal the last character in t then
            Set cost to 1
        Set d1 equal to the edit distance between all characters except the last one in s, and all characters in t, plus 1
        Set d2 equal to the edit distance between all characters in s, and all characters except the last one in t, plus 1

        Set d3 equal to the edit distance between all characters except the last one in s, and all characters except the last one in t, plus cost
        Return the minimum of d1, d2 and d3
```






```python
def edit_distance(s, t):
    if len(s) == 0:
        return len(t)
    elif len(t) == 0:
        return len(s)
    else:
        cost = 0
        if s[-1] != t[-1]:
            cost = 1

        d1 = edit_distance(s[:-1], t) + 1

        d2 = edit_distance(s, t[:-1]) + 1

        d3 = edit_distance(s[:-1], t[:-1]) + cost

        return min(d1,d2,d3)

def main():

    s = input("Enter the first string:")
    t = input("Enter the second string:")

    distance = edit_distance(s, t)
    print(f"\nThe edit distance between '{s}' and '{t}' is {distance}.")

if __name__ == "__main__":
    main()
```

### `Q-9:` Run-Length Encoding

Run-length encoding is a simple data compression technique that can be effective when repeated values occur at adjacent positions within a list. Compression is achieved by replacing groups of repeated values with one copy of the value, followed by the number of times that the value should be repeated. For example, the list
```
["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B", "B", "A", "A", "A", "A", "A", "A", "B"]
```
would be compressed as `["A", 12, "B", 4, "A", 6, "B", 1]`.

Write a recursive function that implements the run-length compression technique
described above. Your function will take a list or a string as its only parameter. It should return the run-length compressed list as its only result. Include a main program that reads a string from the user, compresses it, and displays the run-length encoded result.


```python
def run_length_encode(data):
    if not data:
        return []
    first = data[0]
    count = 1
    while count<len(data) and data[count] == first:
        count += 1
    return [first, count] + run_length_encode(data[count:])

test_list = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B", "B", "A", "A", "A", "A", "A", "A", "B"]
print(run_length_encode(test_list))
```

### `Q-10:` Write a recursive function to convert a decimal to binary


```python
def decimal_to_binary(n):
# Handle negative numbers
    # if n < 0:
    #     return "-" + decimal_to_binary(-n)
    if n == 0:
        return "0"
    if n == 1:
        return "1"

    return decimal_to_binary(n//2) + str(n%2)

print(decimal_to_binary(10))
print(decimal_to_binary(112))
print(decimal_to_binary(18))
print(decimal_to_binary(220))
print(decimal_to_binary(27))
```


```python

```
