import cv2
image=cv2.imread("image_resizing_and_shaping\IMG20250815105348.jpg")
if image is None:
    print("   ")
else:
    (h,w)= image.shape[:2]
    center=(w//2, h//2)
    m=cv2.getRotationMatrix2D(center, 90, 1)
    rotated_image=cv2.warpAffine(image, m, (w, h))
    cv2.imshow("original image", image)
    cv2.imshow("rotated image", rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()