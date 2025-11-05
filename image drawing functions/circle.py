import cv2
image=cv2.imread("image drawing functions\IMG20250815105348.jpg")
if image is None:
    print("   ")
else:
    center=(500,500)
    color=(0,255,0)
    new_image2=cv2.circle(image, center, 300, color, -1)
    cv2.imshow("circle image", new_image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()