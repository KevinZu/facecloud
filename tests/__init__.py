# facecloud/tests/__init__.py

from app.api import app
from app.models.face_recognition import process_start
# from app.models import prcesses
from app import MessageQueue


process_start()
print('===== process_start ok!')
app.run()

MessageQueue.put("complate_msg")
MessageQueue.put("complate_msg")

# for p in processes:
#    p.join() 