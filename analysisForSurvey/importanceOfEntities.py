"""
This file contains analysis of Q11: 
    If you were provided with suggestions from the following entities, 
    whose suggestions will have an impact on your decision? You can select multiple choices from the list.

The following entities have been used:
    - Department, Faculty, and University Research Data Management
    - University I.T. Support
    - Data Management Platform
    - Data Repository Platform
    - Other software suppliers
    - Search Engines, Indexing Engines, and Data Monitors
    - Community
    - Journal and Venues
    - University Legal and Policy team
    - Faculty Ethical Committee
    - Researcher
    - International or EU Policy offices
    - Funders
"""

import pandas as pd
from tabulate import tabulate
from main import data, entities

def calculate_percentage_count(q_responses, data):
    q_responses_flat = [q for response in q_responses for q in response]
    q_count = {key: sum(key in response for response in q_responses_flat) for key in entities}
    total_volunteers = len(data)
    total_count = sum(q_count.values())
    q1_percentage = {key: (count / total_volunteers) * 100 for key, count in q_count.items()}
    q2_percentage = {key: (count / total_count) * 100 for key, count in q_count.items()}
    
    # Create a DataFrame for the table
    q_table = pd.DataFrame({'Percentage (of Total Volunteers)': q1_percentage, 'Percentage (of Total Count)': q2_percentage, 'Count': q_count})
    q_table['Percentage (of Total Volunteers)'] = q_table['Percentage (of Total Volunteers)'].apply(lambda x: f"{x:.2f}%")
    q_table['Percentage (of Total Count)'] = q_table['Percentage (of Total Count)'].apply(lambda x: f"{x:.2f}%")

    return q_table

# Define the Q11 responses from volunteers
q11_responses = [vol[10] for vol in data.values()]

# Calculate and print the table for Q11 using entities
q11_table = calculate_percentage_count(q11_responses, data)

# Convert the DataFrame to tabulated format
table_headers = ['Entity', '% of Total Volunteers', '% of Total Count', 'Count']

table = tabulate(q11_table, headers=table_headers, tablefmt="simple_grid")

# Print the tabulated table for Q11
print('Table for Q11: Whose suggestions will have an impact on your decision?')
print(table)
