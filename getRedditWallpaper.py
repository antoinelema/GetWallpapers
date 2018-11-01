from getReddit import tools
import json
import os

token = tools.getToken()

url = "https://www.reddit.com/r/wallpapers/hot.json?limit=1"

response = tools.get_all(url, token)
data = response.json()
url_img = data['data']["children"][0]['data']['url']

tools.changefond(url_img)
