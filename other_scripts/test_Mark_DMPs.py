# This code takes the DMPs in the provided JSON files, prints out template
# information for each DMP (including RDF Triples).

import json

from collections import Counter

# The id of each file contained in a list.
dmp_file_ids = [102898, 110561, 64375,  83797,  94351,
104396, 111527, 75184,  84265,  95832,
105685, 38304,  77722,  85799,  96070,
105776, 56773,  78027,  88134,  96543,
106382, 64337,  78822,  90090,  98079,
112581, 111764, 111548]

print ('From the Open Science team, we obtained in total ', len (dmp_file_ids),  ' DMPs.')

# To keep count of each template in order to generate statistics.
tmp_ct = Counter()

# This code generates the URI which will be used for the RDF Triple.
linked_dmp_namespace = 'https://linked-dmp.vu.nl/v0.1/'
uses_template = linked_dmp_namespace+'uses_dmp_template'
has_dmp_id = linked_dmp_namespace+'has_dmp_id'

# Create dictionary for each DMP template and the URI.
map_dmp_name_to_URI = {}
# Group 1: Old DMPS from the VU
map_dmp_name_to_URI ["VU DMP template for research with non-personal data"] = 'https://templates.vu.nl/outdated_dmp_template_non-personal_data'
map_dmp_name_to_URI ["VU DMP template for research with personal data"] = 'https://templates.vu.nl/outdated_dmp_template_with_personal_data'
map_dmp_name_to_URI ["Data Management Plan NWO (September 2020)"] = 'https://www.nwo.nl/dmp_nwo_template_2020'

# Group 2: VU's single (conditional) templates to get certified
map_dmp_name_to_URI ["VU DMP template 2021"] = 'https://templates.vu.nl/dmp_template_2021'
map_dmp_name_to_URI ["VU DMP template 2021 (NWO & ZonMW certified)"] = 'https://templates.vu.nl/dmp_template_nwo_zonmw_2021'

# Group 3: Latest templates:
map_dmp_name_to_URI ["1 - VU DMP template 2021 (NWO & ZonMW certified) v1.3"] = 'https://templates.vu.nl/dmp_template_v1.3'

# Group 4: Other templates:
map_dmp_name_to_URI ["ERC DMP"] = 'https://templates.vu.nl/erc_dmp_template'
map_dmp_name_to_URI ["DCC Template"] = 'https://templates.vu.nl/dcc_dmp_template'


path_to_files = './dmps/'
# For each file, we take the template information.
for file_id in dmp_file_ids:
    print ('file id = ', file_id)
    file_name = str(file_id) + '.json'
    print ('file_name = ', file_name)
    with open (path_to_files+file_name) as f:
        data = json.load(f)
        template = data[0][0]['template']['title']
        print ('The template used: ', template)
        tmp_ct[template] += 1
        dmp_uri = linked_dmp_namespace+'dmp/'+str(file_id)
        print ('This VU DMP has a URI: ', dmp_uri)
        template_uri = map_dmp_name_to_URI[template]
        print ('The template has URI: ', template_uri)
        print ('----The RDF Triple----')
        print ('<'+ dmp_uri+ '> <'+ has_dmp_id+ '> "'+ str(file_id) + '"^^<http://www.w3.org/2001/XMLSchema#integer>.')
        print ('<'+ dmp_uri+ '> <'+ uses_template+ '> <'+ template_uri+ '>.')
        print ('\n\n')

# Next, we print some statistics of the template information.
print('\nThe following is a summary of these templates:')
for tmp_name in tmp_ct.keys():
    print ('template ', tmp_name, ' has ', tmp_ct[tmp_name])
