### `Q-1:` Rectangle Class
1. Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.

2. Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​​the rectangle.

3. Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.

Eg.
After making above classes and methods, on executing below code:-
```
my_rectangle = Rectangle(3 , 4)
my_rectangle.display()
```

`Output:`
```
The length of rectangle is:  3
The width of rectangle is:  4
The perimeter of rectangle is:  14
The area of rectangle is:  12
```



```python
class Rectangle:
    def __init__(self, length, width):
        """
        Initialize rectangle with length and width attributes.
        
        Args:
            length (float): The length of the rectangle
            width (float): The width of the rectangle
        """
        self.length = length
        self.width = width
    
    def Perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        
        Returns:
            float: The perimeter (2 * (length + width))
        """
        return 2 * (self.length + self.width)
    
    def Area(self):
        """
        Calculate the area of the rectangle.
        
        Returns:
            float: The area (length * width)
        """
        return self.length * self.width
    
    def display(self):
        """
        Display the length, width, perimeter, and area of the rectangle.
        """
        print(f"Rectangle Properties:")
        print(f"  Length:    {self.length}")
        print(f"  Width:     {self.width}")
        print(f"  Perimeter: {self.Perimeter()}")
        print(f"  Area:      {self.Area()}")


# Display usage:
if __name__ == "__main__":
    # Create a rectangle instance
    rect = Rectangle(3, 4)
    
    # Display its properties
    rect.display()
    
    # Access individual methods if needed
    print(f"\nIndividual calculations:")
    print(f"Perimeter: {rect.Perimeter()}")
    print(f"Area: {rect.Area()}")
```

## `Q-2: Bank Class`

1. Create a Python class called `BankAccount` which represents a bank account, having as attributes: `accountNumber` (numeric type), `name` (name of the account owner as string type), `balance`.
2. Create a constructor with parameters: `accountNumber, name, balance`.
3. Create a `Deposit()` method which manages the deposit actions.
4. Create a `Withdrawal()` method  which manages withdrawals actions.
5. Create an `bankFees()` method to apply the bank fees with a percentage of 5% of the balance account.
6. Create a `display()` method to display account details.
Give the complete code for the  BankAccount class.

Eg.
After making above classes and methods, on executing below code:-
```
newAccount = BankAccount(2178514584, "Mandy" , 2800)

newAccount.Withdrawal(700)

newAccount.Deposit(1000)

newAccount.display()
```

`Output:`
```
Account Number :  2178514584
Account Name :  Mandy
Account Balance :  3100 ₹
```


```python
class BankAccount:
    def __init__(self, accountNumber, name, balance):
        """
        Constructor to initialize bank account attributes.
        
        Args:
            accountNumber (int): The account number
            name (str): Name of the account owner
            balance (float): Initial account balance
        """
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
    
    def Deposit(self, amount):
        """
        Deposit money into the account.
        
        Args:
            amount (float): Amount to deposit
        """
        self.balance += amount
        self.bankFees()

        # self.bankFees()
    
    def Withdrawal(self, amount):
        """
        Withdraw money from the account if sufficient balance exists.
        
        Args:
            amount (float): Amount to withdraw
        """
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance for withdrawal!")
        # self.bankFees() # optional
    
    def bankFees(self):
        """
        Apply bank fees of 5% on the current balance.
        """
        fee = self.balance * 0.05
        # self.balance -= fee #optional
    
    def display(self):
        """
        Display account details.
        """
        print(f"Account Number :  {self.accountNumber}")
        print(f"Account Name :  {self.name}")
        print(f"Account Balance :  {self.balance} ₹")


# Example execution as per the question:
if __name__ == "__main__":
    newAccount = BankAccount(2178514584, "Mandy", 2800)
    
    newAccount.Withdrawal(700)   # Balance: 2800 - 700 = 2100 (This was before cutting fees)
    newAccount.Deposit(1000)     # Balance: 2100 + 1000 = 310 (This was before cutting fees)
    
    newAccount.display()
```

## `Q-3:Computation class`

