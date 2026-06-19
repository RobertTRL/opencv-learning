import numpy as np
import cv2 as opencv

capture = opencv.VideoCapture(1)

while True:
    ret, frame = capture.read()

    width = int(capture.get(3))
    height = int(capture.get(4))

    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = opencv.resize(frame, (0, 0), fx=0.5, fy=0.5)

    opencv.imshow("Frame", image)

    if opencv.waitKey(1) == ord('q'):
        break

capture.release()
opencv.destroyAllWindows()