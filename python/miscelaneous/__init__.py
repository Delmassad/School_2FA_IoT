from os import listdir, remove
from os.path import isfile, join
import cv2

def listFiles(path):
    return [f for f in listdir(path) if isfile(join(path, f))]

def listDir(path):
    return [f for f in listdir(path) if not isfile(join(path, f))]

def loadImage(path):
    #load image
    return cv2.imread(path)

def convertToGray(img):
    """
    convert the test image to gray image as opencv face detector expects gray images
    """
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray_img

def saveResult(img, faces, path):
    #go over list of faces and draw them as rectangles on original colored
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imwrite(path, img)

def empty_dir(dir_path):
    files = listFiles(dir_path)
    for file in files:
        remove(f'{dir_path}/{file}')
