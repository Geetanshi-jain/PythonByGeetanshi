"""Exception handling in Python lets you manage errors gracefully so your program doesn’t crash unexpectedly.

"""
"""
try:
    # Code that might raise an exception
except SomeException:
    # Code that runs if exception occurs
else:
    # Runs if no exception occurs
finally:
    # Runs no matter what (optional)
"""

try:
    a = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

#Example 2: Catching Multiple Exceptions
try:
    x = int("abc")
except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    print("Cannot divide by zero")

#✅ Example 3: Using else
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("That's not a number!")
else:
    print("You entered:", x)

# Example 4: Using finally
try:
    f = open("myfile.txt", "r")
    data = f.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("Closing file...")
    f.close()

#Generic Exception
try:
    # risky code
    1 / 0
except Exception as e:
    print("Error:", e)

#Raising Custom Exceptions
def divide(a, b):
    if b == 0:
        raise ValueError("Denominator can't be zero")
    return a / b

try:
    print(divide(5, 0))
except ValueError as e:
    print("Caught error:", e)
"""
ExceptionName	                           Description
ZeroDivisionError	                       Divide by zero
ValueError	                               Wrong value type
TypeError	                               Wrong data type
IndexError	                               Index out of range
KeyError	                               Missing dictionary key
FileNotFoundError	                       File does not exist
ImportError	                               Import fails
"""