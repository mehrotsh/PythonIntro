readPath=r"C:\Users\sk250102\Desktop\PythonTraining\Day5\file.log"
infile = open(readPath,"r")
lines = infile.readlines()
infile.close()
for line in lines:
   print (line, end=" ")

#Line-by-line (shortcut syntax avoiding readline calls):
readPath=r"C:\Users\sk250102\Desktop\PythonTraining\Day5\file.log"
infile = open(readPath,"r")
for line in infile:
   print (line,end=" ")
infile.close()

#Writing file using context manager
writePath=r"C:\Users\sk250102\Desktop\PythonTraining\Day5\fileWrite.log"
with open(writePath,"a",encoding = 'utf-8') as f:
   f.write("my third file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")