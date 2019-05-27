def addFunc(x, y):
   return x + y

print(addFunc(5, 6))

#Lambda function
print((lambda x,y:x+y)(5,6))

#Lambda Fucntion can be assigned a name
addLambda = lambda x, y: x + y
print(addLambda(5, 6))

#Map Function
def double(x):
   return x*2
a = [1, 2, 3]
for mapElement in map(double, a): 
    print(mapElement) #[2, 4, 6]

#Alternatively using Lambda:
a = [1, 2, 3]
for mapElement in map((lambda x: x*2), a):
    print(mapElement)


#Can also apply a map to functions taking more than one argument;
#Then work with two or more lists
for mapElement in map((lambda x, y: x+y), [1,2,3], [4,5,6,7]):
    print(mapElement)   #[5,7,9]


#Filter Function
print(list(filter((lambda x: x%2==0), range(-4,4))))  #[-4, -2, 0, 2] 
# recall range doesn't include last value given in range    

from functools import reduce
#Reduce Function
print(reduce((lambda x, y: x+y), [0, 1, 2, 3, 4]))

#List Comprehensions
#Find list of integers and square them

a_list = [1, "4", 9, "a", 0, 4]
squared_ints = [ e**2 for e in a_list if isinstance(e,int)]
print(squared_ints)


#Using Map and filter too the above problem can be solved
filterdval=filter(lambda e: type(e) == int, a_list)
print(list(filterdval))

sqr_ints=list(map(lambda e: e**2, filterdval))
print(sqr_ints)


## Varargs support in Lambda

varArg = lambda *x: print(x)

varArg(1,"x","y",3,4)

kwArg = lambda **kwarg:print(kwarg)

kwArg(test="test",x=7,u=8)

