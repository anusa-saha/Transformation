import cv2 
import numpy as np
img = cv2.imread('lenna.jpg', 0)
height, width = img.shape[:2]
M = np.float32([[1, 0.5, 0], [0, 1, 0], [0, 0, 1]])
new_width1 = int(width + abs(0.5 * width)) 
new_height1 = height
sheared_img_xaxis = cv2.warpPerspective(img, M, (new_width1, new_height1))
N = np.float32([[1, 0, 0], [0.5, 1, 0], [0, 0, 1]])
new_width2 = width 
new_height2 = int(height + abs(0.5*height)) 
sheared_img_yaxis = cv2.warpPerspective(img, N, (new_width2, new_height2))
cv2.imshow('sheared_img_xaxis', sheared_img_xaxis)
cv2.imwrite('sheared_img_xaxis.jpg', sheared_img_xaxis)
cv2.imshow('sheared_img_yaxis', sheared_img_yaxis)
cv2.imwrite('sheared_img_yaxis.jpg', sheared_img_yaxis)
cv2.waitKey(0)
cv2.destroyAllWindows()
