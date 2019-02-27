from flask import Flask

app = Flask(__name__)

from multiprocessing import Queue

InfoQueue = Queue()
MessageQueue = Queue()
FrameQueue = Queue()
#from app import routes

#app.run()