# This code takes the DMPs in the provided JSON files, prints out the classes and the attributes for each DMP.

import json
from pprint import pprint

from collections import Counter

# The id of each file contained in a list.
dmp_file_ids = [102898, 110561, 64375,  83797,  94351,
104396, 111527, 75184,  84265,  95832,
105685, 38304,  77722,  85799,  96070,
105776, 56773,  78027,  88134,  96543,
106382, 64337,  78822,  90090,  98079]

# To keep count of each template in order to generate statistics.
tmp_ct = Counter()

# This code generates the URI which will be used for the RDF Triple.
linked_dmp_namespace = 'https://linked-dmp.vu.nl/v0.1/'
uses_template = linked_dmp_namespace+'uses_dmp_template'
has_dmp_id = linked_dmp_namespace+'has_dmp_id'

# Create dictionary for each DMP template and the URI.
map_dmp_name_to_URI = {}
map_dmp_name_to_URI ["Data Management Plan NWO (September 2020)"] = 'https://www.nwo.nl/dmp_template_2020'
map_dmp_name_to_URI ["VU DMP template for research with personal data"] = 'https://templates.vu.nl/dmp_template'
map_dmp_name_to_URI ["1 - VU DMP template 2021 (NWO & ZonMW certified) v1.3"] = 'https://templates.vu.nl/dmp_template_v1.3'
map_dmp_name_to_URI ["VU DMP template for research with non-personal data"] = 'https://templates.vu.nl/dmp_template_non-personal_data'
map_dmp_name_to_URI ["VU DMP template 2021 (NWO & ZonMW certified)"] = 'https://templates.vu.nl/dmp_template_nwo_zonmw'
map_dmp_name_to_URI ["ERC DMP"] = 'https://erc.eu/template'
map_dmp_name_to_URI ["VU DMP template 2021"] = 'https://templates.vu.nl/dmp_template_v1.3'
map_dmp_name_to_URI ["DCC Template"] = 'https://templates.vu.nl/dcc_template'

path_to_files = './dmps/'

# Function to print out the attributes in each DMP json file. 
def print_keys(dl, num_tab):
    if isinstance(dl, dict):
        for k in dl.keys():
            print ('\t'*num_tab, k)
            print_keys(dl[k], num_tab +1)

# Map template to file_ids.
map_template_to_file_ids = {}
for file_id in dmp_file_ids:
    file_name = str(file_id) + '.json'
    with open (path_to_files+file_name) as f:
        data = json.load(f)
        template = data[0][0]['template']['title']
        if template in map_template_to_file_ids.keys():
            map_template_to_file_ids[template].append(file_id)
        else:
            map_template_to_file_ids[template] = [file_id]


# Initializing search key string.
search_key = 'VU'

# Substring Key match in map_template_to_file_ids.
res = dict(filter(lambda item: search_key in item[0], map_template_to_file_ids.items()))

# Prints out the VU templates with the associated file ids and titles of the DMPs.
for temp in map_template_to_file_ids:
    if temp in res.keys():
        print('\n' + str(temp))
        for file_id in map_template_to_file_ids[temp]:
            if str(file_id) in str(res):
                file_name = str(file_id) + '.json'
                with open (path_to_files+file_name) as f:
                    data = json.load(f)
                    for k in data[0][0].keys():
                        if k == 'title':
                            print(file_id, ":", data[0][0][k]) 