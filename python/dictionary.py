#in pyython a dictionary is a collection of key-value pairs
# dictionaries are unordered, mutable, and indexed collections.
# they are defined using curly braces `{}` or the `dict()` constructor.


my_dict = {'apple': 3, 'banana': 5, 'orange': 2}
print(my_dict['apple'])# Output: 3

#adding and removing elements from a dictionary
my_dict['grapes']=4
print(my_dict)  # Output: {'apple': 3, 'banana': 5, 'orange': 2, 'grapes': 4}

# Modifying values in a dictionary
my_dict['banana'] = 6  # Change value
print(my_dict)  # Output: {'apple': 3, 'banana': 6, 'orange': 2, 'grapes': 4}