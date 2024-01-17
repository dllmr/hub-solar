import os
import json
import datetime
import growattServer


username = os.environ.get('SHINEPHONE_USERNAME', '')
password = os.environ.get('SHINEPHONE_PASSWORD', '')

api = growattServer.GrowattApi()
login_response = api.login(username, password)

if login_response['success']:
    createDateStr = login_response['user']['createDate']
    startDate = datetime.datetime.fromisoformat(createDateStr).date()

    config = {
        'userId': login_response['userId'],
        'startDate': startDate,
        'plantId': login_response['data'][0]['plantId'],
        'plantName': login_response['data'][0]['plantName'].strip()
    }

    with open('../config/config.json', 'w') as config_file:
        json.dump(config, config_file, indent=2)

