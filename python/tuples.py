#tuples are immutable sequences in Python, meaning once they are created, their elements cannot be changed. 
# They are defined using parentheses `()`.


my_tuple=(1, 2, 3, 4, 5)

print(my_tuple)# Output: (1, 2, 3, 4, 5)

print(my_tuple[0])  # Accessing the first element
print(my_tuple[-1])# Accessing the last element


#concatenating tuples
tuple=(1,2,3)
tuple2=(4,5,6)

conc_tuple=tuple+tuple2  # Concatenating tuples
print(conc_tuple)  # Output: (1, 2, 3, 4, 5, 6)

#repeating tuples
repeated_tuple=tuple*3  # Repeating the tuple three times           
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)