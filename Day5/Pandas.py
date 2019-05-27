import pandas as pd
from IPython.display import display


# Read csv file
df = pd.read_csv(r"C:\Users\sk250102\Desktop\PythonTraining\Day5\Salaries.csv")
# Save the file
#df.to_csv("Salaries.csv")

# Display a few first records
display(df.head())

# Display first 10 records
print(df.head(10))

# Display the last 5 records
df.tail()

#No of rows
df.index 

#List of Columns
df.columns



# Identify the type of df object
type(df)

# Check the type of a column "salary"
df["salary"].dtype

# the type of the object -- Series
type(df["salary"])

# the type of the object -- DataFrame
type(df[["salary"]])




#List the types of all columns
df.dtypes

#List the column names
df.columns

#List the row labels and the column names
df.axes

#Number of dimensions
df.ndim

#Total number of elements in the Data Frame
df.size

#Number of rows and columns
df.shape

#Output basic statistics for the numeric columns
df.describe()

#Calculate mean for all numeric columns
df.mean()

#Calculate the standard deviation (std() method) for all numeric columns
df.std()

#Calculate average of the columns in the first 50 rows
df.head(50).mean()

####### Data slicing and grouping

df_gender = df.groupby('gender')

#Extract a column by name (method 1)
df['gender'].head()

#Extract a column name (method 2)
df.gender.head()

#Calculate the basic statistics for the salary column
#  (use describe() method)
df['salary'].describe()

#Calculate how many values in the salary column 
# (use count() method)
df['salary'].count()

#Calculate the average salary
df['salary'].mean()

#Group data using rank
df_rank = df.groupby('rank')

#Calculate mean of all numeric columns for the grouped object
df_rank.mean()

#Calculate the mean salary for men and women. 
# The following produce Pandas Series (single brackets around salary)
df.groupby('gender')['salary'].mean()

# If we use double brackets Pandas will produce a DataFrame
df.groupby('gender')[['salary']].mean()

# Group using 2 variables - gender and rank:
df.groupby(['gender','rank'], sort=False)[['salary']].mean()

# Group data by the discipline and find the average salary for each group
df.groupby('discipline')['salary'].mean()


#Select observation with the value in the salary column > 120K
df_sub = df[ df['salary'] > 120000]
df_sub.head()

#Select data for female professors
df_w = df[ df['gender'] == 'Female']
df_w.head()

# Using filtering, find the mean value of the salary for the discipline A
df[df['discipline'] == 'A']['salary'].mean()

# Extract (filter) only observations with high salary ( > 100K) and find how many female and male professors in each group
df[df['salary'] > 120000].groupby('gender')['salary'].count()

### More on slicing the dataset
#Select column salary
df1 = df['salary']

#Check data type of the result
type(df1)

#Look at the first few elements of the output
df1.head()

#Select column salary and make the output to be a data frame
df2 = df[['salary']]

#Check the type
type(df2)

#Select a subset of rows (based on their position):
# Note 1: The location of the first row is 0
# Note 2: The last value in the range is not included
df[2:10]


#If we want to select both rows and columns we can use method .loc
df.loc[10:20,['rank', 'gender','salary']]

#Let's see what we get for our df_sub data frame
# Method .loc subset the data frame based on the labels:
df_sub.loc[10:20,['rank','gender','salary']]

#  Unlike method .loc, method iloc selects rows (and columns) by poistion:
df_sub.iloc[10:20, [0,3,4,5]]


# ### Sorting the Data

#Sort the data frame by yrs.service and create a new data frame
df_sorted = df.sort_values(by = 'service')
df_sorted.head()

#Sort the data frame by yrs.service and overwrite the original dataset
df.sort_values(by = 'service', ascending = False, inplace = True)
df.head()

# Restore the original order (by sorting using index)
df.sort_index(axis=0, ascending = True, inplace = True)
df.head()

# Sort data frame by the salary (in descending order) and display the first few records of the output (head)
df.sort_values(by='salary', ascending=False).head()

#Sort the data frame using 2 or more columns:
df_sorted = df.sort_values(by = ['service', 'salary'], ascending = [True,False])
df_sorted.head(10)


# ### Missing Values

# Read a dataset with missing values
flights = pd.read_csv(r"C:\Users\sk250102\Desktop\PythonTraining\Day5\flights.csv")
flights.head()
# Select the rows that have at least one missing value
flights[flights.isnull().any(axis=1)].head()



# Filter all the rows where arr_delay value is missing:
flights1 = flights[ flights['arr_delay'].notnull( )]
flights1.head()

# Remove all the observations with missing values
flights2 = flights.dropna()


# Fill missing values with zeros
nomiss =flights['dep_delay'].fillna(0)
nomiss.isnull().any()

# Count how many missing data are in dep_delay and arr_delay columns
flights[['dep_delay','arr_delay']].isnull().sum()


# ### Common Aggregation Functions:
# 
# |Function|Description
# |-------|--------
# |min   | minimum
# |max   | maximum
# |count   | number of non-null observations
# |sum   | sum of values
# |mean  | arithmetic mean of values
# |median | median
# |mad | mean absolute deviation
# |mode | mode
# |prod   | product of values
# |std  | standard deviation
# |var | unbiased variance

# Find the number of non-missing values in each column
flights.count()

# Find mean value for all the columns in the dataset
flights.min()

# Let's compute summary statistic per a group':
flights.groupby('carrier')['dep_delay'].mean()

# We can use agg() methods for aggregation:
flights[['dep_delay','arr_delay']].agg(['min','mean','max'])

# An example of computing different statistics for different columns
flights.agg({'dep_delay':['min','mean',max], 'carrier':['nunique']})

# ### Basic descriptive statistics
# |Function|Description
# |-------|--------
# |min   | minimum
# |max   | maximum
# |mean  | arithmetic mean of values
# |median | median
# |mad | mean absolute deviation
# |mode | mode
# |std  | standard deviation
# |var | unbiased variance
# |sem | standard error of the mean
# |skew| sample skewness
# |kurt|kurtosis
# |quantile| value at %

# Convinient describe() function computes a veriety of statistics
flights.dep_delay.describe()

# find the index of the maximum or minimum value
# if there are multiple values matching idxmin() and idxmax() will return the first match
flights['dep_delay'].idxmin()  #minimum value

# Count the number of records for each different value in a vector
flights['carrier'].value_counts()