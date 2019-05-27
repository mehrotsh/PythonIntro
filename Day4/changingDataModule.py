# import moduleFoo

# moduleFoo.x=30     #Value gets changed in the module
# moduleFoo.y[0]=60
# print(moduleFoo._p)
# print(moduleFoo.y)
# moduleFoo.printVars()
# print(moduleFoo.__dundarVar__)

#https://www.python.org/dev/peps/pep-0008/#id36
# from moduleFoo import *
# x=30
# y[0]=60
# print(x)
# print(y)
# printVars()
# print(__dundarVar__) #name '__dundarVar__' is not defined
# print(_p)  # name '_p' is not defined


# from moduleFoo import functionA
# functionA()

# from moduleFoo import x,y,printVars
# x=70
# y[0]=80
# print(x)
# print(y)
# printVars()
# #print(_p)