import cv2
image=cv2.imread("P:\openCV\image_filtering_process\_1.jpg", cv2.IMREAD_GRAYSCALE)
ret, edges=cv2.threshold(image, 80, 255, cv2.THRESH_BINARY)
cv2.imshow("original image", image)
cv2.imshow("thresh image", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()