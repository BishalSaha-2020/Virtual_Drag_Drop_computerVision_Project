import cv2
import cv2.gapi.streaming
import cvzone
from cvzone.HandTrackingModule import HandDetector
cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1600)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1200)
detector=HandDetector(detectionCon=0.7)
img1=cv2.imread("tgr.PNG",cv2.IMREAD_UNCHANGED)

ox,oy=0,0

while True:
    success, img = cap.read();
    img = cv2.flip(img, 1)
    hands,img=detector.findHands(img,flipType=False)


    if hands:
        lmList=hands[0]['lmList']

        length,info,img= detector.findDistance(lmList[8],lmList[12],img)
        if length<60:
            cursor=lmList[8]



            if ox<cursor[0]<ox+w and oy<cursor[1]<oy+h:
                ox,oy=cursor[0]-w//2,cursor[1]-h//2

    try:
    #Draw for JPG images

        h,w,_=img1.shape


    #draw for png
        img=cvzone.overlayPNG(img,img1,[ox,oy])

    except:
        pass


    cv2.imshow("img",img)

    cv2.waitKey(1)