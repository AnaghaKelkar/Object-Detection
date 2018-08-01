import sys
import cv2
import numpy as np
import os
from os import listdir
from os.path import isfile, join

def detectWink(frame, location, ROI, cascade):
    eyes = cascade.detectMultiScale(ROI, 1.27 ,7 , 0|cv2.CASCADE_SCALE_IMAGE, (10, 10))
    if len(eyes) == 0:
         eyes = cascade.detectMultiScale(ROI, 1.02 , 3 , 0|cv2.CASCADE_SCALE_IMAGE, (10, 10))
    for e in eyes:
        e[0] += location[0]
        e[1] += location[1]
        x, y, w, h = e[0], e[1], e[2], e[3]

        cv2.rectangle(frame, (x,y), (x+w,y+h), (0, 0, 255), 2)
    return len(eyes) == 1
    
def detect(frame, face_cascade, eye_cascade):
    scaleFactor = 1.25 
    minNeighbors = 3 
    flag = 0|cv2.CASCADE_SCALE_IMAGE 
    minSize = (30,30 ) 
    faces = face_cascade.detectMultiScale(
        frame,
        scaleFactor,
        minNeighbors,
        flag,
        minSize)
    detected = 0
    for f in faces:
        x, y, w, h = f[0], f[1], f[2], f[3]
        faceROI = frame[y:y+h, x:x+w]
        if detectWink(frame, (x, y), faceROI, eye_cascade):
            detected += 1
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255, 0, 0), 2)
        else:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0, 255, 0), 2)
    return detected
    
def runonFolder(face_cascade, eye_cascade, folder):
    if folder[-1] != "/":
        folder = folder + "/"
    files = [join(folder, f) for f in listdir(folder) if isfile(join(folder, f))]
    
    windowName = None
    totalCount = 0
    for f in files:
        img = cv2.imread(f, 1)
        if type(img) is np.ndarray:
            icnt = detect(img, face_cascade, eye_cascade)
            totalCount += icnt
            if windowName != None:
                cv2.destroyWindow(windowName)
            windowName = f
            cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)
            cv2.imshow(windowName, img)
            cv2.waitKey(2000)
    return totalCount

def runonVideo(face_cascade, eye_cascade):
    videocapture = cv2.VideoCapture(0)
    if not videocapture.isOpened():
        print("Can't open video default camera!")
        exit()
    windowName = "Live Video"
    showlive = True
    while(showlive):
        ret, frame = videocapture.read()
        if not ret:
            print("Can't capture frame")
            exit()
        cnt = detect(frame, face_cascade, eye_cascade)
        print("Detections: {0}".format(cnt))
        cv2.imshow(windowName, frame)
        if cv2.waitKey(30)>=0:
            showlive = False
    videocapture.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    if len(sys.argv)!=1 and len(sys.argv)!=2:
        print(sys.argv[0] + " :got " + len(sys.argv)-1 + " arguments. Expecting 0 or 1 : [image-folder]")
        exit()
    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_eye.xml')
    
    if len(sys.argv)==2:
        folderName = sys.argv[1]
        detections = runonFolder(face_cascade, eye_cascade, folderName)
        print("Total of ", detections, " detections")
    else:
        runonVideo(face_cascade, eye_cascade)