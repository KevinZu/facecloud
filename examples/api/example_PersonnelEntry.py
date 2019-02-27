import requests
from app.models.face_recognition import CaptureFrame
from multiprocessing import Process
from PIL import Image



def DataEntry(file):
    base = 'v1/'
 
    url = 'http://127.0.0.1:5000/' + base

# files = {'file': open('/root/src/test/facenet/images/images_data_160/ye/4.png', 'rb')}
    files = {'file': file}
# data = {'xxx':'xxx','xxx':'xxx'}
  
    response = requests.post(url + 'PersonnelDataEntry' + '?PersonId=' + personId, files=files) # , data=data)
# json = response.json()
# print(json)
    print(response.url,response.text)

    return True


def StartEntry(name):
    PersonId = name + '001'
    pro = Process(target=CaptureFrame,args=(DataEntry,PersonId,))
    pro.start()

def FaceEntry():
    print("++++++ face entry:")
    name = input('please input your name:')
    StartEntry(name)