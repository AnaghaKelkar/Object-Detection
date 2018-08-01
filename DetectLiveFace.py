#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 18:59:48 2018

@author: anaghakelkar
"""

import cv2

cap = cv2.VideoCapture(0)

# create the haar cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while(True):
    # capture frame-by-frame
    ret, frame = cap.read()
    
    # our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in an image
    faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30)
		#flags = cv2.CV_HAAR_SCALE_IMAGE
    )

    print("Found {0} faces!".format(len(faces)))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# when everything is done, release the capture
cap.release()
cv2.destroyAllWindows()

    