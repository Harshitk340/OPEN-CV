import cv2
image=cv2.imread("image_resizing_and_shaping\IMG20250815105348.jpg")
if image is None:
    print("could not load image")
else:
    resized=cv2.resize(image,(300,300))
    cv2.imshow("original image", image)
    cv2.imshow("resized image", resized)
    cv2.imwrite("image_resizing_and_shaping\ resized.jpg", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