1. Create a `Computation` class with a default constructor (without parameters) allowing to perform various calculations on integers numbers.
2. Create a method called `Factorial()` which allows to calculate the factorial of an integer n. Integer n as parameter for this method

3. Create a method called `naturalSum()` allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Integer n as parameter for this method.

4. Create a method called `testPrime()` in  the Calculation class to test the primality of a given integer n, n is Prime or Not? Integer n as parameter for this method.

5. Create  a method called `testPrims()` allowing to test if two numbers are prime between them. Two integers are prime to one another if they have only `1` as their common divisor. Eg. 4 and 9 are prime to each other.

5. Create a `tableMult()` method which creates and displays the multiplication table of a given integer. Then create an `allTablesMult()` method to display all the integer multiplication tables 1, 2, 3, ..., 9.

6. Create a static `listDiv()` method that gets all the divisors of a given integer on new list called  Ldiv. Create another `listDivPrim()` method that gets all the prime divisors of a given integer.


```python
import math

class Computation:
    def __init__(self):
        """Default constructor without parameters"""
        pass
    
    def Factorial(self, n):
        """
        Calculate factorial of n (n!)
        """
        if n < 0:
            return None
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    
    def naturalSum(self, n):
        """
        Calculate sum of first n integers: 1 + 2 + 3 + ... + n
        """
        return n * (n + 1) // 2
    
    def testPrime(self, n):
        """
        Test if n is a prime number
        Returns True if prime, False otherwise
        """
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    def testPrims(self, a, b):
        """
        Test if two numbers are prime to each other (coprime)
        They have only 1 as common divisor
        """
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        
        return gcd(a, b) == 1
    
    def tableMult(self, n):
        """
        Display multiplication table of given integer n
        """
        print(f"\nMultiplication Table of {n}:")
        for i in range(1, 11):
            print(f"{n} x {i} = {n * i}")
    
    def allTablesMult(self):
        """
        Display all multiplication tables from 1 to 9
        """
        for i in range(1, 10):
            self.tableMult(i)
    
    @staticmethod
    def listDiv(n):
        """
        Get all divisors of a given integer n
        Returns list Ldiv containing all divisors
        """
        Ldiv = []
        for i in range(1, n + 1):
            if n % i == 0:
                Ldiv.append(i)
        return Ldiv
    
    def listDivPrim(self, n):
        """
        Get all prime divisors of a given integer n
        """
        Ldiv = self.listDiv(n)
        LdivPrim = []
        for divisor in Ldiv:
            if self.testPrime(divisor):
                LdivPrim.append(divisor)
        return LdivPrim


# ============== DEMONSTRATION ==============

if __name__ == "__main__":
    calc = Computation()
    
    # Test Factorial
    print("=" * 40)
    print("Factorial of 5:", calc.Factorial(5))  # 120
    
    # Test naturalSum
    print("=" * 40)
    print("Sum of first 10 integers:", calc.naturalSum(10))  # 55
    
    # Test testPrime
    print("=" * 40)
    print("Is 17 prime?", calc.testPrime(17))  # True
    print("Is 20 prime?", calc.testPrime(20))  # False
    
    # Test testPrims (coprime)
    print("=" * 40)
    print("Are 4 and 9 prime to each other?", calc.testPrims(4, 9))  # True
    print("Are 6 and 9 prime to each other?", calc.testPrims(6, 9))  # False
    
    # Test tableMult
    print("=" * 40)
    calc.tableMult(5)
    
    # Test allTablesMult
    print("=" * 40)
    calc.allTablesMult()
    
    # Test listDiv (static method)
    print("=" * 40)
    print("All divisors of 24:", Computation.listDiv(24))  # [1, 2, 3, 4, 6, 8, 12, 24]
    
    # Test listDivPrim
    print("=" * 40)
    print("Prime divisors of 24:", calc.listDivPrim(24))  # [2, 3]
    print("Prime divisors of 30:", calc.listDivPrim(30))  # [2, 3, 5]
```

