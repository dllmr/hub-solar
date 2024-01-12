import os
import growattServer

username = os.environ.get('SHINEPHONE_USERNAME', '')
password = os.environ.get('SHINEPHONE_PASSWORD', '')

api = growattServer.GrowattApi()
login_response = api.login(username, password)

if login_response['success']:
    user_id = login_response['userId']
    print(user_id)