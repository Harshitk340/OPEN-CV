import cv2
image=cv2.imread("IMG20250815105348.jpg")
if image is not None:
    success=cv2.imwrite("saved_image.jpg", image)
    if success:
        print("image saved successfully")
    else:
        print("failed to save image")
else:
    print("image loaded succesfully\n")