## `Q-4`: Build flashcard using class in Python.

Build a flashcard using class in python. A flashcard is a card having information on both sides, which can be used as an aid in memoization. Flashcards usually have a question on one side and an answer on the other.

**Example 1:**

Approach:

- Create a class named FlashCard.
- Initialize dictionary fruits using __init__() method. Here you have to define fruit name as key and it's color as value. E.g., {"Banana": "yellow", "Strawberries": "pink"}
- Now randomly choose a pair from fruits by using _random_ module and store the key in variable _fruit_ and _value_ in variable color.
- Now prompt the user to answer the color of the randomly chosen fruit.
- If correct print correct else print wrong.

Output:
```bash
welcome to fruit quiz
What is the color of Strawberries
pink
Correct answer
Enter 0, if you want to play again: 0
What is the color of watermelon
green
Correct answer
Enter 0, if you want to play again: 1
```


```python
import random

class FlashCard:
    def __init__(self):
        """
        Initialize the flashcard with a dictionary of fruits and their colors.
        """
        self.fruits = {
            "Banana": "yellow",
            "Strawberries": "pink",
            "Apple": "red",
            "Orange": "orange",
            "Grapes": "purple",
            "Watermelon": "green",
            "Blueberry": "blue",
            "Mango": "yellow",
            "Kiwi": "brown",
            "Lemon": "yellow"
        }
    
    def quiz(self):
        """
        Start the flashcard quiz game.
        Randomly selects a fruit and asks user for its color.
        """
        print("welcome to fruit quiz")
        
        while True:
            # Randomly choose a fruit-color pair
            fruit, color = random.choice(list(self.fruits.items()))
            
            # Ask user for the color
            user_answer = input(f"What is the color of {fruit}\n").strip().lower()
            
            # Check if answer is correct
            if user_answer == color.lower():
                print("Correct answer")
            else:
                print(f"Wrong answer. The correct color is {color}")
            
            # Ask if user wants to play again
            play_again = input("Enter 0, if you want to play again: ")
            
            if play_again != "0":
                break
        
        print("Thanks for playing!")


# ============== MAIN EXECUTION ==============

if __name__ == "__main__":
    # Create flashcard object
    fc = FlashCard()
    
    # Start the quiz
    fc.quiz()
```

## `Q-5:` Problem 5 based on OOP Python.

TechWorld, a technology training center, wants to allocate courses for instructors. An instructor is identified by name, technology skills, experience and average feedback. An instructor is allocated a course, if he/she satisfies the below two conditions:
- eligibility criteria:
    - if experience is more than 3 years, average feedback should be 4.5 or more
    - if experience is 3 years or less, average feedback should be 4 or more
- he/she should posses the technology skill for the course

Identify the class name and attributes to represent instructors. Write a Python program to implement the class chosen with its attributes and methods.

**Note:**
- Consider all instance variables to be private and methods to be public.
- An instructor may have multiple technology skills, so consider instance variable, technology_skill to be a list.
- *check_eligibility()*: Return true if eligibility criteria is satisfied by the instructor. Else, return false
- *allocate_course(technology)*: Return true if the course which requires the given technology can be allocated to the instructor. Else, return false.

Represent a few objects of the class, initialize instance variables using setter methods, invoke
appropriate methods and test your program.


