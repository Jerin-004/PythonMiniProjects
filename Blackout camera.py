import cv2
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    diff = cv2.absdiff(frame1, frame2)
    if cv2.waitKey(10) ==ord("q") :
        break
    cv2.imshow("Blackout camera", diff)