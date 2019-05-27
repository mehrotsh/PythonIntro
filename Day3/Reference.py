
def f1(x,y):
    x = x * 1
    y = y * 2
    print(x, y)   # 0 [1, 2, 1, 2]
    
def f2(x,y):
    x = x * 1
    y[0] = y[0] * 2
    print(x, y)   # 0 [2, 2]
    
a = 0
b = [1,2]
f1(a,b)
print(a, b)  # 0 [1, 2]
f2(a,b)
print(a, b)  # 0 [2, 2]
