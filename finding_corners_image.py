import numpy as np
import cv2

img = cv2.imread('D:/cubes.jpg')
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayscale = np.float32(grayscale)

dst = cv2.cornerHarris(grayscale, 2, 3, 0.04)#so melhorou quando diminui o k, mas n entendi pq
dst = cv2.dilate(dst, None)

img[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow('Image_with_corners', img)

key = cv2.waitKey(0) & 0xFF

if key == 27:
    cv2.destroyAllWindows()
