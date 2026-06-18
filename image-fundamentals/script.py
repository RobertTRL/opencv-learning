# Images in the computer are a matrix
# OpenCV uses NumPy arrays
# A standard coloured image contains 3 chaneels, blue, green and red
# When an image is read, it returns a tuple containing 3 values -> columns, rows and channels

import cv2 as opencv
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
img = opencv.imread(os.path.join(base_dir, "../assets/setup.jpg"), 1)

section = img[500:700, 600:900] # extract the specific section
img[100:300, 600: 900] = section # write the section onto the image

opencv.imshow("Image", img)
opencv.waitKey(0)
opencv.destroyAllWindows()
