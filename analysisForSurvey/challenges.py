"""
This file contains analysis of Q12: 
    During the process of creating this DMP, did you face any specific difficulties or challenges? 
    If so, kindly provide details or specify the challenges you encountered.

In order to extract useful information from the answers for this question, the answers have been analyzed
and then categorized into common challenges/difficulties encountered by all volunteers. 
"""

from main import data
from tabulate import tabulate
import pandas as pd

# Define your categories and corresponding keywords or patterns
categories = {
    'Terminology and Language': ['terminology not always clear', 'struggled understanding the terminology'],
    'Knowledge and Training': ['not being familiar with metadata standards', 'not particularly knowledgeable', 'in need of information/training', 'more context might have helped'],
    'Understanding Recommendations from Communities': ['not clear how the recommendations from different communities came about', 'could judge their usefulness'],
    'Understanding the Use of FIPS/FERs': ['use of fips and fers'],
    'Specific DMP Challenges': ['two pages in that file instead of seven pages', 'concepts in the DMP are difficult to comprehend'],
    # 'No Challenges': ['did not face any specific difficulties', 'none'],
}

# Calculate the total number of volunteers
total_volunteers = len(data)

# Initialize category counts and percentages
category_counts = {category: 0 for category in categories}
category_percentages = {category: 0 for category in categories}

# Iterate through the responses and categorize them
for volunteer, response in data.items():
    # Extract the response for question 12
    q12_response = response[-1]

    # Initialize category flags for the current response
    response_categories = {category: False for category in categories}

    # Check for each keyword or pattern in the response and categorize it
    for keyword, patterns in categories.items():
        for pattern in patterns:
            if pattern in q12_response.lower():
                response_categories[keyword] = True

    # Update the category counts for this response
    for category, flag in response_categories.items():
        if flag:
            category_counts[category] += 1

# Calculate category percentages
for category, count in category_counts.items():
    category_percentages[category] = (count / total_volunteers) * 100

# Create a DataFrame for the category counts and percentages
category_df = pd.DataFrame({'Category': category_counts.keys(), 'Count': list(category_counts.values()),
                            '%': [f'{percent:.2f}%' for percent in category_percentages.values()]})

# Print the category counts
print("Category Counts for Question 12: Specific difficulties or challenges?")

# Create and print the table
table_headers = ['Category', 'Count', '%']

table3 = tabulate(category_df, headers=table_headers, tablefmt="simple_grid", showindex=False)
print(table3)
