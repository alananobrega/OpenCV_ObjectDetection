import numpy as np
import cv2

cap = cv2.VideoCapture(0)

if (cap.isOpened()==False):
    print("Error open video stream")

while (True):
    ret, frame = cap.read()
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    grayscale = np.float32(grayscale)
    dst = cv2.cornerHarris(grayscale,2,3,0.04)

    dst = cv2.dilate(dst, None)

    frame[dst>0.01*dst.max()]=[0,0,255]#250 eh o valor de branco na escala cinza. entender melhor tbm

    cv2.imshow("Video_with_corners", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()