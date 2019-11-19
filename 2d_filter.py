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
    # performing logical inversion (see manual entry for bitwise_not()


    # write inverted image to file
    mask = np.ones((5,5),np.float32)/25
    filtered_img = cv2.filter2D(img,-1,mask)
    cv2.imwrite('filtered_img.png', filtered_img)
    cv2.imshow(windowName, filtered_img)

else:
    print("No image file successfully loaded.")

#####################################################################


