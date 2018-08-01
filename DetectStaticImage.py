#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 17:11:48 2018

@author: anaghakelkar
"""

import cv2 # import OpenCV library
import sys

# Get user supplied values
imagePath = "Images/abba.png"
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)
# -- Now we create the cascade and initialize it with out face cascade. This loads the face
# cascade into memory. cascade is just an XML file that contains data to detect faces.

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# -- Here we read the image and convert it to grayscale, as many operations in OpenCV are 
# done in grayscale.

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor = 1.1,
    minNeighbors = 5,
    minSize = (30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
)

# -- detectMultiScale is a general function that detects objects.
# -- first option is grayscale image.
# -- second is scaleFactor -> since some faces may be closer to camera, they would appear
# bigger than the faces in the back. The scale factor compensates for this.
# -- minNeighbors -> how many objects are detected near the current one before it declares
# the face found. -- minSize -> size of each window.

# This function returns a list of rectangles in which it believes it found a face.

print "Found {0} faces!".format(len(faces))

# Draw a rectangle around the faces.
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(2000)
# -- we display the image and wait for the user to press a key.
