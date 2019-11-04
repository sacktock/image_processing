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

img1 = cv2.imread('logoMask.png', cv2.IMREAD_COLOR);
img2 = cv2.imread('peppers.png', cv2.IMREAD_COLOR);
img3 = cv2.imread('duLogo.png', cv2.IMREAD_COLOR);

# check it has loaded

if not img1 is None and not img2 is None and not img3 is None:

    # performing logical inversion (see manual entry for bitwise_not()

    h = img2.shape[0]
    w = img2.shape[1]
    
    for y in range(0,h):
        for x in range(0,h):
            if y < img3.shape[0] and x < img3.shape[1]:
                if (img1[y,x][0] != 255) or (img1[y,x][1] != 255) or (img1[y,x][2] != 255):
                    img2[y,x] = img3[y,x]
            

    # write inverted image to file

    cv2.imwrite('imprint.png', img2);

else:
    print("No image file successfully loaded.")

#####################################################################


