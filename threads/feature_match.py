#Feature match
def main(file1,file2,file3):

    import numpy as np
    import cv2
    from matplotlib.pyplot import subplot,imshow,show,figure,pause
    frame=cv2.imread(file1)
    img1=cv2.imread(file2)
    img2=cv2.imread(file3)
    sift=cv2.xfeatures2d.SIFT_create()
    surf=cv2.xfeatures2d.SURF_create()
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(img1,None) #ORB COMPARISON
    kp = orb.detect(img1,None)
    kp, des = orb.compute(img1, kp)
    kp1,desc1=surf.detectAndCompute(img1,None) #sift/surf
    kp3,desc3=surf.detectAndCompute(img2,None) #sift/surf
    img=cv2.drawKeypoints(img1,kp1,img1)
    imgg=cv2.drawKeypoints(img2,kp3,img2)
    index_params = dict(algorithm = 0, trees = 5)
    search_params = dict(checks = 50)
    bf = cv2.BFMatcher()
    flann=cv2.FlannBasedMatcher(index_params,search_params)
    while True:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        kp2,desc2=surf.detectAndCompute(gray,None) #sift/surf
        #kpx, desx = orb.detectAndCompute(gray,None) #sift/surf
        #imgx = cv2.drawKeypoints(gray, kpx, None, color=(0,255,0), flags=0)
    #    matches0 = bf.knnMatch(des1,desc2, k=2)
        matches=flann.knnMatch(desc1,desc2,k=2)
        matches1=flann.knnMatch(desc3,desc2,k=2)
        good=[]
        good1=[]
        for m,n in matches:
            if m.distance<0.6*n.distance:
                good.append(m)
        img3=cv2.drawMatches(img,kp1,gray,kp2,good,None)
        #img3=cv2.drawMatches(imgg,kp3,gray,kp2,good,None)
        for m1,n1 in matches1:
            if m1.distance<0.6*n1.distance:
                good1.append(m1)
        img4=cv2.drawMatches(imgg,kp3,gray,kp2,good1,None)
        if (len(good1)>10):
            try:
                query_pts=np.float32([kp3[m.queryIdx].pt for m in good1]).reshape(-1,1,2)
                train_pts=np.float32([kp2[m.trainIdx].pt for m in good1]).reshape(-1,1,2)
                matrix,mask=cv2.findHomography(query_pts,train_pts,cv2.RANSAC,5.0)
                match_mask=mask.ravel().tolist()
                h,w=np.shape(cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY))
                pts=np.float32([[0,0],[0,h],[w,h],[w,0]]).reshape(-1,1,2)
                dst=cv2.perspectiveTransform(pts,matrix)
                homography=cv2.polylines(frame,[np.int32(dst)],True,(255,0,0))
                cv2.imshow('Rock homography',homography)
            except:
                pass
        if (len(good)>10):
            try:
                query_pts=np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1,1,2)
                train_pts=np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1,1,2)
                matrix,mask=cv2.findHomography(query_pts,train_pts,cv2.RANSAC,5.0)
                match_mask=mask.ravel().tolist()
                h,w=np.shape(cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY))
                pts=np.float32([[0,0],[0,h],[w,h],[w,0]]).reshape(-1,1,2)
                dst=cv2.perspectiveTransform(pts,matrix)
                homography=cv2.polylines(frame,[np.int32(dst)],True,(255,0,0))
                cv2.imshow('Mineral homography',homography)
            except:
                pass
        else:
            cv2.imshow('homography',gray)
        cv2.imshow('img3',img3)
        cv2.imshow('img4',img4)
        #cv2.imshow('imgx',imgx)
        if cv2.waitKey(1) & 0xFF== ord('q'):
            break
    
    cv2.destroyAllWindows()
    
