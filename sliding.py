import cv2
import numpy as np
from matplotlib import pyplot as plot
import imutils


template = cv2.imread('template.jpg')
hsvTemplate = cv2.cvtColor(template, cv2.COLOR_BGR2HSV)
templateHist = cv2.calcHist([hsvTemplate], [0,1], None, [180,256], [0,180,0,256])

#filename = raw_input("Enter image: ")
img = cv2.imread('opencv_frame_4.png')
orig = img.copy()
hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

previousSlides = []

rows = img.shape[0]
columns = img.shape[1]

selection = [0,rows/2, 0,columns/2]

horSlideDist = (columns/2)/10
verSlideDist = (rows/2)/10

def defineQuads(image, quad):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    rows = img.shape[0]
    columns = img.shape[1]
    q1 = img[0:rows/2, columns/2:columns]
    q2 = img[0:rows/2, 0:columns/2]
    q3 = img[rows/2:rows, 0:columns/2]
    q4 = img[rows/2:rows, columns/2:columns]
    if quad == 1:
        selection = [0, rows/2, columns/2, columns]
        return q1
    elif quad == 2:
        selection = [0,rows/2, 0,columns/2]
        return q2
    elif quad == 3:
        selection = [rows/2, rows, 0,columns/2]
        return q3
    elif quad == 4:
        selection = [rows/2,rows, columns/2,columns]
        return q4

def slide(selection, direction, amount, original):
    y1 = selection[0]
    y2 = selection[1]
    x1 = selection[2]
    x2 = selection[3]
    image = original[y1:y2, x1:x2]
    original = original.copy()
    if direction == 'right' or 'left':
        timesSlide = amount * horSlideDist
        if direction == 'right':
            slidImage = original[y1:y2, x1+timesSlide:x2+timesSlide]
        elif direction == 'left':
            timesSlide = -1*timesSlide
            slidImage = original[y1:y2, x1+timesSlide:x2+timesSlide]
    elif direction == 'up' or 'down':
        timesSlide = amount * verSlideDist
        if direction == 'up':
            timesSlide = -1*timesSlide
            slidImage = original[y1+timesSlide:y2+timesSlide, x1:x2]
        elif direction == 'down':
            slidImage = original[y1+timesSlide:y2+timesSlide, x1:x2]
    return slidImage

def getAmount():
    amount = int(raw_input("Enter how many slides are to occur: "))
    return amount

def templateCompare(histo1):
    histo = cv2.calcHist([histo1], [0,1], None, [180,256], [0,180,0,256])
    histo2 = templateHist
    correlation = cv2.compareHist(templateHist, histo, cv2.HISTCMP_INTERSECT)
    return correlation


def previous():
    direction = determineDirection()
    amount = getAmount()
    i = 1
    while i <= amount:
        previousSlides.append(slide(selection, direction, i, img))
        i += 1

def determineDirection():
    direction = str(raw_input("Enter direction to slide: "))
    return direction

previous()



while True:
    cv2.imshow('original', orig)
    cv2.imshow('q2', defineQuads(img, 2))

    print len(previousSlides)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
