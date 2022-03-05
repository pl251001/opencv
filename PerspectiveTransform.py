import cv2 as cv
import numpy as np
#C:/Users/Lucas/Downloads/IMG_9750
img = cv.imread('C:/Users/Lucas/Downloads/test_l3.jpg')
#img = cv.imread('/Users/local/Downloads/test_l3.jpeg')


height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
# print(height,width)

pts1 = np.float32([[770,312], [1657,105],
                [888,799], [1770,603]])


pts2 = np.float32([[1090, 293], [1381, 293],
                [1090, 584], [1381, 584]])


# Apply Perspective Transform Algorithm
matrix = cv.getPerspectiveTransform(pts1, pts2)
result = cv.warpPerspective(img, matrix, (2121,1414))

cv.circle(img, (770,312), 20, (255, 255, 255), 3)
cv.circle(img, (1657,105), 20, (255, 255, 255), 3)
cv.circle(img, (883,810), 20, (255, 255, 255), 3)
cv.circle(img, (1770,603), 20, (255, 255, 255), 3)
cv.circle(img, (353,0), 20, (0,255,0), 3)
cv.circle(img, (353,1414), 20, (0,255,0), 3)
cv.circle(img, (1768,0), 20, (0,255,0), 3)
cv.circle(img, (1768,1414), 20, (0,255,0), 3)


frame=result.copy()
frame = cv.cvtColor(result, cv.COLOR_BGR2GRAY)


frame = cv.medianBlur(frame, 5)


circles = cv.HoughCircles(frame, cv.HOUGH_GRADIENT, 1, 20,
                      param1=50, param2=30, minRadius=75, maxRadius=150)

if circles is None:
   pass
else:

   circles = np.uint16(np.around(circles))
   for i in circles[0, :1]:
       # draw the outer circle
       cv.circle(result, (i[0], i[1]), i[2], (255, 255, 255), 3)
       # draw the center of the circle
       cv.circle(result, (i[0], i[1]), 2, (0, 0, 255), 3)


matrix = cv.getPerspectiveTransform(pts2, pts1)
result = cv.warpPerspective(result, matrix, (2121,1414))




# Wrap the transformed image
#cv.imshow('frame', img)  # Initial Capture
cv.imshow('frame1', result)  # Transformed Capture

#cv.imwrite('/Users/local/Downloads/uwu.jpeg',result)

cv.waitKey()
img.release()
cv.destroyAllWindows()







