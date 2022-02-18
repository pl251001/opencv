import cv2 as cv
import numpy as np
#C:/Users/Lucas/Downloads/IMG_9750
img = cv.VideoCapture('C:/Users/Lucas/Downloads/IMG_9750.MOV')


frame_width = int(img.get(3))
frame_height = int(img.get(4))

size = (frame_width, frame_height)

out = cv.VideoWriter('outpy.avi', cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, size)


number = 0
total = 0
while img.isOpened():
   if total==283:
       break
   else:
       ret, image = img.read()
       total = total + 1
       # if frame is read correctly ret is True
       if not ret:
         print("Can't receive frame (stream end?). Exiting ...")
         break
       frame=image.copy()
       frame = cv.medianBlur(cv.cvtColor(img.read()[1], cv.COLOR_BGR2GRAY), 5)

       # frame = cv.medianBlur(frame, 5)

       # cimg = cv.cvtColor(frame, cv.COLOR_GRAY2BGR)
       circles = cv.HoughCircles(frame, cv.HOUGH_GRADIENT, 1, 20,
                               param1=10, param2=40, minRadius=40, maxRadius=60)

       if circles is None:
         pass
       else:

         circles = np.uint16(np.around(circles))
         for i in circles[0, :1]:
             number = number + 1
             # draw the outer circle
             cv.circle(image, (i[0], i[1]), i[2], (255, 255, 255), 3)
             # draw the center of the circle
             cv.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)
       #frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
       txt=f"Frames with circle: {number}/{total}"
       #cv.waitKey(50)
       cv.putText(img=image, text=txt, org=(0, 50), fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0, 255, 0),
                 thickness=3)
       cv.putText(img=image, text="I love you Mr. Rivero give me A+ uwu", org=(0, 500), fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(252, 15, 192),
                thickness=3)

       if ret==True:
           out.write(image)

       cv.imshow('frame', image)
       # out = cv.VideoWriter('outpy.avi', cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, size)
       #imwrite
       print(number, total)
       # cv.waitKey(5)
       if cv.waitKey(1) == ord('q'):
         break
print(f"total frames: {total}\nnumber of frames with circle: {number}")

out.release()
img.release()
cv.destroyAllWindows()









