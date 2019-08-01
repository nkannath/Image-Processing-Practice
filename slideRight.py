import cv2
import numpy as np
from matplotlib import pyplot as plot
import imutils
#import slide

template = cv2.imread('template.jpg')
hsvTemplate = cv2.cvtColor(template, cv2.COLOR_BGR2HSV)
templateHist = cv2.calcHist([hsvTemplate], [0,1], None, [180,256], [0,180,0,256])

filename = raw_input("Enter image: ")
img = cv2.imread(filename)
orig = img.copy()
hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

Ranking = []

rows = img.shape[0]
columns = img.shape[1]

selection = [0,rows/2, 0,columns/2]

horSlideDist = (columns/2)/10
verSlideDist = (rows/2)/10

def defineQuads(image, quad):
    img = image
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
    if direction == 'up' or 'down':
        timesSlide = amount * verSlideDist
        if direction == 'up':
            timesSlide = -1*timesSlide
            slidImage = original[y1+timesSlide:y2+timesSlide, x1:x2]
        elif direction == 'down':
            slidImage = original[y1+timesSlide:y2+timesSlide, x1:x2]
    return slidImage


def templateCompare(histo1):
    histo = cv2.calcHist([histo1], [0,1], None, [180,256], [0,180,0,256])
    histo2 = templateHist
    correlation = cv2.compareHist(templateHist, histo, cv2.HISTCMP_CORREL)
    return correlation

def getShape(image):
    rows = image.shape[0]
    columns = image.shape[1]
    shape = [rows, columns]
    return shape

right1 = slideRight(0, rows/2, 0, columns/2, 1, img)
right2 = slideRight(0, rows/2, 0, columns/2, 2, img)
right3 = slideRight(0, rows/2, 0, columns/2, 3, img)
right4 = slideRight(0, rows/2, 0, columns/2, 4, img)
right5 = slideRight(0, rows/2, 0, columns/2, 5, img)
right6 = slideRight(0, rows/2, 0, columns/2, 6, img)
right7 = slideRight(0, rows/2, 0, columns/2, 7, img)
right8 = slideRight(0, rows/2, 0, columns/2, 8, img)
right9 = slideRight(0, rows/2, 0, columns/2, 9, img)

first = templateCompare(defineQuads(img, 2))
second = templateCompare(right1)
third = templateCompare(right2)
fourth = templateCompare(right3)
fifth = templateCompare(right4)
sixth = templateCompare(right5)
seventh = templateCompare(right6)
eighth = templateCompare(right7)
ninth = templateCompare(right8)
tenth = templateCompare(right9)




q3 = defineQuads(img, 3)
q3R1 = slideRight(rows/2,rows, 0,columns/2, 1, img)
q3R2 = slideRight(rows/2,rows, 0,columns/2, 2, img)
q3R3 = slideRight(rows/2,rows, 0,columns/2, 3, img)
q3R4 = slideRight(rows/2,rows, 0,columns/2, 4, img)
q3R5 = slideRight(rows/2,rows, 0,columns/2, 5, img)


q31 = templateCompare(defineQuads(img, 3))
q32 = templateCompare(q3R1)
q33 = templateCompare(q3R2)
q34 = templateCompare(q3R3)
q35 = templateCompare(q3R4)
q36 = templateCompare(q3R5)



print "Q2 first: ", first
print "Q2 second: ", second
print "Q2 third: ", third
print "Q2 fourth: ", fourth
print "Q2 fifth: ", fifth
print "Q2 sixth: ", sixth
print "Q2 seventh: ", seventh
print "Q2 eighth: ", eighth
print "Q2 ninth: ", ninth
print "Q2 tenth: ", tenth


print "Q3 first: ", q31
print "Q3 second: ", q32
print "Q3 third: ", q33
print "Q3 fourth: ", q34
print "Q3 fifth: ", q35
print "Q3 sixth: ", q36


while True:
    cv2.imshow('original', orig)
    #cv2.imshow("q2", defineQuads(img, 2))

    cv2.imshow('first', defineQuads(img, 2))
    cv2.imshow('slide', slide(selection, 'down', 2, img))

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
