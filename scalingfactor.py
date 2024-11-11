import cv2
import numpy as np

image = cv2.imread("lenna.jpg")
height, width = image.shape[:2]
print("Height:", height)
print("Width:", width)
scale_up = 2.0
resized_image = cv2.resize(image, None ,fx= scale_up, fy= scale_up,
                            interpolation= cv2.INTER_LINEAR)
cv2.imwrite("resized_double.jpg", resized_image)
cv2.imshow("resized_double",resized_image )
h1,w1 = resized_image.shape[:2]
print("Height(sized up):", h1)
print("Width(sized up):", w1)
scale_down = 0.5
resized_image = cv2.resize(image, None ,fx= scale_down, fy= scale_down,
                           interpolation= cv2.INTER_LINEAR)
cv2.imwrite("resized_50_percent.jpg", resized_image)
cv2.imshow("resized_50_percent",resized_image )
h1,w1 = resized_image.shape[:2]
print("Height(sized down):", h1)
print("Width(sized down):", w1)
cv2.waitKey()
cv2.destroyAllWindows()
