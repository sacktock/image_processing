#####################################################################

# Example : save an image from file (and invert it)

# Author : Toby Breckon, toby.breckon@durham.ac.uk

# Copyright (c) 2015 School of Engineering & Computing Science,
#                    Durham University, UK
# License : LGPL - http://www.gnu.org/licenses/lgpl.html

#####################################################################

import numpy as np
import cv2
import random as rand

#####################################################################

# read an image from the specified file (in colour)

img = cv2.imread('peppers.png', cv2.IMREAD_COLOR);

# check it has loaded

def salt_pepper(image,p):

    h = image.shape[0]
    w = image.shape[1]

    for y in range(0,h):
        for x in range(0,w):
            f = rand.random()
            if f < p/2:
                image[y,x][0] = 255
                image[y,x][1] = 255
                image[y,x][2] = 255
            elif f < p:
                image[y,x][0] = 0
                image[y,x][1] = 0
                image[y,x][2] = 0
                
    return image
            
def median_filter(image,k):
    
    h = image.shape[0]
    w = image.shape[1]

    for y in range(0,h):
        for x in range(0,w):
            arr = np.array([])
            for i in range(-k,k+1):
                for j in range(-k,k+1):
                    if y + i in range(0,h):
                        if x + j in range(0,w):
                            arr.append(image[y,x])
        
    
if not img is None:

    # performing logical inversion (see manual entry for bitwise_not()

    newImg = salt_pepper(img, 0.1);

    # write inverted image to file

    cv2.imwrite('salt_pepper_noise.jpg', newImg);

else:
    print("No image file successfully loaded.")

#####################################################################


