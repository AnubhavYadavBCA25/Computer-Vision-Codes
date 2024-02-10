import numpy as np
import cv2

##### VARIABLES #####

# True while mouse button down, False while mouse button up
drawing = False
ix = -1
iy = -1

#### FUNCTION #######

def draw_circle(event,x,y,flags,params):
    
    global ix,iy,drawing
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
    
##### SHOWING IMAGE WITH OPENCV ######

# BLACK IMAGE#
img = np.zeros(shape=(512,512,3),dtype=np.int8)

cv2.namedWindow(winname='my_drawing')

cv2.setMouseCallback('my_drawing',draw_circle)

while True:
    
    cv2.imshow('my_drawing',img)
    
    if cv2.waitKey(1) & 0xFF == 27:
        
        break
        
cv2.destroyAllWindows()