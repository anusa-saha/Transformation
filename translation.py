import cv2
import numpy as np
img = cv2.imread('lenna.jpg')
height, width = img.shape[:2]
x_shift = width/8
y_shift = height/2
translation_matrix = np.float32([
    [1, 0, x_shift],
    [0, 1, y_shift]
])
translated_img = cv2.warpAffine(
    img,
    translation_matrix,
    (height, width),
)
cv2.imshow('Original', img)
cv2.imshow('Translated', translated_img)
cv2.imwrite('translated_image.jpg', translated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
