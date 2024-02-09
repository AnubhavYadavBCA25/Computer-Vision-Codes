import cv2

img = cv2.imread('C://Users/anu52/Downloads/Computer-Vision-with-Python/Computer-Vision-with-Python/DATA/00-puppy.jpg')

while True:
    
    cv2.imshow('Puppy', img)
    
    # If we'hv waited at least 1 mm AND we pressed the Esc
    if cv2.waitKey(1) & 0xFF == 27:
        
        break
        
cv2.destroyAllWindows()

# Run your .py script file(mypuppy.py) on terminal