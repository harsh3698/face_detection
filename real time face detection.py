# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 12:48:38 2019

@author: harsh
"""

import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
camera = cv2.VideoCapture(0)
img_counter = 0
i = 0
while True:
    ret, image = camera.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    k = cv2.waitKey(1)
    faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor = 1.5,
            minNeighbors = 5,
            minSize = (30, 30),
            flags = cv2.CASCADE_SCALE_IMAGE
            )
    cv2.rectangle(image, (200, 120), (440,360), (255, 255, 255), 2)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x,y), (x+w, y+h), (255, 255, 255), 2)
    cv2.imshow('FaceDetection', image)
    if k%256 == 27:
        break
    elif 210<x<240 and 130<y<160 and 400<x+w<430 and 320<y+h<350:
        if i == 1:
            break
        else:
            ima = "{}.jpg".format(i)
            cv2.imwrite(ima, image[y:y+h, x:x+w])
            img_counter += 1
            i+=1
camera.release()
cv2.destroyAllWindows()