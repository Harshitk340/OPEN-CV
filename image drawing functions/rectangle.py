import cv2
image=cv2.imread("image drawing functions\IMG20250815105348.jpg")
if image is None:
    print("   ")
else:
    pt1=(50,100)
    pt2=(500,500)
    color=(0,255,0)
    new_image2=cv2.rectangle(image, pt1, pt2, color, 5)
    cv2.imshow("rectangle image", new_image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()