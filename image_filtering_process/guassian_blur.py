import cv2
image=cv2.imread('image_filtering_process\Screenshot 2024-12-03 204159.png')
blured=cv2.GaussianBlur(image, (7,7), 0)

cv2.imshow("original image", image)
cv2.imshow("blurred image", blured)
cv2.waitKey(0)
cv2.destroyAllWindows()