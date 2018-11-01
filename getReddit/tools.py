import os
import requests
import requests.auth
from subprocess import call
import urllib
from datetime import datetime
import sys

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
    try:
        response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
        response.raise_for_status()
    except Exception as e:
         sys.exit('the token could not be fetched, exiting ...')
    json_data = response.json()
    token = json_data['access_token']
    return token


def getUrlImg(token, count=0):
    url = "https://www.reddit.com/r/wallpapers/hot.json?limit=1"
    try:
        response = get_all(url, token)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_error:
        print(http_error.response.status_code)
        if (http_error.response.status_code == 404):
            sys.exit("there seems to be a problem, oops")
        else:
            if (count == 0):
                with open("../.token",'w') as file:
                    token = getToken()
                    file.write(token)
                    getUrlImg(token, count+1)
            else:
                sys.exit("there seems to be a problem, oops")
    data = response.json()
    url_img = data['data']["children"][0]['data']['url']
    return url_img


def get_all(url,token):
    """Conection et Get du site."""
    querystring = {
        "access_token": token
        }
    header = {
        'User-Agent': 'My User Agent GetRedditWallpaper',
        'From': 'neiho'
        }

    return requests.get(url, headers=header, params=querystring)


def ext(url):
    """ trouve et renvoi l'extention d'une url """
    filename, file_extension = os.path.splitext(url)
    return(file_extension)


def changefond(trueUrlImg):
    """ enregistre l'image et la met en fond """
    now=datetime.now()
    extension=ext(trueUrlImg)
    pathToImg = os.path.expanduser("~")+"/Images/fonds"
    cheminImg = "{}/fond.{}-{}-{}{}".format(pathToImg,now.day,now.month,now.year,extension)
    print("telechargement ...")
    urllib.request.urlretrieve(trueUrlImg, cheminImg)
    call(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", "file://{}".format(cheminImg)])  # change le fond d'ecran de l'ordi #gnome3
