"""
This file contains analysis of the following questions:
    Q6: Did you find all the FAIR-Enabling Resources you wanted to specify in the list (using the search bar)?
    Q8: How many years have you been in academia (counting from the start of your PhD)?
    Q9: Have you written any DMP before?
"""

import pandas as pd
from tabulate import tabulate
from main import df

# Analysis of Q6
q6_results = df.loc['Q6']
q6_percentage_yes = (q6_results.value_counts(normalize=True) * 100).get('yes')
q6_percentage_no = (q6_results.value_counts(normalize=True) * 100).get('no')

# Create a table for Q6 analysis
q6_table = pd.DataFrame({'Response': ['yes', 'no'], 'Percentage': [f"{q6_percentage_yes:.2f}%", f"{q6_percentage_no:.2f}%"]})

print("Analysis of Q6: Did you find all the FAIR-Enabling Resources you wanted to specify in the list (using the search bar)?")

# Create and print the table
table_headers = ['Response', 'Percentage']

table1 = tabulate(q6_table, headers=table_headers, tablefmt="simple_grid", showindex=False)
print(table1)
print()




# Analysis of Q8
q8_results = df.loc['Q8']
q8_percentage = (q8_results.value_counts(normalize=True) * 100)

# Create a table for Q8 analysis
q8_table = pd.DataFrame({'Experience Category': q8_percentage.index, 'Percentage': [f"{percentage:.2f}%" for percentage in q8_percentage.values]})

print("Analysis of Q8: How many years have you been in academia (counting from the start of your PhD)?")

# Create and print the table
table_headers2 = ['Experience Category', 'Percentage']

table2 = tabulate(q8_table, headers=table_headers2, tablefmt="simple_grid", showindex=False)
print(table2)
print()




# Analysis of Q9
q9_results = df.loc['Q9']
q9_percentage_yes = (q9_results.value_counts(normalize=True) * 100).get('yes', 0)
q9_percentage_no = (q9_results.value_counts(normalize=True) * 100).get('no', 0)

# Create a table for Q9 analysis
q9_table = pd.DataFrame({'Response': ['yes', 'no'], 'Percentage': [f"{q9_percentage_yes:.2f}%", f"{q9_percentage_no:.2f}%"]})

print("Analysis of Q9: Have you written any DMP before?")
# Create and print the table
table_headers = ['Response', 'Percentage']

table3 = tabulate(q9_table, headers=table_headers, tablefmt="simple_grid", showindex=False)
print(table3)
print()
