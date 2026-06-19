import numpy as np
import cv2 as opencv

capture = opencv.VideoCapture(1) # Enter a filename or a number corresponding to the number of cameras one is connected to

while True: # Loops indefinitely
    ret, frame = capture.read()
    opencv.imshow("Frame", frame)

    if opencv.waitKey(1) == ord('q'):
        break

capture.release()
opencv.destroyAllWindows()
