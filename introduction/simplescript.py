# Basic opencv tutorial

import cv2 # importing the library
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
img = cv2.imread(os.path.join(base_dir, "../assets/setup.jpg"), 1)
# img = cv2.resize(img, (500, 500)) resizing the image, write fixed dimension in a tuple
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5) # resizes the image on a scale of 0.5


"""
cv2.IMREAD_COLOR / 1 : Loads a color image. Any transparency of image will be neglected. It is the default flag.
cv2.IMREAD_GRAYSCALE / 0 : Loads image in grayscale mode
cv2.IMREAD_UNCHANGED / -1 : Loads image as such including alpha channel
"""

cv2.imshow("Image", img ) # displaying the image
cv2.waitKey(0) # waits a specified amount of time in ms before executing the next line of code, 0 is infinite
cv2.destroyAllWindows() # destroys the window when any key is pressed