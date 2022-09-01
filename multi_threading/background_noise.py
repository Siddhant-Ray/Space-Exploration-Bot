import cv2
import numpy as np
cap=cv2.VideoCapture(0)
fgbg=cv2.createBackgroundSubtractorMOG2()

while True:
    _,frame=cap.read()
    fgmask=fgbg.apply(frame)
    cv2.imshow('orignal',frame)
    cv2.imshow('fg',fgmask)
    k=cv2.waitKey(1)
    if k & 0xFF==ord('q'):
        break
