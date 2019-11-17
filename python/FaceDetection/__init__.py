# TODO: speed comparisons of both classifiers
import time
from os import listdir
from os.path import isfile, join

import cv2
import matplotlib.pyplot as plt

from miscelaneous import convertToGray

# Global variables for the classifier's detection
SCALE_FACTOR = 1.1
MIN_NEIGHBORS = 6

#load cascade classifier training file for haarcascade
haar_face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')

def getFacesHaar(RGB_Img, classifier=haar_face_cascade):
    """
    returns the list of faces as arrays of RGB imgs
    """
    gray_img = convertToGray(RGB_Img)
    #let's detect multiscale (some images may be closer to camera than others) images
    faces = classifier.detectMultiScale(gray_img, scaleFactor=SCALE_FACTOR, minNeighbors=MIN_NEIGHBORS)
    faces_img = []
    for (x, y, w, h) in faces:
        faces_img.append(RGB_Img[y:y+h, x:x+w])
    return faces_img
