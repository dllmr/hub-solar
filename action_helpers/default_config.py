import os
import json
import growattServer
import helper_defs


username = os.environ.get('SHINEPHONE_USERNAME', '')
password = os.environ.get('SHINEPHONE_PASSWORD', '')

api = growattServer.GrowattApi()
login_response = api.login(username, password)

if login_response['success']:
    config = {
        'userId': login_response['userId'],
        'startDate': login_response['user']['createDate'],
        'plantId': login_response['data'][0]['plantId'],
        'plantName': login_response['data'][0]['plantName'].strip()
    }

    with open(helper_defs.CONFIG_FILE, 'w') as config_file:
        json.dump(config, config_file, indent=2)
