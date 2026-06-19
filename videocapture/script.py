import numpy as np
import cv2 as opencv

capture = opencv.VideoCapture(1) # Enter a filename or a number corresponding to the number of cameras one is connected to

while True: # Loops indefinitely
    ret, frame = capture.read()

    width = int(capture.get(3))
    height = int(capture.get(4))

    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = opencv.resize(frame, (0, 0), fx=0.5, fy=0.5)

    image[:height // 2, :width // 2] = smaller_frame # top-left
    image[height // 2:, :width // 2] = smaller_frame # bottom-left
    image[:height // 2, width // 2:] = smaller_frame # top-right
    image[height // 2:, width // 2:] = smaller_frame # bottom-right

    opencv.imshow("Frame", image)

    if opencv.waitKey(1) == ord('q'):
        break

capture.release()
opencv.destroyAllWindows()
