#Relational Operators
x = 2
print(x == 2) # prints out True
print(x!=2) #prints out False
print(x == 3) # prints out False
print(x < 3) # prints out True

#Boolean operators
# The "and" and "or" boolean operators allow building complex boolean 
# expressions

name = "John"
age = 24
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")


# The 'not' operator
# This syntax is not permitted   print(!False)
print(not False) # Prints out True
print((not False) == (False)) # Prints out False


#The "in" operator could be used to check if a specified object exists
# within an iterable object container

name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")
    

#If operator

x = 2
if x == 2:
    print("x equals two!")
elif x==3:
    print("x equals three!")   
else:
    print("x does not equal to two.")    

'''
A statement is evaulated as true if one of the following is correct: 
1. The "True" boolean variable is given, or calculated using an expression,
    such as an arithmetic comparison. 
2. An object which is not considered "empty" is passed.

Here are some examples for objects which are considered as empty: 
1. An empty string: "" 
2. An empty list: [] 
3. The number zero: 0 
4. The false boolean variable: False
'''    

#is operator : The operators "is" and "is not" test for object identity:
#  x is y is true if and only if x and y are the same object
# that can be if they have same memory location.

x = 'a'
x += 'bc'
y = 'abc'
z = y
w= 'abc'

print("x is y ", (x is y))  #False
print("z is y ", (z is y))  #True
print("w is y", (w is y))   #True
print("the id of x is", str(id(x)))
print("the id of x is", str(id(y)))
print("the id of x is", str(id(w)))

# For more read https://stackoverflow.com/questions/13650293/understanding-pythons-is-operator


   