import os
import growattServer
import json
import datetime

username = os.environ.get('SHINEPHONE_USERNAME', '')
password = os.environ.get('SHINEPHONE_PASSWORD', '')

api = growattServer.GrowattApi()
login_response = api.login(username, password)

if login_response['success']:
    #Get a list of plants
    user_id = login_response['userId']
    #print(user_id)
    plant_list = api.plant_list(user_id)
    formatted_plant = json.dumps(plant_list, indent=2)
    print(formatted_plant)

    #Get ID of first plant
    plant_id = plant_list['data'][0]['plantId']
    #print(plant_id)

    now = datetime.datetime.now()
    data = api.plant_detail(plant_id, growattServer.Timespan.day, now)
    formatted_data = json.dumps(data, indent=2, sort_keys=True)
    print(formatted_data)
