import builtins

print(dir(builtins))


a = 5  # global
def func(b):
   """
   Test function
   """
   global c
   a=10
   c = a + b
   return c
print(func(4))        # gives 4+5=9
print (c)              # not defined
print(a)

help(func)