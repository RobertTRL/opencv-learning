import cv2 as opencv

capture = opencv.VideoCapture(1)

while True:
    ret, frame = capture.read()

    width = int(capture.get(3))
    height = int(capture.get(4))

    image = opencv.line(frame, (width // 2, ((height // 2) - 10)), (width // 2, ((height // 2) + 10)), (0, 0, 255), 2)
    image = opencv.line(image, (((width // 2) - 10), height // 2), (((width // 2) + 10), height // 2), (0, 0, 255), 2)
    image = opencv.rectangle(image, (width // 2, height // 2), (width, height), (255, 0, 0), 1)
    image = opencv.circle(image, (300,300), 100, (0, 255, 0, 0.3 ), -1)
    image = opencv.putText(image, "Robert is Great!", (200, height - 10), opencv.FONT_HERSHEY_SIMPLEX, 1 ,(255, 255, 255), 5, opencv.LINE_AA)

    opencv.imshow("Frame", image)

    if opencv.waitKey(1) == ord('q'):
        break

capture.release()
opencv.destroyAllWindows()