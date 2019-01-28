import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True,
                help = 'Path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('Original', image)


cropped = image[20:200, 600:900] # [y, x]
cv2.imshow('Cropped', cropped)
cv2.waitKey(0)