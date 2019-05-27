
#Avoid assigning variable to functions which do not return any value
a = [0, 1, 2]
b = a.append(3)
print(b)

#Block keywords you already know are "if", "for", and "while".
#Functions in python are defined using the block keyword "def", followed with the function's name as the block's name. 
#the block head is of the following format: block_keyword block_name(argument1,argument2, ...) 


def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)
print("The sum of two numbers are %d " % x)


# Multiple return values
def onetwothree(x):
  return x*1, x*2, x*3

print(onetwothree(3))

# Default arguments

def print_error(lineno, message="error"):
   print("%s at line %d" % (message, lineno))

print_error(42)

print_error(44,"WARN")

print_error( message="Testing",lineno=66)

#print_error()  #Error : missing 1 required positional argument

#Variable arguments
def sum(*args):
    result = 0
    for arg in args:
        result += arg
    return result

print(sum(1,2,3) ) #6

#Keyworded arguments
def print_hello(firstname="", lastname=""):
    print("Hello, %s %s" % (firstname, lastname))
    
print_hello(lastname="Sherrill",firstname="David")

print_hello("David","Sherrill")

#Using Both Args and Kwargs in a Function

def func(*args,**kwargs):
  for arg in args:
    print(arg)
  for item in kwargs.items():
    print(item)

func(1,x=7,u=8)

# Another way to use args and kwargs in a function

def myFun(arg0,arg1, arg2, arg3): 
    print("arg0:",arg0)
    print("arg1:", arg1) 
    print("arg2:", arg2) 
    print("arg3:", arg3) 
      
# Now we can use *args or **kwargs to 
# pass arguments to this function :  
args = ("Testing", "Fucntions", "Arguments") 
myFun("test",*args) 
  
kwargs = {"arg1" : "Testing", "arg2" : "Fucntions", "arg3" : "Arguments"} 
myFun("test",**kwargs) 

