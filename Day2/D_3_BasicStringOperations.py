
astr="Hello World!"

#Length
print("The length of String is %s " % len(astr))

#Index

print("The index ", astr.index("o"))

#Count

print("The count is ", astr.count("l"))

#Slice Operator

print("word from index 3 to 6", astr[0:20])

print("printing word from beginning to second last char",astr[:-1])

''' Note ::
This prints a slice of the string, starting at index 3, and ending at index 6. 
But why 6 and not 7? Again, most programming languages do this - it makes doing math inside 
those brackets easier.

If you just have one number in the brackets, it will give you the single character at that index.
If you leave out the first number but keep the colon, it will give you a slice from the start
to the number you left in. If you leave out the second number, if will give you a slice from 
the first number to the end.

You can even put negative numbers inside the brackets. They are an easy way of starting at the
 end of the string instead of the beginning. This way, -3 means "3rd character from the end".
 
Index from rear:    -6  -5  -4  -3  -2  -1      
Index from front:    0   1   2   3   4   5      
                   +---+---+---+---+---+---+    
                   | a | b | c | d | e | f |    
                   +---+---+---+---+---+---+    
Slice from front:  :   1   2   3   4   5   :    
Slice from rear:   :  -5  -4  -3  -2  -1   :

Various Slice options :
a[start:end] # items start through end-1
a[start:]    # items start through the rest of the array
a[:end]      # items from the beginning through end-1
a[:]         # a copy of the whole array

There is also the step value, which can be used with any of the above:

a[start:end:step] # start through not past end, by step 
 

 
'''

print("printing one char ", astr[12])

print("printing from the start ", astr[:3])

print("print from begining to end ", astr[:])

print("printing in from last ", astr[-1])

#Note : The slice operator syntax is  [begin:end:step] , where default step is 1
# which means by default it will move from left to right while step -1 will move from right to left

print("printing the string in reverse", astr[::-1])

print("printing from last index until index 1(non-inclusive)", astr[-1:1:-1])

#Uppercase and Lowercase

print(astr.upper())
print(astr.lower())

#Starts with
print(astr.startswith("Hell"))

#Ends with
print(astr.endswith("Hell"))

#Split
print(astr.split(" "))

#Finds the first occurance 
print("The word begins at ::",astr.find("llo"))

astr.find("llo")

haystack = 'asdfh'

haystack.find('a') # result: 0
haystack.find('h') # result: 4
haystack.find('g') # result: -1

if haystack.find('s') >= 0:
    print('Needle found.')
else:
  print('Needle not found.')
  
#Finding a sub string

if "orld" in astr: 
   print('Sub String exists')  