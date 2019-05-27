import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="mukesh",
  passwd="mysql",
  database ="test"
)

data = pd.read_sql('select * from test.students', mydb)

print(data.head())

query="select * from test.students"
generator_df = pd.read_sql(sql=query,  con=mydb) # mysql query

print(generator_df.head())
mydb.close()

outPath=r"C:\Users\sk250102\Desktop\PythonTraining\Day5\sqlOut.csv"
generator_df.to_csv(outPath, encoding = 'utf-8', index = True)
