# DRAWING A RECTANGLE ON LIVE CAMERA

import cv2

## CALLBACK FUNCTION RECTANGLE
def draw_rectangle(event,x,y,flags,param):
    
    global pt1,pt2,topLeft_clicked,bottomRight_clicked
    
    if event == cv2.EVENT_LBUTTONDOWN:
        
        # REST THE RECTANGLE (IT CHECKS IF THE REC THEIR)
        if topLeft_clicked == True and bottomRight_clicked == True:
            pt1 = (0,0)
            pt2 = (0,0)
            topLeft_clicked = False
            bottomRight_clicked = False
            
        if topLeft_clicked == False:
            pt1 = (x,y)
            topLeft_clicked = True
            
        elif bottomRight_clicked == False:
            pt2 = (x,y)
            bottomRight_clicked = True
    

## GLOBAL VARIABLES 
pt1 = (0,0)
pt2 = (0,0)
topLeft_clicked = False
bottomRight_clicked = False

## CONNECT TO THE CALLBACK
cap = cv2.VideoCapture(0)
cv2.namedWindow('Test')
cv2.setMouseCallback('Test',draw_rectangle)

while True:
    
    ret, frame = cap.read()
    
    # DRAWING ON THE FRAME BASED OFF THE GLOBAL VARIABLES
    if topLeft_clicked:
        cv2.circle(frame,center=pt1,radius=5,color=(0,0,255),thickness=-1)
    
    if topLeft_clicked and bottomRight_clicked:
        cv2.rectangle(frame,pt1,pt2,(0,0,255),3)
    
    cv2.imshow('Test',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()