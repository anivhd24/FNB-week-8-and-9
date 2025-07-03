#exaple of how to minipulate lists in Python

fruits=["apple", "banana", "cherry"]

print(fruits[0])  # Output: apple
fruits[1] = "blueberry"  # Change value
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']


#adding and removing elements from a list

fruits={"apple", "banana", "cherry"}

fruits.append("orange")  # Add an element to the end
print(fruits) # Output: ['apple', 'banana', 'cherry', 'orange']


fruits.insert(1, "kiwi")  # Insert an element at index 1
print(fruits)  # Output: ['apple', 'kiwi', 'banana', 'cherry', 'orange']

fruits.remove("banana")  # Remove an element by value
print(fruits)  # Output: ['apple', 'kiwi', 'cherry', 'orange']


#sorting items in a list 

fruits = ["banana", "apple", "cherry", "date"]
fruits.sort()  # Sort the list in ascending order
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']

# Reversing the order of items in a list
fruits.sort(reverse=True)  # Sort the list in descending order
print(fruits)  # Output: ['date', 'cherry', 'banana', ' apple']
