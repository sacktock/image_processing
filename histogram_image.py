import numpy as np
import cv2
from matplotlib import pyplot as plt

# read an image from the file (in colour)
img = cv2.imread('./peppers.png', 0)

# check if it has loaded
if not img is None:
    # histogram
    hist, bins = np.histogram(img.flatten(), 256, [0,256])

    # normalized histogram
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()

    # create plot
    plt.subplot(2,1,1),plt.imshow(img, cmap = 'gray')
    plt.title('Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,1,2)
    plt.plot(cdf_normalized, color = 'b')
    plt.hist(img.flatten(),256,[0,256], color = 'r')
    plt.xlim([0,256])
    plt.legend(('cdf', 'histogram'), loc = 'upper left')
    plt.title('Histogram')

    # show plot
    plt.show()

else:
    print("No image file successfully loaded.")
