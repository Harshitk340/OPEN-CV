import cv2
image=cv2.imread("image_filtering_process\Screenshot 2024-12-03 204159.png", cv2.IMREAD_GRAYSCALE)
edges=cv2.Canny(image, 50, 150)
cv2.imshow("original image", image)
cv2.imshow("edge image", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()