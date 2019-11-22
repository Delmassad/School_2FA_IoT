# TODO: speed comparisons of both classifiers
import time
from os import listdir, makedirs
from os.path import isfile, join, isdir
from miscelaneous import listFiles, listDir

import cv2
import matplotlib.pyplot as plt

from miscelaneous import convertToGray

# Global variables for the classifier's detection
SCALE_FACTOR = 1.1
MIN_NEIGHBORS = 6

#load cascade classifier training file for haarcascade
haar_face_cascade = cv2.CascadeClassifier('./FaceDetection/haarcascade_frontalface_alt.xml')

def getFacesHaar(RGB_Img, classifier=haar_face_cascade):
    """
    returns the list of faces as arrays of RGB imgs
    """
    gray_img = convertToGray(RGB_Img)
    print(len(gray_img))
    #let's detect multiscale (some images may be closer to camera than others) images
    faces = classifier.detectMultiScale(gray_img, scaleFactor=SCALE_FACTOR, minNeighbors=MIN_NEIGHBORS)
    faces_img = []
    for (x, y, w, h) in faces:
        faces_img.append(RGB_Img[y:y+h, x:x+w])
    return faces_img

def dataTransfer(sourcePath, username, destPath):
    rawPhotosPaths = listFiles(sourcePath)
    cropped_files = []
    for photo in rawPhotosPaths:
        path = f'{sourcePath}{photo}'
        print(path)
        img = getFacesHaar(cv2.imread(path))
        if img:
            cropped_files.append(*img)
    for index, img in enumerate(cropped_files):
        destPath_f = f'{destPath}{username}/face_{index}.jpg'
        print(destPath_f)
        if not isdir(f'{destPath}{username}'):
            makedirs(f'{destPath}{username}')
        cv2.imwrite(destPath_f, img)
