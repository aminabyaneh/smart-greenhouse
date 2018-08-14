# Importing libraries

import cv2
import numpy as np

# Defining color variables

green = 0
yellow = 0

# Loading images

img1 = cv2.imread('D:\Engineering\Projects\Dr.Bagheri\Smart Greenhouse\Python\plant1.jpg')
img2 = cv2.imread('D:\Engineering\Projects\Dr.Bagheri\Smart Greenhouse\Python\plant2.jpg')
img3 = cv2.imread('D:\Engineering\Projects\Dr.Bagheri\Smart Greenhouse\Python\plant3.jpg')

# Get images' information

row1, col1, ch1 = img1.shape
row2, col2, ch2 = img1.shape
row3, col3, ch3 = img1.shape
img1_size = row1 * col1
img2_size = row2 * col2
img3_size = row3 * col3

# Detecting green and yellow colored pixels

for i in range(0, row1 - 1):
    for j in range(0, col1 - 1):
        blue_pix = float(img1[i, j, 0])
        green_pix = float(img1[i, j, 1])
        red_pix = float(img1[i, j, 2])

        # The number of green color pixels

        if (green_pix > 3 * (blue_pix + red_pix) / 4) &\
                (green_pix > (blue_pix / 2)) &\
                (green_pix > (red_pix / 2)) &\
                (green_pix > 50):
            green += 1

        # The number of yellow color pixels

        elif (green_pix + red_pix > 100) &\
                (blue_pix < 0.3 * (red_pix + green_pix)) &\
                (abs(red_pix - green_pix) < 0.4 * min(red_pix, green_pix)):
            yellow += 1

# Showing the image

cv2.imshow('Image 1', img1)

# Detecting health of the plant in the image

green_percentage = (green / (green + yellow)) * 100
yellow_percentage = (yellow / (green + yellow)) * 100

if green_percentage > 95:
    healthy = True
else:
    healthy = False

# Printing the image's data

print(img1.shape)
print('Total pixels : %d' % img1_size)
print('Total green pixels : %d' % green)
print('Total yellow pixels : %d' % yellow)
print('Total green and yellow pixels : %d' % (green + yellow))
print('Green percentage is : %f' % green_percentage)
print('Yellow percentage is : %f' % yellow_percentage)
print('Total other colors pixels : %d' % (img1_size - (green - yellow)))
print('Healthy : %s' % healthy)

# Press Esc key to quit

k = cv2.waitKey(0) & 0xFF
while 1:
    if k == 27:
        break
cv2.destroyAllWindows()

# The End
