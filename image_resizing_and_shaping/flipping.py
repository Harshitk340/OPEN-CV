import cv2
image=cv2.imread("image_resizing_and_shaping\IMG20250815105348.jpg")
if image is None:
    print("   ")
else:
    flipped_horizontal=cv2.flip(image, 1)
    flipped_vertical=cv2.flip(image, 0)
    flipped_both=cv2.flip(image, -1)
    cv2.imshow("flipped horizontal", flipped_horizontal)
    cv2.imshow("flipped vertical", flipped_vertical)
    cv2.imshow("flipped_both", flipped_both)
    cv2.waitKey(0)
    cv2.destroyAllWindows()