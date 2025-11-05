import cv2
image=cv2.imread("IMG20250815105348.jpg")
if image is not None:
    h, w, c = image.shape
    print(f"image dimensions are:\nheight: {h} \nwidth:{w} \nchannel:{c}")
else:
    print("could not load image\n")