```python
class Instructor:
    def __init__(self):
        """
        Private instance variables (encapsulation)
        """
        self.__name = None
        self.__technology_skills = []  # List of skills
        self.__experience = 0          # Years of experience
        self.__average_feedback = 0.0  # Average feedback score
    
    # ============ SETTER METHODS ============
    
    def set_name(self, name):
        """Set instructor name"""
        self.__name = name
    
    def set_technology_skills(self, skills):
        """
        Set technology skills (accepts list or single skill)
        """
        if isinstance(skills, list):
            self.__technology_skills = skills
        else:
            self.__technology_skills = [skills]
    
    def set_experience(self, experience):
        """Set years of experience"""
        self.__experience = experience
    
    def set_average_feedback(self, feedback):
        """Set average feedback score"""
        self.__average_feedback = feedback
    
    # ============ GETTER METHODS (optional but useful) ============
    
    def get_name(self):
        return self.__name
    
    def get_technology_skills(self):
        return self.__technology_skills
    
    def get_experience(self):
        return self.__experience
    
    def get_average_feedback(self):
        return self.__average_feedback
    
    # ============ BUSINESS LOGIC METHODS ============
    
    def check_eligibility(self):
        """
        Check if instructor meets eligibility criteria:
        - Exp > 3 years: feedback >= 4.5
        - Exp <= 3 years: feedback >= 4.0
        """
        if self.__experience > 3:
            return self.__average_feedback >= 4.5
        else:
            return self.__average_feedback >= 4.0
    
    def allocate_course(self, technology):
        """
        Check if course can be allocated:
        1. Must satisfy eligibility criteria
        2. Must possess the required technology skill
        """
        # First check eligibility
        if not self.check_eligibility():
            return False
        
        # Then check if instructor has the required skill
        return technology in self.__technology_skills
    
    def display_details(self):
        """Display instructor information"""
        print(f"\nInstructor Name: {self.__name}")
        print(f"Technology Skills: {', '.join(self.__technology_skills)}")
        print(f"Experience: {self.__experience} years")
        print(f"Average Feedback: {self.__average_feedback}")


# ============== TESTING THE PROGRAM ==============

if __name__ == "__main__":
    
    print("=" * 50)
    print("TechWorld Instructor Allocation System")
    print("=" * 50)
    
    # ========== Create Instructor 1: Eligible, has skill ==========
    print("\n--- Creating Instructor 1: John ---")
    instructor1 = Instructor()
    instructor1.set_name("John Smith")
    instructor1.set_technology_skills(["Python", "Java", "Data Science"])
    instructor1.set_experience(5)
    instructor1.set_average_feedback(4.7)
    
    instructor1.display_details()
    print(f"Eligible? {instructor1.check_eligibility()}")
    
    # Try to allocate Python course
    tech = "Python"
    result = instructor1.allocate_course(tech)
    print(f"Can allocate '{tech}' course? {result}")
    
    # Try to allocate C++ course (skill not possessed)
    tech = "C++"
    result = instructor1.allocate_course(tech)
    print(f"Can allocate '{tech}' course? {result}")
    
    # ========== Create Instructor 2: Not eligible (low feedback) ==========
    print("\n--- Creating Instructor 2: Alice ---")
    instructor2 = Instructor()
    instructor2.set_name("Alice Johnson")
    instructor2.set_technology_skills(["Python", "Machine Learning"])
    instructor2.set_experience(2)
    instructor2.set_average_feedback(3.8)  # Less than 4.0
    
    instructor2.display_details()
    print(f"Eligible? {instructor2.check_eligibility()}")
    
    tech = "Python"
    result = instructor2.allocate_course(tech)
    print(f"Can allocate '{tech}' course? {result}")
    
    # ========== Create Instructor 3: Eligible with 3 years exp ==========
    print("\n--- Creating Instructor 3: Bob ---")
    instructor3 = Instructor()
    instructor3.set_name("Bob Williams")
    instructor3.set_technology_skills(["JavaScript", "React", "Node.js"])
    instructor3.set_experience(3)  # Exactly 3 years
    instructor3.set_average_feedback(4.2)  # Above 4.0
    
    instructor3.display_details()
    print(f"Eligible? {instructor3.check_eligibility()}")
    
    tech = "React"
    result = instructor3.allocate_course(tech)
    print(f"Can allocate '{tech}' course? {result}")
    
    # ========== Create Instructor 4: High exp but low feedback ==========
    print("\n--- Creating Instructor 4: Carol ---")
    instructor4 = Instructor()
    instructor4.set_name("Carol Davis")
    instructor4.set_technology_skills(["Python", "Django"])
    instructor4.set_experience(6)  # More than 3 years
    instructor4.set_average_feedback(4.3)  # Less than 4.5
    
    instructor4.display_details()
    print(f"Eligible? {instructor4.check_eligibility()}")
    
    tech = "Python"
    result = instructor4.allocate_course(tech)
    print(f"Can allocate '{tech}' course? {result}")
    
    print("\n" + "=" * 50)
    print("Testing Complete!")
    print("=" * 50)
```

