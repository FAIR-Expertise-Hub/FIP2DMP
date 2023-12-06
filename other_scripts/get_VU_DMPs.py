# This code takes the DMPs in the provided JSON files, and returns the file ids and titles for all the VU templates.

import json

# The id of each file contained in a list.
dmp_file_ids = [102898, 110561, 64375,  83797,  94351,
104396, 111527, 75184,  84265,  95832,
105685, 38304,  77722,  85799,  96070,
105776, 56773,  78027,  88134,  96543,
106382, 64337,  78822,  90090,  98079]

path_to_files = './dmps/'

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
            file_name = str(file_id) + '.json'
            with open (path_to_files+file_name) as f:
                data = json.load(f)
                print(file_id, ":", data[0][0]['title'])
