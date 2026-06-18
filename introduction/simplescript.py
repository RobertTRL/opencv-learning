# Basic opencv tutorial

import cv2 # importing the library
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
img = cv2.imread(os.path.join(base_dir, "../assets/setup.jpg"), -1)

"""
cv2.IMREAD_COLOR / 1 : Loads a color image. Any transparency of image will be neglected. It is the default flag.
cv2.IMREAD_GRAYSCALE / 0 : Loads image in grayscale mode
cv2.IMREAD_UNCHANGED / -1 : Loads image as such including alpha channel
"""

cv2.imshow("Image", img ) # displaying the image
cv2.waitKey(0)
cv2.destroyAllWindows()