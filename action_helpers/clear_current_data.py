import json
import helper_defs


empty_dict = {}

with open(helper_defs.TODAY_FILE, 'w') as data_file:
    json.dump(empty_dict, data_file)

with open(helper_defs.THIS_MONTH_FILE, 'w') as data_file:
    json.dump(empty_dict, data_file)
