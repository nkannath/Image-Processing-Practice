# merge channel to enhace colors

import cv2
import numpy as np

filename = raw_input("Enter Filename: ")
img = cv2.imread(filename)

g,b,r = cv2.split(img)
image = cv2.merge((g, b, r))

image[:,:,2] = 0


gbr_img = cv2.merge((g, b, r))
rbr_img = cv2.merge((r, b, r))
rgr_img = cv2.merge((r, g, r))

b_img = cv2.merge((b, b, b))


toWrite = raw_input("Enter name of file to save: ")
cv2.imwrite(toWrite, image)

cv2.imshow('image', image)
#cv2.imshow('blue', b_img)
cv2.waitKey()