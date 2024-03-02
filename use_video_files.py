import cv2
#import time   'Python Module'

cap = cv2.VideoCapture('mycvvideo.mp4')

if cap.isOpened() == False:
    print('ERROR! FILE NOT FOUND OR CODEC IS WRONG!')
    
while cap.isOpened():
    
    ret,frame = cap.read()
    
    if ret == True:
        
        time.sleep(1/20)                   # 'HELP US TO WATCH VIDEO IN NORMAL SPEED'
        cv2.imshow('frame',frame)
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    
    else:
        break
        
cap.release()
cv2.destroyAllWindows()