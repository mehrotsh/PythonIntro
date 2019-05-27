#Basic structure of Exception Handling
import sys
import traceback
try:
   #i = int("snakes")
   i = int("9")
   rem=i/0
   print("the integer is", i)
except (ValueError):
   print("oops!  invalid value")
   print(traceback.format_exc())
except Exception as e:
    print("Unexpected error:", sys.exc_info()[0])  
    print("the error occured because of :",str(e)) 
    print(traceback.format_exc())
else :
   print("Try block got executed without exception")
finally :
   print("This block will always be executed!")   
