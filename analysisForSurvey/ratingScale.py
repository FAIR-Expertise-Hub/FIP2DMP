"""
This file contains analysis of
    - Q1: On a scale of 1 to 5, how relevant are communities for this DMP? 
        1 indicating that no community is relevant and 5 indicating that many communities are relevant.
    - Q2: On a scale of 1 to 5, please evaluate whether the suggestions provided in this DMP are helpful for the communities in answering their corresponding questions. 
        1 indicating that it is not helpful and 5 indicating that it is very helpful.',
    - Q3: On a scale of 1 to 5, how much would you consider aligning the decisions in this DMP with those made by the relevant community? 
        1 indicating minimal alignment and 5 indicating complete alignment.
    - Q7: On a scale of 1 to 5, how easy was it for you to find the FAIR-Enabling Resource in the search bar? 
        1 indicating extremely difficult and 5 indicating extremely easy.
    - Q10: On a scale of 1 to 5, how clear was the goal of the study to you? 1 indicating not clear at all and 5 indicating very clear.

All these questions deal with a rating scale from 1 (e.g. extremely difficult) to 5 (e.g. very easy). 
"""

from tabulate import tabulate
from main import questions, df

# Define the questions you want to include in the table
questions_to_include = ['Q1', 'Q2', 'Q3', 'Q7', 'Q10']

# Create a list of question texts in the same order as questions_to_include
question_text = ["How relevant are communities for this DMP?", 
                 "Are DMP suggestions helpful to answer community questions?", 
                 "Aligning DMP with community decisions: Importance?", 
                 "How easy was it for you to find the FER in the search bar?", 
                 "How clear was the goal of the study to you?"]

# Create a list to store the table data
table_data = []

# Iterate through the questions
for question in questions:
    if question['name'] in questions_to_include:
        question_name = question['name']
        mean_value = round(df.loc[question_name].mean(), 2)
        max_value = df.loc[question_name].max()
        min_value = df.loc[question_name].min()
        median_value = df.loc[question_name].median()
        std_value = round(df.loc[question_name].std(), 2) 
        range_value = [min_value, max_value]  # Combine min and max as a list
        table_data.append([question_name, question_text[questions_to_include.index(question_name)], range_value, mean_value, median_value, std_value])

# Create and print the table
table_headers = ['Question Description','Range', 'Mean', 'Median', 'Std']

table = tabulate(table_data, headers=table_headers, tablefmt="simple_grid")
print(table)
