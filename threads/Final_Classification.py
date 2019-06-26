import cv2
import numpy as np
font = cv2.FONT_HERSHEY_SIMPLEX
global count
count=0
def dark_brown(img):
    masked=cv2.inRange(img,(0,0,47),(126,76,167))
    dB=cv2.bitwise_and(img,img,mask=masked)
    _, contours, _ = cv2.findContours(masked,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    dB=cv2.cvtColor(masked,cv2.COLOR_GRAY2RGB)
    if(len(contours)>0):
        cv2.drawContours(dB,contours,-1, (204,114,18), 1)
        area=0
        for i in contours:

            if area<(cv2.contourArea(i)+0.1):
                area=cv2.contourArea(i)
                cnt=i
            M=cv2.moments(cnt)
            cx = int(M['m10']/(M['m00']+0.05))
            cy = int(M['m01']/(M['m00']+0.05))
        cv2.putText(dB,'Dark brown soil',(cx,cy), font, 0.5,(255,255,255),1,cv2.LINE_AA)
    cv2.imshow('Dark brown soil',cv2.cvtColor(dB,cv2.COLOR_RGB2BGR))
    cv2.imshow('Actual feed',img)



def gray(img):
    global count
    masked=cv2.inRange(img,(95,36,74),(107,110,172))
    dB=cv2.bitwise_and(img,img,mask=masked)
    #cv2.imshow('dBxxx',dBx)
    #cv2.imshow('img',img)
    _,contours, _ = cv2.findContours(masked,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    dB=cv2.cvtColor(masked,cv2.COLOR_GRAY2RGB)
    if(len(contours)>0):
        cv2.drawContours(dB,contours,-1, (137,132,132), 1)
        area=0
        for i in contours:
            if area<(cv2.contourArea(i)+0.1):
                area=cv2.contourArea(i)
                cnt=i
            M=cv2.moments(cnt)
            cx = int(M['m10']/(M['m00']+0.01))
            cy = int(M['m01']/(M['m00']+0.01))
        cv2.putText(dB,'Gray White soil',(cx,cy), font, 0.5,(255,255,255),1,cv2.LINE_AA)
    cv2.imshow('Gray white soil',dB)
    cv2.imshow('Actual feed',img)
    cv2.imwrite('gray'+str(count)+'.png',dB)
    count=count+1



def mountains(img):
    masked=cv2.inRange(img,(5,8,160),(36,39,171))
    dB=cv2.bitwise_and(img,img,mask=masked)
    #cv2.imshow('dBxxx',dBx)
    #cv2.imshow('img',img)
    _, contours, _ = cv2.findContours(masked,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    xcraj=cv2.cvtColor(masked,cv2.COLOR_GRAY2RGB)
    if(len(contours)>0):
        cv2.drawContours(dB,contours,-1, (137,132,132), 1)
        area=0
        for i in contours:
            if area<(cv2.contourArea(i)+0.1):
                area=cv2.contourArea(i)
                cnt=i
            M=cv2.moments(cnt)
            cx = int(M['m10']/(M['m00']+0.01))
            cy = int(M['m01']/(M['m00']+0.01))
        cv2.putText(dB,'Mountains',(cx,cy), font, 0.5,(255,255,255),1,cv2.LINE_AA)
    cv2.imshow('Mountains',dB)
    cv2.imshow('Actual feed',img)


def light_soil(img):
    masked=cv2.inRange(img,(0,5,111),(162,22,150))
    dB=cv2.bitwise_and(img,img,mask=masked)
    _, contours, _ = cv2.findContours(masked,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    xcraj=cv2.cvtColor(masked,cv2.COLOR_GRAY2RGB)
    if(len(contours)>0):
        cv2.drawContours(dB,contours,-1, (137,132,132), 1)
        area=0
        for i in contours:
            if area<(cv2.contourArea(i)+0.1):
                area=cv2.contourArea(i)
                cnt=i
            M=cv2.moments(cnt)
            cx = int(M['m10']/(M['m00']+0.01))
            cy = int(M['m01']/(M['m00']+0.01))
        cv2.putText(dB,'Light soil',(cx,cy), font, 0.5,(255,255,255),1,cv2.LINE_AA)
    cv2.imshow('Light soil',dB)
    cv2.imshow('Actual feed',img)


def water_bodies(img):
    masked=cv2.inRange(img,(94,40,94),(105,66,131))
    dB=cv2.bitwise_and(img,img,mask=masked)
    _, contours, _ = cv2.findContours(masked,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    xcraj=cv2.cvtColor(masked,cv2.COLOR_GRAY2RGB)
    if(len(contours)>0):
        cv2.drawContours(dB,contours,-1, (137,132,132), 1)
        area=0
        cx=cy=10
        for i in contours:
            if area<cv2.contourArea(i):
                area=cv2.contourArea(i)
                cnt=i
                M=cv2.moments(cnt)
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
        cv2.putText(dB,'Water bodies',(cx,cy), font, 0.5,(255,255,255),1,cv2.LINE_AA)
    cv2.imshow('Water bodies',dB)
    cv2.imshow('Actual feed',img)


this_I=0
cam=cv2.VideoCapture('curiosity.mp4')
ret=True
wb=ls=ds=m=g=0
#1=dark2=gray3=mountains4=light soil5=water bodies
while ret:
    k=cv2.waitKey(1)
    if k and 0xFF == ord('q'):
        break

    ret,img=cam.read()
    img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
    if k==ord('m'):
        this_I=int(input('Enter the mode'))
    if(this_I==1):
        dark_brown(cv2.cvtColor(img,cv2.COLOR_BGR2HSV))
    elif(this_I==2):
        gray(cv2.cvtColor(img,cv2.COLOR_BGR2HSV))
    elif(this_I==3):
        mountains(cv2.cvtColor(img,cv2.COLOR_BGR2HSV))
    elif(this_I==4):
        light_soil(cv2.cvtColor(img,cv2.COLOR_BGR2HSV))
    elif(this_I==5):
        water_bodies(cv2.cvtColor(img,cv2.COLOR_BGR2HSV))
    else:
        pass
    cv2.imshow('img',img)
#cv2.waitKey(0)
    
