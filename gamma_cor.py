#####################################################################

# Example : save an image from file (and invert it)

# Author : Toby Breckon, toby.breckon@durham.ac.uk

# Copyright (c) 2015 School of Engineering & Computing Science,
#                    Durham University, UK
# License : LGPL - http://www.gnu.org/licenses/lgpl.html

#####################################################################

import numpy as np
import cv2


def gamma(image, g):
    c = 255 ^ g

    h = image.shape[0]
    w = image.shape[1]

    for y in range(0,h):
        for x in range(0,w):
            image[y,x][0] = (255*(image[y,x][0]^g)) // c
            image[y,x][1] = (255*(image[y,x][1]^g)) // c
            image[y,x][2] = (255*(image[y,x][2]^g)) // c

    return image
#####################################################################

# read an image from the specified file (in colour)

img = cv2.imread('peppers.png', cv2.IMREAD_COLOR);

# check it has loaded

if not img is None:

    # performing logical inversion (see manual entry for bitwise_not()

    gammaImg = gamma(img, 5);

    # write inverted image to file

    cv2.imwrite('gamma.jpg', gammaImg);

else:
    print("No image file successfully loaded.")

#####################################################################


