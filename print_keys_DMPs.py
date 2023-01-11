# This code takes the DMPs in the provided JSON files, prints out the classes and the attributes for each DMP.

import json
from pprint import pprint

from collections import Counter

# The id of each file contained in a list.
dmp_file_ids = [102898, 110561, 64375,  83797,  94351,
104396, 111527, 75184,  84265,  95832,
105685, 38304,  77722,  85799,  96070,
105776, 56773,  78027,  88134,  96543,
106382, 64337,  78822,  90090,  98079,
112581, 111764, 111548]

print ('From the Open Science team, we obtained in total ', len (dmp_file_ids),  ' DMPs.')

path_to_files = './dmps/'

# Function to print out the attributes in each DMP json file.
def print_keys(dl, num_tab):
    if isinstance(dl, dict):
        for k in dl.keys():
            print ('\t'*num_tab, k)
            print_keys(dl[k], num_tab +1)
            # --------comment the four lines below to print only the keys
            # if not isinstance(dl[k], list) and not isinstance(dl[k], dict):
            #     print ('\t'*num_tab, k, ' : ', dl[k])
            # else:
            #     print_keys(dl[k], num_tab +1)
    elif isinstance(dl, list):
        for l in dl:
            # print ('\t'* num_tab, '--------')
            print_keys(l, num_tab+1)
        # print (dl)

# remove html tags and return a clean string.
import re
def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

# print all the questions. 
def print_questions(dl, num_tab):
    if isinstance(dl, dict):
        for k in dl.keys():
            # if num_tab > 2 :
            #     print ('\t'*num_tab, k, dl[k])
            # print_keys(dl[k], num_tab +1)
            # --------comment the four lines below to print only the keys
            # if k =='description':
            #     print ('\t'*num_tab, dl[k])

            if k == 'questions':
                print ('\n','\t'*num_tab, 'Section title:', dl['title'])
                # print ('\t'*num_tab, 'description:', dl['description'])
                print ('\t'*num_tab, 'questions:')
                for q in dl[k]:
                    print ('\t' * (num_tab+1), )
                    print ('\t' * (num_tab+1), 'Question No.', q['number'], ' = ', striphtml(q['text']))

            # if not isinstance(dl[k], list) and not isinstance(dl[k], dict):
            #     print ('\t'*num_tab, k, ' : ', dl[k])

            print_questions(dl[k], num_tab +1)
    elif isinstance(dl, list):
        for l in dl:
            # if num_tab > 3 :
            #     print ('\t'*num_tab, l)
            # print ('\t'* num_tab, '--------')
            print_questions(l, num_tab + 1)


# Map template to file_ids.
map_template_to_file_ids = {}
for file_id in dmp_file_ids:
    print ('file id = ', file_id)
    file_name = str(file_id) + '.json'
    with open (path_to_files+file_name) as f:
        data = json.load(f)
        template = data[0][0]['template']['title']
        print ('The template used: ', template)
        if template in map_template_to_file_ids.keys():
            map_template_to_file_ids[template].append(file_id)
        else:
            map_template_to_file_ids[template] = [file_id]

# Next, we print some template information and an overview of all the attributes for each DMP json file.
for temp in map_template_to_file_ids:
    print ('*'*20)
    print ('Now Let us handle DMP template: ', temp)
    dmp_ids = map_template_to_file_ids[temp]
    for file_id in dmp_ids:
        print ('file id = ', file_id)
        file_name = str(file_id) + '.json'
        print ('file_name = ', file_name)
        with open (path_to_files+file_name) as f:
            data = json.load(f)
            # print_keys(data[0][0], 1)
            print_questions(data[0][0], 1)
