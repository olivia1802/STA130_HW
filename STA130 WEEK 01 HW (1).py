#!/usr/bin/env python
# coding: utf-8

# #1

# In[3]:


import pandas as pd

# Load the CSV data from the URL
url = "https://raw.githubusercontent.com/KeithGalli/pandas/master/pokemon_data.csv"
df = pd.read_csv(url)

# Display the count of missing values in each column
missing_values_count = df.isnull().sum()
print(missing_values_count)


# https://chatgpt.com/c/66de59c4-1fec-800e-a4aa-4cc50f40ca37
# summary of interaction for Q1

# #2

# In statistics, the term "observations" are also known as rows or data points. 
# From my perspective, observations are the single figure or case that we are trying to collect about a given variable. The term "variables" are also known as columns in statistics. Variables could be anything like the attributes, characteristics, or properties that can be measured.Each variable could be used to collect many different types of data. 
# In conclusion, observations and variables are closely linked and has a strong relationship. Mostly, each row represents observations and each column representsvariables. Each observation records values for all the variables.

# In[1]:


import pandas as pd

# Load the dataset from the URL
url = 'https://raw.githubusercontent.com/KeithGalli/pandas/master/pokemon_data.csv'
pokemon_data = pd.read_csv(url)

# Verify the data is loaded by printing the first few rows
print(pokemon_data.head())



# #3

# In[2]:


# Get summary statistics for numerical columns
summary_stats = pokemon_data.describe()
print(summary_stats)



# In[3]:


# Count the occurrences of each unique value in the "Type 1" column
type_counts = pokemon_data['Type 1'].value_counts()
print(type_counts)


# https://chatgpt.com/c/66de5ca2-9e6c-800e-8810-bb21300c600a

# #4

# In[8]:


import pandas as pd

# Load the dataset
url = "https://raw.githubusercontent.com/KeithGalli/pandas/master/pokemon_data.csv"
df = pd.read_csv(url)


# In[9]:


# Get the shape of the DataFrame
shape = df.shape
print("Shape of the DataFrame:", shape)


# In[10]:


# Get a statistical summary of the DataFrame
description = df.describe()
print("Statistical Summary of the DataFrame:")
print(description)


# 

# (a) number of columns analyzed
# - df.shape: 
#     - provides the dimensions of the DataFrame as a tuple. 
#     - includes all columns, regardless of their data type.
# 
# - df.describe():
#     - provides only a summary of numerical columns.
#     - no categorical or non-numerical columns.
#     - no summary will provided if there are categorical or columns with missing values
#     
# (b) "count" column
# - df.shape:
#     - "count" value is just the total number of rows in the DataFrame
#     
# - df.describe():
#     - outputs the number of non-null entries for each numerical column
#     - if missing values are in the column, could generate an error

# Attributes
# - is a property or characteristic of an object that contains a value.
# - can be accessed directly without parentheses.
# - can use it by simply referencing it. 
# - hold data.
# Methods
# - is a function associated with an object.
# - called with parentheses.
# - perform actions.

# https://chatgpt.com/c/66de64a4-6644-800e-9efd-923634073d75

# #6
# 1. Count:
# - the number of non-missing(non-NA/null), or valid,  values in the column
# - tells how many valid entries exist for one variable
# 
# 2. Mean:
# - the average of the data in the column
# - can be calculated by summing up all the values and divde them by the count of values
# 
# 3. Standard Deviation(std):
# - a measure of the amount of variation or dispersion of the data
# - low standard deviation: the data points are close to the mean
# - high standard deviation: the data points are widely spreaded
# 
# 4. Minimum(min):
# - the smallest value in the column
# 
# 5. 25th Percentile(25%):
# - equivalent to the first quartile(Q1)
# - value below which 25% of the data fails
# - measure of the lower range of data distribution
# 
# 6. 50th Percentile(50%):
# - equivalent to the third quartile(Q3)
# - value below which 75% of the data fails
# - measure of the upper range of the data distribution
# 
# 7. Maximum(max):
# - the largest value in the columnd

