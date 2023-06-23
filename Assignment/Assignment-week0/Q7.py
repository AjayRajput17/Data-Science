"""
Q7. What do you understand about mutable and immutable data types? Give examples for both showing
this property.
"""
     # mutable data types

# list
my_list = [1, 2, 3]
print("original list",my_list)
my_list.append(4)
my_list[0] = 5
print("modified list",my_list)


          # immutable

# String

str = "Ajay Rajput"
try:
   str1 =  str[0] = "V"
except Exception as e :
    print("You Cannot modify a string because string is immutable data type")
