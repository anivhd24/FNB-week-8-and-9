#functions are a fundamental part of Python programming, allowing you to encapsulate code for reuse and organization.
# They can take parameters, return values, and help in structuring your code effectively.
#using the `def` keyword to define a function, followed by the function name and parentheses.

'''
def greet(name):
    print(f"Hello, {name}!")
    
greet("Alice")  # Output: Hello, Alice!    

def add(a, b):
    return a + b

result=add(2,5)
print(result)  # Output: 7 
'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")
    
    greet("Bob","Good Morning")  # Output: Good Morning, Bob