# #7
# 1. Example of a "use case" in which df.dropna() preferred over del df['col']
# Use Case: Cleaning a Dataset with Partial Missing Data
# Suppose the dataset contains columns such as CustomerID, Name, Email, PhoneNumber, and Age. Some rows have missing values in the PhoneNumber or Email columns, but other information such as CustomerID and Age is complete. 
# The dataset looks like:

# In[6]:


import pandas as pd

data = {
    'CustomerID': [101, 102, 103, 104],
    'Name': ['John', 'Alice', 'Bob', 'Mary'],
    'Email': ['john@example.com', None, 'bob@example.com', 'mary@example.com'],
    'PhoneNumber': [None, '123-456-7890', '987-654-3210', None],
    'Age': [28, 34, 25, 40]
}

df = pd.DataFrame(data)
print(df)


# In this case, I want to clean the records for email and phone contacts since it contains missing values. However, I don't want to drop the entire PhoneNumber and Email columns. Thus, using df.dropna() is a better choice than deleting an entire column with del df['PhoneNumber']. Instead of deleting the entire column, we can target missing rows. 

# 2. Example of "the opposite use case" in which using del df['col'] preferred over df.dropna()

# Use Case: Removing an Entire Column with Mostly Missing or Irrelevant Data
# Suppose there's a large dataset with customer information, including several columns such as CustomerID, Name, Email, PhoneNumber, and DateOfLastPurchase. There's also an additional column, MiddleName, that contains almost entirely missing or irrelvant data. 

# In[8]:


import pandas as pd

data = {
    'CustomerID': [101, 102, 103, 104],
    'Name': ['John', 'Alice', 'Bob', 'Mary'],
    'MiddleName': [None, None, None, 'Ann'],
    'Email': ['john@example.com', 'alice@example.com', 'bob@example.com', 'mary@example.com'],
    'DateOfLastPurchase': ['2023-01-15', '2023-02-20', '2023-03-22', '2023-04-10']
}

df = pd.DataFrame(data)
print(df)


# In this case, I want to remove the entire MiddleName column because 75% of the values are missing(Q3 case). We can use del df['MiddleName'] instead of df.dropna() because it would unnecessarily remove 75% of the rows from the dataset. Overall, del is more simpler and more direct. 

# In[9]:


# Delete the MiddleName column
del df['MiddleName']

print(df)


# 3. Why it is important to apply del df['col'] before df.dropna() when both are used together

# Applying del df['col'] first is important because it allows to remove irrelevant columns with excessive missing values before removing selected rows with missing data in other important columns. We can conclude that following this order can prevent unintentional data loss and ensure more effective data cleaning. 

# 4. Remove all missing data from the dataset using some combination of del df['col'] and/or df.dropna() and give a justification for my approach, including a "before and after" report of the results of my approach for the dataset

# In[10]:


import pandas as pd

# Load the dataset from the provided URL
url = "https://raw.githubusercontent.com/KeithGalli/pandas/master/pokemon_data.csv"
df = pd.read_csv(url)

# Display the first few rows of the dataset
print(df.head())


# In[11]:


# Check for missing data
print(df.info())
print(df.isna().sum())


# We can identify that Type 2 column might be irrelevant when we are not interested in dual-type Pokemon

# In[12]:


# Remove irrelevant column 'Type 2' if not needed for analysis
del df['Type 2']

# Drop rows with missing values in critical columns
df_cleaned = df.dropna(subset=['Name', 'HP', 'Attack'])

# Display the cleaned dataset
print(df_cleaned.head())


# "Before and After" Report:
# 
# Before: I can generate a summary of missing values before cleanup using df.isna().sum(). ex) Type 2 column have missing values
# 
# After: After removing the Type 2 column and dropping rows with missing critical values, I can recheck it with df_cleaned.isna().sum()

