# Standard imports
import cv2
import numpy as np

# Read image
im = cv2.imread("D:/blobs.jpg", cv2.IMREAD_GRAYSCALE)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 10;
params.maxThreshold = 2000;

# Filter by Area.
params.filterByArea = True
params.minArea = 100
params.maxArea = 100000

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.75
params.maxCircularity = 0.785

# Filter by Convexity
#params.filterByConvexity = True
#params.minConvexity = 0.87

# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.5
#params.maxInertiaRatio = 1


detector = cv2.SimpleBlobDetector_create(params)
keypoints = detector.detect(im)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0, 0, 255),
                                      cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)