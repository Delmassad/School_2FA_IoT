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

CAM_CAPTURE_URL = 'http://192.168.43.60/capture'

# dataTransfer('./data/', 'LastName', './FaceRecognition/data/')

# img = loadImage('./data/lastPicture.jpeg')

@app.route('/')
def who_am_i():
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

@app.route('/save_picture/<name>')
def save_picture(name=None):
    if name is None:
        return 'ça n\'a pas marché'
    dataTransfer('./data/', name, './FaceRecognition/data/')
    return f'okay c\'est fait chef {name}'
