# Notes on Python for Data

# import library_name as alias
# dataset_name = pd.read_csv('filename.csv')
# dataset_name.head() -> previews first 5 lines
#alternative to .head() -> DataFrame.head(n=10) where n=# of lines
# dataset_name.dtypes

#import pandas as pd
#departments = pd.read_csv('departments_example.csv')
#departments.head() 
#departments.dtypes

#------------------------------------------------------

# dictionary = {
# key1:value1,
# key2:value2,
# key3:value3 }

# access values -> dictionary[key]

# .append() for adding new elements to a list

#------------------------------------------------------
# Counting Values:

# example: dataset = repair
# repair = pd.read_csv('repair.csv')

# repair['product_category'].value_counts()
# lamp                                 4250
# laptop                               4139
# vacuum                               4034

# The .value_counts() method has a few different parameters we can modify, including

# example: repair['product_category'].value_counts(normalize=True) -> (example: lamp         0.068445)

# normalize=True, which will return percentages instead of raw numbers 
# ascending=True, which will sort from smallest to largest, instead of largest to smallest

# -----------------------------------------------------
# Summarizing Numeric Data:

# The Series method .describe() calculates statistical information about the numbers in a numeric column.
# example:
# repair['product_age'].describe()
# count    21823.000000
# mean        12.202012
# std         14.612353
# min          0.000000
# 25%          4.000000
# 50%          7.000000
# 75%         15.000000
# max        122.000000
# Name: product_age, dtype: float64

# count: the number of numbers in the column
# mean: the average of the numbers in the column
# std: the standard deviation of the numbers in the column
# in: the minimum of the numbers in the column
# 25%, 50%, 75%: the 25th, 50th, and 75th percentiles of the numbers in the column
# max: the maximum of the numbers in the column

# The .describe() method can be used on columns with the object type, but the output is different.
# example:
# repair['repair_status'].describe()
# count     62094
# unique        4
# top       fixed
# freq      32601
# Name: repair_status, dtype: object

# count: the number of (non-missing) entries in the column.
# unique: the number of unique values. From the last exercise, we know they are fixed, repairable, end of life, and unknown.
# top: the most frequent value
# freq: the number of times the top value appears