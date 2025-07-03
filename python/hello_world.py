
print("hello world")

#strings -----------------------------------------------------------------------------------------------------------------

message='hello world'

print(message)


#advanced concepts in stings ------------------------------------------------------------------------------------------------

message='  Hello,World  '

print(message[0]) #first character
print(message[1])# second character
print(len(message))#length of the string 
print(message.strip())  # removes leading and trailing whitespace
print(message.lower())  # converts to lowercase
print(message.split(','))  # splits the string into a list
print(message.replace('Hello', 'Hi'))  # replaces a substring
print(message.upper())  # converts to uppercase


#numeric data -------------------------------------------------------------------------------------------------------------

num=3

print(type(num))  # prints the type of num

num2=3.14
print(type(num2))  # prints the type of num2


#variables -----------------------------------------------------------------------------------------------------------------------

my_variable=10 # variable names can contain letters, numbers, and underscores, but cannot start with a number
total_count=0 # variable names are case-sensitive, so 'total_count' and 'Total_Count' are different variables
user='John Doe'# variable names should be descriptive and meaningful



#opperators --------------------------------------------------------------------------------------------------------------

#addition(+) subtraction(-) multiplication(*) division(/) modulus(%) exponentiation(**) 

x=10
y=2

print(x + y)  # addition
print(x - y)  # subtraction
print(x * y)  # multiplication
print(x / y)  # division
print(x % y)  # modulus
print(x ** y)  # exponentiation


#opperators with strings ------------------------------------------------------------------------------------------------

str1='Hello'
str2='World'

print(str1 + ' ' + str2)  # concatenation
print(str1 * 3)  # repetition


#control statements ------------------------------------------------------------------------------------------------------

# if, elif, else statements
num=-20
if num>0:
    print("The number is positive")
elif num<0:
    print("The number is negative")
    
num2=40
if num2>0:
    print("The number is positive")
elif num2==0:
    print("The number is zero")
else:
    print("The number is negative")   
    
    


num5=int(input("Enter a number: "))
num6=int(input("Enter another number: "))
if num5 > num6:
    print("{num5} is greater than {num6}")
elif num5 < num6:
    print("{num5} is less than {num6}")
else:
    print("{num5} is equal to {num6}")
    
    
    
    
#loops -------------------------------------------------------------------------------------------------------------


# for loop

fruits=["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    
    numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
    
    
 # while loop
count = 0
while count <=5:
    print(count)
    count += 1  # increment the count by 1 each iteration
    
    
    
#loop control statements --------------------------------------------------------------------------------------------

# break statement

fruits=["apple", "banana", "cherry", "date"]
for fruit in fruits:
    if fruit == "cherry":
        break  # exit the loop when banana is found
    print(fruit)
    
# continue statement
print()
for fruit in fruits:
    if fruit == "cherry":
        continue  # skip the iteration when banana is found
    print(fruit)
    
# pass statement
print()
for fruit in fruits:
    if fruit == "cherry":
        pass  # do nothing, just continue the loop
    print(fruit)
    
#while loop with break statement
count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:
        break  # exit the loop when count is 3