# Importing libraries
import cv2
import numpy as np

# Defining color variables
green = 0
yellow = 0
green_percentage = 0
yellow_percentage = 0
healthy = False

# Loading the image
img = cv2.imread('D:\Engineering\Projects\Dr.Bagheri\Smart Greenhouse\Python\plant2.jpg')

# Get image's information
row, col, ch = img.shape
img_size = row * col


# Detecting green and yellow colored pixels
def detect_green_yellow():
    global green
    global yellow
    for i in range(0, row - 1):
        for j in range(0, col - 1):
            blue_pix = float(img[i, j, 0])
            green_pix = float(img[i, j, 1])
            red_pix = float(img[i, j, 2])

            # The number of green color pixels
            if (green_pix > 3 * (blue_pix + red_pix) / 4) & \
                    (green_pix > (blue_pix / 2)) & \
                    (green_pix > (red_pix / 2)) & \
                    (green_pix > 50):
                green += 1

            # The number of yellow color pixels
            elif (green_pix + red_pix > 100) & \
                    (blue_pix < 0.3 * (red_pix + green_pix)) & \
                    (abs(red_pix - green_pix) < 0.4 * min(red_pix, green_pix)):
                yellow += 1


# Detecting health
def detect_health():
    global green_percentage
    global yellow_percentage
    global healthy

    # Detecting health of the plant in the image
    green_percentage = (green / (green + yellow)) * 100
    yellow_percentage = (yellow / (green + yellow)) * 100

    # Detecting plant's health
    healthy = False
    if green_percentage > 95:
        healthy = True


# Exit Function
def escape():
    # Press Esc key to quit
    k = cv2.waitKey(0) & 0xFF
    while 1:
        if k == 27:
            break
    cv2.destroyAllWindows()


# Main
def main():
    # Calling detecting color function
    detect_green_yellow()

    # Showing the image
    cv2.imshow('Image 1', img)

    # Calling detecting health function
    detect_health()

    # Printing the image's data
    print(img.shape)
    print('Total pixels : %d' % img_size)
    print('Total green pixels : %d' % green)
    print('Total yellow pixels : %d' % yellow)
    print('Total green and yellow pixels : %d' % (green + yellow))
    print('Green percentage is : %f' % green_percentage)
    print('Yellow percentage is : %f' % yellow_percentage)
    print('Total other colors pixels : %d' % (img_size - (green - yellow)))
    print('Healthy : %s' % healthy)

    # Exit by pressing escape button
    escape()

# Run
if __name__ == '__main__':
    main()

# The END!
