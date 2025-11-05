import cv2
image=cv2.imread("IMG20250815105348.jpg")
if image is None:
    print("image not found\n")
else:
    print("image loaded succesfully\n")