# #8
# 1) df.groupby("col1")["col2"].describe()
#     1. df.groupby("col1"):
#           - groups the DataFrame df by the values in 
#             the column "col1".
#           - each value in "col1" will create a group
#           
#     2. ["col2]:
#           - after grouping by "col1", I am selecting only             the "col2" column
#           
#     3. .describe():
#           - generates summary statistics for selected                 column ("col2") within each group
#           - statistics like count, mean, std, min, 25%,               50%, 75%, max are included
#           
# Overall, it first groups the DataFrame by the "col1" values. Then, it calculates statistics for the "col2" column for each group in "col1".
# 
# For example, if "col1" represents Pokemon types and "col2" is their HP, this operation will group the Pokemon by type and output will be the summary statistics(mean, min, max, etc.) for HP within each type. 

# 2) df.describe():
#     - calculates summary statistics for the entire 
#       DataFrame or for each column individually
#     - count represents the number of non-missing
#       (non-NaN) values for each column across the entire
#       dataset
#     - for each column, it gives the total count of 
#       non-missing values
#       
#    df.groupby("col1")["col2"].describe():
#     - groups the DataFrame by "col1" and then calculates
#       summary statistics for the "col2" column within
#       each group
#     - count represents the number of non-missing values in
#       "col2" for each unique group in "col1"
#     - for each group within "col1", it shows how many
#       values in "col2" are non-missing
#       
# Difference matters because:
# - Missing data patterns:
# Grouping by "col1" allows to see if missing data in "col2" is distributed unevenly across different categories in "col1".
# - Global vs. local analysis:
# The df.describe() gives an overall picture of missing data whereas the group-based describe() shows how missingness might differ by group
# 
# To conclude, the values in the count differ because one gives a total for the entire column while the other gives group-specific counts

# #3
# A. 

# In[ ]:


data = {
    'CustomerID': [101, 102, 103, 104],
    'Name': ['John', 'Alice', 'Bob', 'Mary'],
    'Email': ['john@example.com', None, 'bob@example.com', 'mary@example.com'],
    'PhoneNumber': [None, '123-456-7890', '987-654-3210', None],
    'Age': [28, 34, 25, 40]
}

df = pd.DataFrame(data)
print(df)


# Use ChatGPT to Fix the Error:
# ChatGPT told me to include import panadas as pd in my code

# B.

# In[5]:


# Intentional typo in the file name
import pandas as pd

url = "titanics.csv"
df = pd.read_csv(url)


# Use ChatGPT to Fix Error:
# ChatGPT told me to go step by step. First step was mistype the filename. Then, step 2 was to troubleshoot the typo in ChatGPT and identified the error is caused by the typo in the file name.

# C.

# In[6]:


import pandas as pd

# Correctly loading the dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)

# Intentional typo in the DataFrame variable name
DF.groupby("class")["age"].describe()


# Use ChatGPT to Fix Error:
# ChatGPT found the error right away and indicated that in Python, df and DF are considered differnt variables. 

# D.

# In[12]:


import pandas as pd

# Correctly loading the dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
# Missing closing parenthesis
df = pd.read_csv(url


result = df.groupby("class")["age"].describe()


# Use ChatGPT to Fix Error:
# ChatGPT explained to me that I am facing SyntaxError because I did not close the parenthesis correctly. It corrected the code right away. 

# E.

# In[13]:


import pandas as pd

# Loading the dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)

# Mistyped function name
result = df.group_by("class")["age"].describe()


# Use ChatGPT to Fix Error:
# ChatGPT told me the method group_by does not exist on the DataFrame object, so it corrected me to use the method groupby. 

# F.

# In[14]:


import pandas as pd

# Loading the dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)

# Mistyped column name in groupby
result = df.groupby("Sex")["age"].describe()


# Use ChatGPT to Fix Error:
# It identified the issue right away, which is the column "Sex" does not exist in the DataFrame. The correct column name is "sex".

# E.

# In[15]:


import pandas as pd

# Loading the dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)

# Missing quotes around column name
result = df.groupby(sex)["age"].describe()


# Use ChatGPT to Fix Error:
# ChatGPT identified that sex is interpreted as a variable, not a column name, because it is not in quotes. It corrected the error right away.     

# In my opinion, troubleshooting using ChatGPT was a lot helpful because it prompted the correct code right away, while google search requires me extra work since it does not fix the code for me. 

# #9
# Yes

# https://chatgpt.com/c/66e25602-5730-800e-a18b-ba16bcdd7e6b
