import os
import growattServer

username = os.environ.get('SHINEPHONE_USERNAME', '')
password = os.environ.get('SHINEPHONE_PASSWORD', '')

api = growattServer.GrowattApi()
login_response = api.login(username, password)

if login_response['success']:
    user_id = login_response['userId']
    plant_list = api.plant_list(user_id)

    #Get ID of first plant
    #TODO - get all plant IDs as a list
    plant_id = plant_list['data'][0]['plantId']
    print(plant_id)
