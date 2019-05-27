print("moduleFoo's  __name__ = %s" % __name__)
print("before import")
import math

#__all__ = ['x', '_p']       # __all__ has precedence while using from ..import *
x=20
y=[1,2,3]
_p="private"
__dundarVar__="systemVar"

def printVars():
    print("x is :"+str(x))
    print("y is :"+str(y))
    print("_p is :"+_p)


print("before functionA")


def functionA():
    print("Function A")


print("before functionB")


def functionB():
    print("Function B {}".format(math.sqrt(100)))


print("before __name__ guard")
if __name__ == "__main__":
    print("moduleFoo is being run directly")
    functionA()
    functionB()
else:
    print("module is being imported")
print("after __name__ guard")
