#A set in python is an unordered collection of unique elements.
# Sets are mutable, meaning you can add or remove elements after creation, but they do not allow duplicate values.
# Sets are defined using curly braces `{}` or the `set()` constructor.

my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Adding elements to a set

my_set.add(6)  # Add a single element
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

#removing elements from a set
my_set.remove(3)  # Remove a specific element   
print(my_set)  # Output: {1, 2, 4, 5, 6}


#opperations on sets

set1= {1, 2, 3}
set2 = {3, 4, 5}

# Union of two sets
union_set = set1.union(set2)  # or set1 | set2  
print(union_set)  # Output: {1, 2, 3, 4, 5} removes duplicates

# Intersection of two sets
intersection_set = set1.intersection(set2)  # or set1 & set2
print(intersection_set)  # Output: {3} common elements

# Difference of two sets
difference_set = set1.difference(set2)  # or set1 - set2
print(difference_set)  # Output: {1, 2} elements in set1 but not in set2


#sets are useful for membership testing, removing duplicates from a list, and performing mathematical set operations like union, intersection, and difference.
