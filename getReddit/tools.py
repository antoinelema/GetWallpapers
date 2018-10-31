import os
import requests
import requests.auth


def getToken():
    client_auth = requests.auth.HTTPBasicAuth(os.environ['clientID'], os.environ['clientSecret'])
    post_data = {
        "grant_type": "password",
        "username": "neiho",
        "password": os.environ['passwd']
        }
    headers = {
        'User-Agent': 'My User Agent GetRedditWallpaper',
        'From': 'neiho'
        }

    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
    json_data = response.json()
    token = json_data['access_token']
    return token
