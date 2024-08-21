import cv2 as cv
import numpy as np


img = cv.imread('ideal.jpg')
img2 = cv.imread('sample6.jpg')
#cv.imshow('ideal gear',img)
#cv.imshow('sample gear',img2)

#apply grayscale to the images
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
#cv.imshow('grayscale ideal gear', gray_img)
#cv.imshow('grayscale sample gear', gray_img2)

#apply thresholding to the grayscale images to seprate the image from the background
ret, thresh1 = cv.threshold(gray_img, 127, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(gray_img2, 127, 255, cv.THRESH_BINARY)
#cv.imshow('threshold ideal gear', thresh1)
#cv.imshow('threshold sample gear', thresh2)


#make a xor bitwise operation on the thresholding images
bitwise_xor = cv.bitwise_xor(thresh1, thresh2)
cv.imshow('bitwise XOR', bitwise_xor)

#get the contours of the xor image
contours, hierarchy = cv.findContours(bitwise_xor, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

#draw the contours on the original images

for cnt in contours:
    #for every contour a different randomize color
    color = np.random.randint(0,255,(3)).tolist()
   # cv.drawContours(img, [cnt], 0, color, 3)
    #cv.drawContours(img2, [cnt], 0, (0,255,0), 3)
    

#cv.imshow('xor contours on ideal gear', img)
#cv.imshow('xor contours on sample gear', img2)

#print area
#for cnt in contours:
 #   area = cv.contourArea(cnt)
  #  print("Area: ", area)

#analyze the defects
brokenTeeth = 0
wornTeeth = 0
for cnt in contours:
    area = cv.contourArea(cnt)
    if area < 600 and area > 0:
        if 550 - area < 90:
            brokenTeeth += 1
        elif 10 < area < 490:
            wornTeeth += 1


print("Number of broken teeth: ", brokenTeeth)
print("Number of worn teeth: ", wornTeeth)


cv.waitKey(0)