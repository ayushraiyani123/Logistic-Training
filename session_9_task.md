### `Problem-1:` Class inheritence

Create a **Bus** child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

Note: The bus seating capacity is 50. so the final fare amount should be 5500. You need to override the fare() method of a Vehicle class in Bus class.


```python
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def __init__(self, name, mileage, capacity):
        super().__init__(name, mileage, capacity)

    def fare(self):
        base_fare = self.capacity * 100
        maintenance_charge = base_fare * 0.10
        return base_fare + maintenance_charge

cap = Bus("Lions", 22,50)
print("Total fare is:",cap.fare())
```

### `Problem-2:` Class Inheritence

Create a Bus class that inherits from the Vehicle class. Give the capacity argument of *Bus.seating_capacity()* a default value of 50.

Use the following code for your parent Vehicle class.


```python
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def __init__(self, name, mileage, capacity):
        super().__init__(name, mileage, capacity)

    def seating_capacity():
        return 50
        
    def fare(self):
        base_fare = self.capacity * 100
        maintenance_charge = base_fare * 0.10
        return base_fare + maintenance_charge
        
default=Bus.seating_capacity()
cap = Bus("Lions",22,default)
print("Total fare is:",cap.fare())
```

### `Problem-3:` Write a program that has a class Point. Define another class Location which has two objects (Location & Destination) of class Point. Also define a function in Location that prints the reflection of Destination on the x axis.


```python
class Point:
    
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def display(self):
        return f"({self.x},{self.y})"

class Location:
    def __init__(self,loc,destination):
        self.loc = loc
        self.dest = destination

    def print_reflaction(self):
        reflected = Point(self.dest.x, self.loc.y)
        print(f"Original Destination: {self.dest.display()}")
        print(f"Reflection on x-axis: {reflected.display()}")

loc_point = Point(3, 4)      
dest_point = Point(5, -2) 

# my_loc = Location(loc_point, dest_point)

my_loc=Location(loc_point,dest_point)
my_loc.print_reflaction()
    
```

### `Problem-4:` Write a program that has an abstract class Polygon. Derive two classes Rectangle and Triamgle from Polygon and write methods to get the details of their dimensions and hence calculate the area.


```python
class Polygon:
    def __init__(
```


```python
class Polygon:
    # base class
    def get_dims(self):
        pass
    
    def area(self):
        pass


class Rectangle(Polygon):
    def __init__(self):
        self.l = 0
        self.w = 0
    
    def get_dims(self):
        self.l = float(input("Enter length: "))
        self.w = float(input("Enter width: "))
    
    def area(self):
        return self.l * self.w


class Triangle(Polygon):
    def __init__(self):
        self.base = 0
        self.h = 0
    
    def get_dims(self):
        self.base = float(input("Enter base: "))
        self.h = float(input("Enter height: "))
    
    def area(self):
        return 0.5 * self.base * self.h


# main
print("Rectangle:")
r = Rectangle()
r.get_dims()
print(f"Area = {r.area()}")

print("\nTriangle:")
t = Triangle()
t.get_dims()
print(f"Area = {t.area()}")
```

### `Problem-5:` Write a program with class Bill. The users have the option to pay the bill either by cheque or by cash. Use the inheritance to model this situation.


```python
class Bill:
    def __init__(self, bill_no, customer, amount):
        self.bill_no = bill_no
        self.customer = customer
        self.amount = amount
        self.paid = False
    
    def show(self):
        print(f"\nBill No: {self.bill_no}")
        print(f"Customer: {self.customer}")
        print(f"Amount: ${self.amount}")
        status = "Paid" if self.paid else "Pending"
        print(f"Status: {status}")


class Payment:
    # base class for all payment types
    def __init__(self, bill):
        self.bill = bill
    
    def pay(self):
        self.bill.paid = True
        print("\nPayment successful!")


class Cash(Payment):
    def __init__(self, bill, cash_given):
        super().__init__(bill)
        self.cash_given = cash_given
    
    def pay(self):
        if self.cash_given < self.bill.amount:
            print("Not enough cash!")
            return
        
        change = self.cash_given - self.bill.amount
        super().pay()
        print(f"Cash received: ${self.cash_given}")
        print(f"Change returned: ${change}")


class Cheque(Payment):
    def __init__(self, bill, cheque_no, bank):
        super().__init__(bill)
        self.cheque_no = cheque_no
        self.bank = bank
    
    def pay(self):
        super().pay()
        print(f"Cheque no: {self.cheque_no}")
        print(f"Bank: {self.bank}")


# main program
bill = Bill("B001", "Alice", 500)
bill.show()

print("\n--- Pay by Cash ---")
cash_pay = Cash(bill, 600)
cash_pay.pay()
bill.show()

# new bill for cheque demo
bill2 = Bill("B002", "Bob", 1200)
print("\n--- Pay by Cheque ---")
cheque_pay = Cheque(bill2, "CHK123", "SBI")
cheque_pay.pay()
bill2.show()
```

### `Q-6:` FlexibleDict
As of now we are accessing values from dictionary with exact keys. Now we want to amend accessing values functionality. if a dict have key `1` (int) the even if we try to access values by giving `'1'` (1 as str) as key, we should get the same result and vice versa.

Write a class `FlexibleDict` upon builtin `dict` class with above required functionality.

Hint- `dict[key] => dict.__getitem__(key)`

Ex.
```
fd = FlexibleDict()
fd['a'] = 100
print(fd['a']) # Like regular dict

fd[5] = 500
print(fd[5]) # Like regular dict

fd[1] = 100
print(fd['1']) # actual Key is int but still trying to access through str key.
fd['1'] = 100
print(fd[1])

```
`Output:`
```
100
500
100
100

```


```python
class FlexibleDict(dict):
    def __getitem__(self, key):
        # try the key as-is first
        try:
            return super().__getitem__(key)
        except KeyError:
            pass
        
        # try converting int to str or str to int
        if isinstance(key, int):
            alt_key = str(key)
        elif isinstance(key, str):
            try:
                alt_key = int(key)
            except ValueError:
                raise KeyError(key)
        else:
            raise KeyError(key)
        
        return super().__getitem__(alt_key)
    
    def __setitem__(self, key, value):
        # if key already exists as other type, overwrite it
        if isinstance(key, int):
            alt_key = str(key)
            if alt_key in self:
                super().__delitem__(alt_key)
        elif isinstance(key, str):
            try:
                alt_key = int(key)
                if alt_key in self:
                    super().__delitem__(alt_key)
            except ValueError:
                pass
        
        super().__setitem__(key, value)


# testing
fd = FlexibleDict()
fd['a'] = 100
print(fd['a'])  # Like regular dict

fd[5] = 500
print(fd[5])    # Like regular dict

fd[1] = 100
print(fd['1'])  # actual key is int but accessing through str

fd['1'] = 100
print(fd[1])    # actual key is str but accessing through int
```


```python

```


```python

```
