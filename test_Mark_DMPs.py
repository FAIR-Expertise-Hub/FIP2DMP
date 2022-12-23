# general description about this code

import json

from collections import Counter

dmp_file_ids = [102898, 110561, 64375,  83797,  94351,
104396, 111527, 75184,  84265,  95832,
105685, 38304,  77722,  85799,  96070,
105776, 56773,  78027,  88134,  96543,
106382, 64337,  78822,  90090,  98079]

print('From the Open Science team, we obtained in total ', len (dmp_file_ids),  ' DMPs.')

tmp_ct = Counter()

linked_dmp_namespace = 'https://linked-dmp.vu.nl/v0.1/'
uses_template = linked_dmp_namespace+'uses_dmp_template'
has_dmp_id = linked_dmp_namespace+'has_dmp_id'

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
# for each file, we take the template information
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
        print ('This VU DMP has a URI ', dmp_uri)
        print ('It uses template ', template)
        template_uri = map_dmp_name_to_URI[template]
        print ('The template has URI ', template_uri)
        print ('----The RDF Triple----')
        print ('<'+ dmp_uri+ '> <'+ has_dmp_id+ '> '+ str(file_id) + '^^XML:String.')
        print ('<'+ dmp_uri+ '> <'+ uses_template+ '> <'+ template_uri+ '>.')
        print('\n\n')

# Next, we print some statistics of the template information

print('\nThe following is a summary of these templates:')
for tmp_name in tmp_ct.keys():
    print ('template ', tmp_name, ' has ', tmp_ct[tmp_name])
