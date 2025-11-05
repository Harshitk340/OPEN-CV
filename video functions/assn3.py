import cv2
camera=cv2.VideoCapture(0)
user=input("what do you wants to do?(use camera/ record video): ")
if user.lower()=='use camera':
    while True:
        success, video=camera.read()
        if not success:
            break
        cv2.imshow("live video", video)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    camera.release()
    cv2.destroyAllWindows()
    print(".-/|\-.")
elif user.lower()=='record video':
    frame_width=int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height=int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
    codec=cv2.VideoWriter_fourcc(*'XVID')
    recorder=cv2.VideoWriter('myvideo.avi', codec, 20, (frame_width, frame_height))
    while True:
        success, video=camera.read()
        if not success:
            break
        recorder.write(video)
        cv2.imshow("recording video", video)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    camera.release()
    recorder.release()
    cv2.destroyAllWindows()
    view=input("do you wants to view your video(yes/no):")
    if view.lower()=='yes':
        recorded_video=cv2.VideoCapture("myvideo.avi")
        while True:
            success, image=recorded_video.read()
            if not success:
                break
            cv2.imshow("recorded video", image)
            if cv2.waitKey(50) & 0xFF==ord('q'):
                break
        recorded_video.release()
        cv2.destroyAllWindows()
    else:
        print("--------------byy---------------")
else:
    print("please type properly")
