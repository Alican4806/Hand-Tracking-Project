import cv2 as cv
import mediapipe as mp
import time
import HandTrackingModule as htm




pTime = 0 # It is previous time and it was 0 at started
cTime = 0 # It is current time and it was 0 at started
cap = cv.VideoCapture(0) # we wrote 0 to use my laptop's camera. If we want to use another camera on the usb, we have to write 1. 

detector = htm.handDetector()  # we created object that called detector.

while True:
        success,img = cap.read() # 'success' variable is boolean and we got video from the my laptop with cap.read()
        img =detector.findHands(img,draw= False) # we didn't give another values because it is given by default
        # We prevent drawing line by giving false 
        
        lmList = detector.findPositon(img,draw = False) # It has more arguments so we define like draw = False
        if len(lmList)!= 0: # if this state is provided, it will print it
            print(lmList[4]) # We is written fourth value of the list

      
        cTime = time.time() # we got current time as cTime
    
        fps = 1/ (cTime-pTime) # We found fps
    
        pTime = cTime # cTime assigned as previous time 
    
        cv.putText(img,str(int(fps)),(10,100),cv.FONT_HERSHEY_SIMPLEX,3,(255,0,255),3) # we write fps value to the screen.
    
        cv.imshow("Alican",img)
        if cv.waitKey(30) & 0xFF == ord('q'): # We used function that is 0xFF == ord('q') to close the laptop's camera 
            break        