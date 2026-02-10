import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1024)
cap.set(cv2.CAP_PROP_FPS, 60)

while cv2.waitKey(10) < 0:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2.imshow("VideoFrame", frame)

cap.release()
cv2.destroyAllWindows()