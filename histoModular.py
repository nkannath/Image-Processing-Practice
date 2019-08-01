import cv2
import numpy as np
from matplotlib import pyplot as plot
import imutils

template = cv2.imread('picTemplate.png')
hsvTemplate = cv2.cvtColor(template, cv2.COLOR_BGR2HSV)
templateHist = cv2.calcHist([hsvTemplate], [0,1], None, [180,256], [0,180,0,256])


filename = raw_input("Enter image: ")
img = cv2.imread(filename)
orig = img.copy()
hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

Ranking = []


def defineQuads(image, quad):
    img = image
    rows = img.shape[0]
    columns = img.shape[1]
    q1 = img[0:rows/2, columns/2:columns]
    q2 = img[0:rows/2, 0:columns/2]
    q3 = img[rows/2:rows, 0:columns/2]
    q4 = img[rows/2:rows, columns/2:columns]
    if quad == 1:
        return q1
    elif quad == 2:
        return q2
    elif quad == 3:
        return q3
    elif quad == 4:
        return q4

def conCompHisto(image):
    img = image
    hist1 = cv2.calcHist([defineQuads(img, 1)], [0,1], None, [180,256], [0,180,0,256])
    hist2 = cv2.calcHist([defineQuads(img, 2)], [0,1], None, [180,256], [0,180,0,256])
    hist3 = cv2.calcHist([defineQuads(img, 3)], [0,1], None, [180,256], [0,180,0,256])
    hist4 = cv2.calcHist([defineQuads(img, 4)], [0,1], None, [180,256], [0,180,0,256])
    q1Comp = cv2.compareHist(templateHist, hist1, cv2.HISTCMP_CORREL)
    q2Comp = cv2.compareHist(templateHist, hist2, cv2.HISTCMP_CORREL)
    q3Comp = cv2.compareHist(templateHist, hist3, cv2.HISTCMP_CORREL)
    q4Comp = cv2.compareHist(templateHist, hist4, cv2.HISTCMP_CORREL)
    Ranking.append(q1Comp)
    Ranking.append(q2Comp)
    Ranking.append(q3Comp)
    Ranking.append(q4Comp)
    maxIndex = Ranking.index(max(Ranking))
    if maxIndex == 0:
        newBase = defineQuads(img, 1)
    elif maxIndex == 1:
        newBase = defineQuads(img, 2)
    elif maxIndex == 2:
        newBase = defineQuads(img, 3)
    elif maxIndex == 3:
        newBase = defineQuads(img, 4)
    del Ranking [:]
    return newBase

new = conCompHisto(img)
newnew = conCompHisto(new)
newnewnew = conCompHisto(newnew)

while True:
    cv2.imshow('original', orig)
    #cv2.imshow("q1", defineQuads(img, 1))
    cv2.imshow('new', new)
    cv2.imshow('newnew', newnew)
    cv2.imshow('newnewnew', newnewnew)


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
