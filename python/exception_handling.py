#exception handling is a way to handle errors gracefully in your code.
# It allows you to catch and respond to errors without crashing the program.    
#try:code that might raise an exception
#except:code that runs if an exception occurs
#finally:code that runs no matter what, even if an exception occurs

try:
    print(x)
  
except NameError:
    print("Variable x is not defined")
else:
    print("everything went wrong")        


x=-1

if x < 0:
    raise ecxeption("no numbers below zero allowed")