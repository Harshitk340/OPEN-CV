import numpy as np
import cv2
image=cv2.imread('image_filtering_process\Screenshot 2024-12-03 204159.png')
kernal=np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])
sharpen=cv2.filter2D(image,-1,kernal)
cv2.imshow("original image", image)
cv2.imshow("sharpen image", sharpen)
cv2.waitKey(0)
cv2.destroyAllWindows()