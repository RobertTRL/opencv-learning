import cv2 as opencv

capture = opencv.VideoCapture(0)

while True:
    ret, frame = capture.read()

    width = int(capture.get(3))
    height = int(capture.get(4))

    image = opencv.line(frame, (0, 0), (width, height), (0, 0, 255), 6)
    image = opencv.line(image, (0, height), (width, 0), (0, 0, 255), 6)

    opencv.imshow("Frame", image)

    if opencv.waitKey(1) == ord('q'):
        break

capture.release()
opencv.destroyAllWindows()