import cv2
image=cv2.imread("IMG20250815105348.jpg")
if image is not None:
    gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    a= input("save or show? :")
    if a.lower()=="save":
        name= input("enter name of file with extension:")
        success=cv2.imwrite(name, gray)
        if success:
            print("image saved successfully")
        else:
            print("could not save image")
    elif a.lower()=="show":
        cv2.imshow("gray scale image", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("please type properly")
else:
    print("could not load image")
