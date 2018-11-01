from getReddit import tools

with open(".token", 'r+') as file:
    file_data = file.read()
    if file_data == "":
        token = tools.getToken()
        file.write(token)
    else:
        token = file_data

url_img = tools.getUrlImg(token)
tools.changefond(url_img)
