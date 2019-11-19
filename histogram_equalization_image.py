import numpy as np
import cv2
from matplotlib import pyplot as plt

# read an image from the file (in colour)
img = cv2.imread('./peppers.png',0)

# check if it has loaded
if not img is None:
    # histogram equalization
    equ = cv2.equalizeHist(img)

    # create plot
    plt.subplot(1,2,1),plt.imshow(img, cmap = 'gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(1,2,2),plt.imshow(equ, cmap = 'gray')
    plt.title('Histogram Equalization'), plt.xticks([]), plt.yticks([])

    # show plot
    plt.show()

else:
    print("No image file successfully loaded.")
