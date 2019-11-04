import numpy as np
import cv2

# define video capture object
cap = cv2.VideoCapture(0)

# check if camera opened successfully
if (cap.isOpened()==False):
    print("No camera successfully loaded.")

# loop
while(cap.isOpened()):
    # capture frame-by-frame
    ret, frame = cap.read()

    # if not empty frame
    if ret==True:
        # our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # display the resulting frame
        cv2.imshow('frame', gray)

    # press Q on keyboard to  exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# when everything done, release the capture
cap.release()

# close all windows
cv2.destroyAllWindows()
