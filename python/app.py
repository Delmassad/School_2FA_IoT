from flask import Flask
import os
from io import open as iopen
from datetime import datetime
from base64 import decodebytes
import numpy as np
import cv2
import requests
from FaceDetection import dataTransfer
from FaceRecognition import votingRecognition
from miscelaneous import loadImage, listdir, listFiles, empty_dir
from flask_cors import CORS
from flask import jsonify, abort, Response
app = Flask(__name__, static_folder="static")
CORS(app)

CAM_CAPTURE_URL = 'http://192.168.43.60/capture'

# dataTransfer('./data/', 'LastName', './FaceRecognition/data/')

# img = loadImage('./data/lastPicture.jpeg')

@app.route('/health')
@app.route('/')
def health():
    return 'server running'

@app.route('/who_am_i')
def who_am_i():
    i = requests.get(CAM_CAPTURE_URL)
    if i.status_code == requests.codes.ok:
        arr = np.fromstring(i.content, dtype=np.uint8)
        im = cv2.imdecode(arr, 1)
        # remove old last pic
        empty_dir('./static/lastPicture')
        # write the new one
        time = datetime.now()
        cv2.imwrite(f'./static/lastPicture/lastPicture_{time}.jpeg', im)
        img = loadImage(f'./static/lastPicture/lastPicture_{time}.jpeg')
        return votingRecognition(img)
    else:
        abort(500)
# # for testing
#     img_name = listFiles('./static/lastPicture')[0]
#     img = loadImage(f'./static/lastPicture/{img_name}')
#     empty_dir('./static/lastPicture')
#     time = datetime.now()
#     cv2.imwrite(f'./static/lastPicture/lastPicture_{time}.jpeg', img)
#     img = loadImage(f'./static/lastPicture/lastPicture_{time}.jpeg')
#     return 'vigny'

@app.route('/names')
def get_names():
    return jsonify(listdir('./static/FaceRecognition/'))


@app.route('/save_picture/<name>')
def save_picture(name=None):
    if name is None:
        abort(500)
    dataTransfer('./static/lastPicture/', name, './static/FaceRecognition/')
    return f'okay c\'est fait chef {name}'

@app.route('/get_pictures_urls/<name>')
def get_pictires_urls(name=None):
    if name is None:
        abort(500)
    URLs = listFiles(f'./static/FaceRecognition/{name}')
    return jsonify(URLs)

@app.route('/last_picture')
def get_last_pic_urls():
    return listFiles('./static/lastPicture')[0]