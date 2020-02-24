# Imports

import cv2
import numpy as np
import random

# Pre Images Processing

img = cv2.imread('roger.png') # Load images
img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Convert to gray scale
img_g = cv2.GaussianBlur(img_g, (5,5), cv2.BORDER_DEFAULT) # Blure images for less details
ret, img_g = cv2.threshold(img_g, 125, 255, cv2.THRESH_BINARY) # Binarization threshold

print('shape[0] is {}, shape[1] is {}'.format(img_g.shape[0], img_g.shape[1]))

# Creating dataset

data = [] # Array for holding our pixel coords

for rows in range(img_g.shape[0]): # Loop throguh the rows
    for cols in range(img_g.shape[1]): # Loop through the cols
        if img_g.item(rows, cols) == 0: # Chech if the pixel is black
            data.append((rows, cols)) # Save it to the data array

for i in range(100):
    index = random.randint(0, len(data))
    temp =  img[data[index]]
    temp = tuple(temp)
    img[data[index]] = (0, 0, 255)
    cv2.imshow('image',img) # Show binary images
    cv2.imshow('gray',img_g) # Show binary images
    cv2.waitKey(100) # Wait for key press
    img[data[index]] = temp

# cv2.imshow('image0',img) # Show original images
# cv2.imshow('image',img_g) # Show binary images
# cv2.waitKey(0) # Wait for key press
# cv2.destroyAllWindows() # Destroy windows