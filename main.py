# Imports

import cv2
import numpy as np
import matplotlib.pyplot as plt
import gng

# Pre Images Processing

img = cv2.imread('astro.png') # Load images
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Convert to gray scale
img = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT) # Blure images for less details
ret, img = cv2.threshold(img,150,255,cv2.THRESH_BINARY) # Binarization threshold

# Creating dataset

data = [] # create array to hold coordinates

for y in range(img.shape[0]): # Loop through the imgae rows
    for x in range(img.shape[1]): # Loop through the images collums
        if img[x,y] == 0: # Chech if the pixels is black
            data.append((y,-x)) # Save coordinate to dataset

plt.scatter(*np.array(data).T)
plt.show()

# cv2.imshow('image',img) # Show images
# cv2.waitKey(0) # Wait for key press
# cv2.destroyAllWindows() # Destroy windows