import requests

base = 'v1/'
 
url = 'http://127.0.0.1:5000/' + base

# files = {'file': open('/root/src/test/facenet/images/images_data_160/ye/4.png', 'rb')}
files = {'file': open('/root/Downloads/1.jpg', 'rb')}
# data = {'xxx':'xxx','xxx':'xxx'}
  
response = requests.post(url + 'PersonnelDataEntry' + '?PersonId=tangge0098', files=files) # , data=data)
# json = response.json()
# print(json)
print(response.url,response.text)