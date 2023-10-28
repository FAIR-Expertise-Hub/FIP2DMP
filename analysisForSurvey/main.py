import pandas as pd

# Define a dictionary to map short question names to their descriptions
q = {
    '4.6': 'Q4.6 Where will you publish your data assets?',
    '4.8': 'Q4.8 How will you ensure your data assets get a persistent identifier (e.g. a DOI-code)?',
    '4.9': 'Q4.9 Will you register your datasets in an online registry other than PURE? If yes, where?',
    '4.13': 'Q4.13 Please indicate the license and/ or terms of use under which you share your data.',
    '5.1': 'Q5.1 What metadata and documentation will accompany the project?',
    '5.2': 'Q5.2 What metadata and documentation will accompany the data assets?',
    '5.3': 'Q5.3 What methods, software or hardware are needed to access and use your data?',
    'None': 'None of the above',
}

entities = [
    'Department, Faculty, and University Research Data Management', 
    'University I.T. Support',
    'Data Management Platform',
    'Data Repository Platform',
    'Other software suppliers',
    'Search Engines, Indexing Engines, and Data Monitors',
    'Community',
    'Journal and Venues',
    'University Legal and Policy team',
    'Faculty Ethical Committee',
    'Researcher',
    'International or EU Policy offices',
    'Funders']

# Define the questions, question types, question text and all possible answers
questions = [
    {
        'name': 'Q1',
        'type': 'rating scale',
        'text': 'On a scale of 1 to 5, how relevant are communities for this DMP? 1 indicating that no community is relevant and 5 indicating that many communities are relevant.',
        'options': [1, 2, 3, 4, 5],
    },
    {
        'name': 'Q2',
        'type': 'rating scale',
        'text': 'On a scale of 1 to 5, please evaluate whether the suggestions provided in this DMP are helpful for the communities in answering their corresponding questions. 1 indicating that it is not helpful and 5 indicating that it is very helpful.',
        'options': [1, 2, 3, 4, 5],
    },
    {
        'name': 'Q3',
        'type': 'rating scale',
        'text': 'On a scale of 1 to 5, how much would you consider aligning the decisions in this DMP with those made by the relevant community? 1 indicating minimal alignment and 5 indicating complete alignment.',
        'options': [1, 2, 3, 4, 5],
    },
    {
        'name': 'Q4',
        'type': 'mutiple response',
        'text': 'On which question(s) were the suggestions helpful or inspiring?',
        'options': list(q.keys()),
    },
    {
        'name': 'Q5',
        'type': 'mutiple response',
        'text': 'On which question(s) were the suggestions not helpful or misleading?',
        'options': list(q.keys()),
    },
    {
        'name': 'Q6',
        'type': 'multiple choice',
        'text': 'Did you find all the FAIR-Enabling Resources you wanted to specify in the list (using the search bar)?',
        'options': ['yes', 'no'],
    },
    {
        'name': 'Q7',
        'type': 'rating scale',
        'text': 'On a scale of 1 to 5, how easy was it for you to find the FAIR-Enabling Resource in the search bar? 1 indicating extremely difficult and 5 indicating extremely easy.',
        'options': [1, 2, 3, 4, 5],
    },
    {
        'name': 'Q8',
        'type': 'multiple choice',
        'text': 'How many years have you been in academia (counting from the start of your PhD)?',
        'options': ['Less than 1 year', '1-2 years', '3-5 years', '6-10 years', 'More than 10 years'],
    },
    {
        'name': 'Q9',
        'type': 'multiple choice',
        'text': 'Have you written any DMP before?',
        'options': ['yes', 'no'],
    },
    {
        'name': 'Q10',
        'type': 'rating scale',
        'text': 'On a scale of 1 to 5, how clear was the goal of the study to you? 1 indicating not clear at all and 5 indicating very clear.',
        'options': [1, 2, 3, 4, 5],
    },
    {
        'name': 'Q11',
        'type': 'multiple response',
        'text': 'If you were provided with suggestions from the following entities, whose suggestions will have an impact on your decision? You can select multiple choices from the list.',
        'options': entities,
    },
    {
        'name': 'Q12',
        'type': 'text',
        'text': 'During the process of creating this DMP, did you face any specific difficulties or challenges? If so, kindly provide details or specify the challenges you encountered.',
        'options': [], 
    },
]

# Manually input data for 5 volunteers
data = {
    'Volunteer 1': [3, 2, 3, (q['4.6'], q['4.8'], q['4.9'], q['4.13'], q['5.1'], q['5.2'], q['5.3']), (q['None'], ), 'yes', 5, '6-10 years', 'yes', 3, [entities[0], entities[1], entities[2], entities[3], entities[8], entities[9], entities[11], entities[12]], 'Terminology not always clear (many abbreviations and lots of technical language). Not being familiar with metadata standards, this was confusing. I think not only I, but most colleagues, are in need of information/training on Data management  practices in general, but perhaps metadata practices in particular.'],
    'Volunteer 2': [3, 4, 2, (q['4.6'], q['4.8'], q['4.13'], q['5.1']), (q['4.9'], q['5.3']), 'no', 3, '3-5 years', 'yes', 4, [entities[0], entities[7], entities[8], entities[9], entities[10], entities[12]], 'At times I struggled understanding the terminology (while I have created DMPs before I wouldn\'t describe myself as particularly knowledgeable on the matter) On a more methodological level, I would probably have had an easier time doing this for a project I am working on myself. At times it was not clear to me how the recommendations from different communities came about and how I could judge their usefulness. More context might have helped.'],
    'Volunteer 3': [3, 4, 4, (q['4.13'], ), (q['5.1'], q['5.2']), 'no', 2, '3-5 years', 'yes', 2, [entities[0], entities[1], entities[2], entities[3], entities[6], entities[7], entities[8], entities[9], entities[10], entities[11]], 'I didn\'t really understood the use of FIPs and FERs.'],
    'Volunteer 4': [3, 3, 3, (q['4.9'], ), (q['5.1'], q['5.2']), 'no', 4, '6-10 years', 'yes', 4, [entities[0], entities[1], entities[6], entities[9], entities[10]], 'I did not face any specific difficulties'],
    'Volunteer 5': [4, 3, 3, (q['4.8'], q['4.9']), (q['4.13'], q['5.1'], q['5.2']), 'yes', 2, '6-10 years', 'yes', 3, [entities[0], entities[1], entities[2], entities[6], entities[9], entities[10]], 'I chose mock DMP 2 "Understanding Public Opinion on Climate Change" because this topic is more close to the theory and method I\'ve conducted before. Somehow there was only two pages in that file instead of seven pages as it stated. I am not sure whether this is on purpose or not. Also, I think due to my own background and experiences with qualitative methods including ethnographic methods, many concepts in the DMP are difficult for me to comprehend. For researchers like me, this type of DMP is not so common. So I am not sure my answers can contribute to your study.'],
}

# Create a DataFrame for the volunteer responses
df = pd.DataFrame(data, index=[question['name'] for question in questions])
