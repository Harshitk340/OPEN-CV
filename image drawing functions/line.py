import cv2
image=cv2.imread("image drawing functions\IMG20250815105348.jpg")
if image is None:
    print("   ")
else:
    pt1=(50,100)
    pt2=(200,200)
    color=(0,255,0)
    new_image=cv2.line(image, pt1, pt2, color, 2)
    cv2.imshow("line image", new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()