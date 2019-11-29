from flask import Flask
from io import open as iopen
from base64 import decodebytes
import numpy as np
import cv2
import requests
from FaceDetection import dataTransfer
from FaceRecognition import votingRecognition
from miscelaneous import loadImage
app = Flask(__name__)

CAM_CAPTURE_URL = 'http://192.168.4.38/capture'

# dataTransfer('./data/', 'LastName', './FaceRecognition/data/')

# img = loadImage('./data/lastPicture.jpeg')

@app.route('/')
def hello_world():
    file_name = './data/test.jpeg'
    i = requests.get(CAM_CAPTURE_URL)
    if i.status_code == requests.codes.ok:
        arr = np.fromstring(i.content, dtype=np.uint8)
        im = cv2.imdecode(arr, 1)
        cv2.imwrite('./data/lastPicture.jpeg', im)
        img = loadImage('./data/lastPicture.jpeg')
        return votingRecognition(img)
    else:
        return 'sorry I don\' get it'