import cv2
image=cv2.imread("image_resizing_and_shaping\IMG20250815105348.jpg")
if image is not None:
    cropped=image[100:200, 500:750]
    cv2.imshow("original image", image)
    cv2.imshow("cropped image", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("could not found image")