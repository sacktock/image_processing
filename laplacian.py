#####################################################################

# Example : save an image from file (and invert it)

# Author : Toby Breckon, toby.breckon@durham.ac.uk

# Copyright (c) 2015 School of Engineering & Computing Science,
#                    Durham University, UK
# License : LGPL - http://www.gnu.org/licenses/lgpl.html

#####################################################################

import numpy as np
import cv2
import copy

#####################################################################

# read an image from the specified file (in colour)

img = cv2.imread('peppers.png', cv2.IMREAD_COLOR);

# check it has loaded

if not img is None:
    windowName = "filtered img"

    img = cv2.GaussianBlur(img,(3,3),0)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dst = cv2.Laplacian(img_gray, cv2.CV_16S, ksize=3)
    abs_dst = cv2.convertScaleAbs(dst)



    # write inverted image to file
    cv2.imwrite('laplacian_p.png', abs_dst)
    cv2.imshow(windowName, abs_dst)

else:
    print("No image file successfully loaded.")

#####################################################################


