import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #img2=cv2.rotate(frame, frame, cv2.ROTATE_90_CLOCKWISE)
    
    img2 = cv2.rotate(frame, rotateCode=cv2.ROTATE_90_CLOCKWISE)

    #img2=cv2.flip(frame,1)
    
    cv2.imshow('flipped video',img2)
    # Display the resulting frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()