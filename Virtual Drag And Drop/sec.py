import cv2

import cvzone
from cvzone.HandTrackingModule import HandDetector
cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1600)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1200)
detector=HandDetector(detectionCon=0.8)




while True:
    success, img = cap.read();
    img = cv2.flip(img, 1)
    hands,img=detector.findHands(img,flipType=False)











    cv2.imshow("img",img)

    cv2.waitKey(1)