### Better Understanding of method reusability


```python
class Instructor:
    def __init__(self):
        """
        Private instance variables (encapsulation)
        """
        self.__name = None
        self.__technology_skills = []  
        self.__experience = 0          
        self.__average_feedback = 0.0  
    
    # ============ SPACING FUNCTION ============
    
    def print_separator(self, char="=", length=50):
        """
        Reusable function to print separator lines
        Makes output more readable and organized
        """
        print(char * length)
    
    def print_blank_line(self, count=1):
        """
        Reusable function to print blank lines
        """
        print("\n" * (count - 1)) if count > 1 else print()
    
    # ============ SETTER METHODS ============
    
    def set_name(self, name):
        self.__name = name
    
    def set_technology_skills(self, skills):
        if isinstance(skills, list):
            self.__technology_skills = skills
        else:
            self.__technology_skills = [skills]
    
    def set_experience(self, experience):
        self.__experience = experience
    
    def set_average_feedback(self, feedback):
        self.__average_feedback = feedback
    
    # ============ GETTER METHODS ============
    
    def get_name(self):
        return self.__name
    
    def get_technology_skills(self):
        return self.__technology_skills
    
    def get_experience(self):
        return self.__experience
    
    def get_average_feedback(self):
        return self.__average_feedback
    
    # ============ BUSINESS LOGIC METHODS ============
    
    def check_eligibility(self):
        """
        Check if instructor meets eligibility criteria
        """
        if self.__experience > 3:
            return self.__average_feedback >= 4.5
        else:
            return self.__average_feedback >= 4.0
    
    def allocate_course(self, technology):
        """
        Check if course can be allocated
        """
        if not self.check_eligibility():
            return False
        return technology in self.__technology_skills
    
    # ============ DISPLAY METHOD USING SPACING FUNCTION ============
    
    def display_details(self):
        """Display instructor information with proper spacing"""
        self.print_blank_line()  # Add blank line before
        print(f"Instructor Name: {self.__name}")
        print(f"Technology Skills: {', '.join(self.__technology_skills)}")
        print(f"Experience: {self.__experience} years")
        print(f"Average Feedback: {self.__average_feedback}")
        self.print_blank_line()  # Add blank line after


# ============== TESTING WITH SPACING FUNCTIONS ==============

if __name__ == "__main__":
    
    # Create instructor
    instructor = Instructor()
    instructor.set_name("John Smith")
    instructor.set_technology_skills(["Python", "Java", "Data Science"])
    instructor.set_experience(5)
    instructor.set_average_feedback(4.7)
    
    # ========== DEMONSTRATING SPACING FUNCTIONS ==========
    
    # Header with separator
    instructor.print_separator("=", 50)
    print("TechWorld Instructor Allocation System")
    instructor.print_separator("=", 50)
    
    instructor.print_blank_line(2)  # Two blank lines
    
    # Section separator
    instructor.print_separator("-", 30)
    print("INSTRUCTOR DETAILS")
    instructor.print_separator("-", 30)
    
    instructor.display_details()
    
    # Another section
    instructor.print_separator("-", 30)
    print("COURSE ALLOCATION RESULTS")
    instructor.print_separator("-", 30)
    
    # Test allocations
    courses = ["Python", "C++", "Machine Learning"]
    for course in courses:
        result = instructor.allocate_course(course)
        status = "✓ ALLOCATED" if result else "✗ NOT ALLOCATED"
        print(f"{course:20} {status}")
    
    instructor.print_blank_line()
    instructor.print_separator("=", 50)
    print("END OF REPORT")
    instructor.print_separator("=", 50)
```


```python

```
