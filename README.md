# FIP2DMP

## Overview
Welcome to the FIP2DMP project! This open-source project focuses on analyzing survey results related to Data Management Plans (DMPs) and mapping DMP questions to FAIR implementation profiles (FIPs). The project uses Python for analysis and includes code for processing survey data, mapping questions, and extracting valuable insights.

## Knowledge Models
The project includes knowledge models from FAIR Wizard for both Leiden and Vrije Universiteit Amsterdam, facilitating comprehensive analysis.

### Testing Knowledge Model on FAIR Wizard
We conducted testing on our knowledge model using FAIR Wizard with 5 users. The survey results indicate their experience in creating a DMP project using the knowledge model, which provides suggestions from different research communities as answers.

## Analysis for Survey
### Directory: `analysisForSurvey`
This directory contains Python scripts for analyzing specific survey questions.

- **`main.py`**
  - Stores data on each volunteer.
- **`generalAnalysis.py`**
  - Analyzes data for each question.
- **`analysisOfRemainingQuestions.py`**
  - Analyzes questions Q6, Q8, and Q9 from the survey.
- **`challenges.py`**
  - Analyzes question Q12, focusing on difficulties and challenges faced during DMP creation. In order to extract useful information from the answers for this question, the answers have been analyzed and categorized into common challenges/difficulties encountered by all volunteers.
- **`helpfulOrMisleadingQuestions.py`**
  - Analyzes questions Q4 and Q5, assessing the helpfulness or misleading nature of DMP questions.
- **`importanceOfEntities.py`**
  - Analyzes question Q11, examining the impact of suggestions from various entities.
- **`ratingScale.py`**
  - Analyzes rating scale questions (Q1, Q2, Q3, Q7, Q10) using a scale from 1 to 5.

### Survey Questions
Below is a table defining the survey questions (Q1-Q12):

| Question | Description |
|----------|-------------|
| Q1       | On a scale of 1 to 5, how relevant are communities for this DMP? 1 indicating that no community is relevant and 5 indicating that many communities are relevant. |
| Q2       | On a scale of 1 to 5, please evaluate whether the suggestions provided in this DMP are helpful for the communities in answering their corresponding questions. 1 indicating that it is not helpful and 5 indicating that it is very helpful. |
| Q3       | On a scale of 1 to 5, how much would you consider aligning the decisions in this DMP with those made by the relevant community? 1 indicating minimal alignment and 5 indicating complete alignment. |
| Q4       | On which question(s) were the suggestions helpful or inspiring? |
| Q5       | On which question(s) were the suggestions not helpful or misleading? |
| Q6       | Did you find all the FAIR-Enabling Resources you wanted to specify in the list (using the search bar)? |
| Q7       | On a scale of 1 to 5, how easy was it for you to find the FAIR-Enabling Resource in the search bar? 1 indicating extremely difficult and 5 indicating extremely easy. |
| Q8       | How many years have you been in academia (counting from the start of your PhD)? |
| Q9       | Have you written any DMP before? |
| Q10      | On a scale of 1 to 5, how clear was the goal of the study to you? 1 indicating not clear at all and 5 indicating very clear. |
| Q11      | If you were provided with suggestions from the following entities, whose suggestions will have an impact on your decision? You can select multiple choices from the list. |
| Q12      | During the process of creating this DMP, did you face any specific difficulties or challenges? If so, kindly provide details or specify the challenges you encountered. |

## Mapping
### Directory: `mapping`
This directory focuses on mapping DMP questions to FAIR implementation profiles (FIPs).

- **`dmp_questions.py`**
  - Defines the structure of a DMP question and links the DMP questions to FAIR principles.
- **`fip_questions.py`**
  - Defines the structure of a FIP question.

Additional scripts and documents:
- **`FIP2DMPLeiden_conceptual mapping (1).pdf`**
  - This document links questions in the Leiden DMP template to FAIR principles, providing a conceptual mapping.
- **`global_KM-Leiden-DMP.km`**
- **`gofair-fip-wizard-3.0.0.3.km`**
- **`leiden_KM-Leiden-FIP2DMP_1.0.0.km`**
- **`leiden_maDMP4F_0.0.7.km`**
  - Leiden knowledge model files.
- **`vu-template-dmp-with-fer-v2 4.1.0.km`**
  - Vrije Universiteit knowledge model file.
- **`get_VU_DMPs.py`**
  - This Python code takes the DMPs in the provided JSON files and returns the file IDs and titles for all the Vrije Universiteit templates.
- **`print_keys_DMPs.py`**
  - This Python code takes the DMPs in the provided JSON files and prints out the classes and attributes for each DMP.
- **`test_Mark_DMPs.py`**
  - This Python code takes the DMPs in the provided JSON files and prints out template information for each DMP, including RDF Triples.

## Usage
To run the analysis scripts, ensure you have Python installed. Navigate to the respective script in the `analysisForSurvey` directory and execute it using the Python interpreter.

For mapping DMP questions to FIPs, refer to the `mapping` directory. The provided Python scripts offer functionality such as extracting DMP information and printing template details.

## Contributing
This project is open source, and contributions are welcome.

Thank you for your interest in FIP2DMP!

## Contact
Contact: Shuai Wang (shuai.wang@vu.nl)

## Licence
CC-BY 4.0
