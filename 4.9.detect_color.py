import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    blur = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    upper_blue = np.array([130,255,255])
    lower_blue = np.array([110,50,50])
    mask = cv2.inRange(hsv, lower_blue,upper_blue)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for i in contours:
        area = cv2.contourArea(i)

        if area > 3000:
            cv2.drawContours(frame, i, -1, (0,255,0), 3)


    cv2.imshow('mask', mask)
    cv2.imshow('imagem', frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()