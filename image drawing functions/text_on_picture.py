import cv2
image=cv2.imread("image drawing functions\IMG20250815105348.jpg")
if image is None:
    print("   ")
else:
    color=(0,255,0)
    new_image2=cv2.putText(image, "this is text written by me", (200,200), cv2.FONT_HERSHEY_COMPLEX, 1, color, 2)
    cv2.imshow("text on image", new_image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()