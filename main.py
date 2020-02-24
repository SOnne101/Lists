# Imports

import cv2
import numpy as np
import random

# Pre Images Processing

img = cv2.imread('roger.png') # Load images
img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Convert to gray scale
img_g = cv2.GaussianBlur(img_g, (5,5), cv2.BORDER_DEFAULT) # Blure images for less details
ret, img_g = cv2.threshold(img_g, 125, 255, cv2.THRESH_BINARY) # Binarization threshold

# Creating dataset

data = [] # Array for holding our pixel coords

for cols in range(img_g.shape[0]): 
    for rows in range(img_g.shape[1]):
        if img_g.item(cols, rows) == 0:
            data.append((cols, rows))

for i in range(100):
    index = random.randint(0, len(data))
    img_g[data[index]] = 127
    cv2.imshow('image',img_g) # Show binary images
    cv2.waitKey(100) # Wait for key press
    img_g[data[index]] == 0

# cv2.imshow('image0',img) # Show original images
# cv2.imshow('image',img_g) # Show binary images
# cv2.waitKey(0) # Wait for key press
# cv2.destroyAllWindows() # Destroy windows