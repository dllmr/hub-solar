import os
import json
import growattServer
import helper_defs


username = os.environ.get('SHINEPHONE_USERNAME', '')
password = os.environ.get('SHINEPHONE_PASSWORD', '')

api = growattServer.GrowattApi()
login_response = api.login(username, password)

if login_response['success']:
    with open(helper_defs.CONFIG_FILE, 'r') as config_file:
        config = json.load(config_file)

    plantId = config['plantId']
    
    today_data = api.plant_detail(plantId, growattServer.Timespan.day)
    if today_data['success']:
        with open(helper_defs.TODAY_FILE, 'w') as data_file:
            json.dump(today_data, data_file, indent=2, sort_keys=True)

    this_month_data = api.plant_detail(plantId, growattServer.Timespan.month)
    if this_month_data['success']:
        with open(helper_defs.THIS_MONTH_FILE, 'w') as data_file:
            json.dump(this_month_data, data_file, indent=2, sort_keys=True)
