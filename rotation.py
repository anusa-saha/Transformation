import cv2
import numpy as np 
image = cv2.imread('lenna.jpg')
height, width = image.shape[:2]
center = (width / 2, height / 2)
angle = 45
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale=1.0)
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
cv2.imshow('Rotated Image', rotated_image)
cv2.imwrite('rotated_image.jpg', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
