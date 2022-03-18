import cv2 as cv
import numpy as np
import random
import math

img = cv.imread('/Users/local/Downloads/IMG_9912.jpg')


height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
print(height,width)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Use canny edge detection
edges = cv.Canny(gray, 5000, 8000, apertureSize=5)

kernel_size = 15
edges = cv.GaussianBlur(edges,(kernel_size, kernel_size),0)


lines = cv.HoughLinesP(
      edges, # Input edge image
      1, # Distance resolution in pixels
      np.pi/180, # Angle resolution in radians
      threshold=1000, # Min number of votes for valid line
      minLineLength=1100, # Min allowed length of line
      maxLineGap=10 # Max allowed gap between line for joining them
      )
print(len(lines))
# print(lines)
slopelst=[]
color1,color2,color3=0,100,200
linelst=[]
anglelst=[]


for points in lines:
    #print(points)
    # Extracted points nested in the list
    slope=1
    x1,y1,x2,y2=points[0]
    if x2-x1==0:
        pass
    else:
        slope=(y1-y2)/(x2-x1)

    if slope<0:
        angle=np.pi-math.atan(abs(slope))
    else:
        angle = math.atan(slope)
    # print(x1,y1,x2,y2)
    # print(img[1304,1183])
    # print(img[y1,x1])
    # print(img[y2,x2])
    # Draw the lines joing the points
    # On the original image
    number=255
    b1, g1, r1 = (img[y1,x1])
    b2, g2, r2 = (img[y2, x2])
    if (b1<number and g1<number and r1<number) or (b2<number and r2<number and g2<number):
        #print(x1,y1,x2,y2)
        print(f"slopes: {slope}")
        print(f"angles: {angle}")
        #cv.line(img,(x1,y1),(x2,y2),(color1,color2,color3),4)
        color1=random.randint(0, 255)
        color2 = random.randint(0, 255)
        color3 = random.randint(0, 255)
        anglelst.append(angle)
        slopelst.append(slope)
        linelst.append(points[0][0:2])
        linelst.append(points[0][2:])

set1=[]
set2=[]
firstintercept=points[0][0][1]-(points[0][0][0]*slopelst[0])
for x in range(len(lines)):
    x1, y1, x2, y2 = points[0]
    slope=slopelst[x]
    yintercept=y1-(x1*slope)
    if yintercept <= firstintercept+100 and yintercept >= firstintercept-100:
        lines[x].append(1)
    else:
        lines[x].append(0)
#0 is one side, 1 is another side

for x in lines;
    x1, y1, x2, y2 = x[0]
    if x[1]==1:
        cv.line(img,(x1,y1),(x2,y2),(255,255,0),4)
    if x[1]==0:

min1x=0
min2x=0
max1y=0
max2y=0
for x in linelst:

    if max1y>max2y:
        if x[1]>max1y:
            if x[1]>max2y:
               min2x=x[0]
               max2y=x[1]
            else:
               max1y=x[1]
               min1x=x[0]
    else:

        if x[1]>=max2y:
            if x[1]>max1y:
               min1x=x[0]
               max1y=x[1]
            else:
               max2y=x[1]
               min2x=x[0]

print(min1x, max1y, min2x, max2y)

midpt=(int((min1x+min2x)/2),int((max1y+max2y)/2))
print(midpt)

avgangle=0
for x in anglelst:
   avgangle=avgangle+x
   avgangle=avgangle/len(anglelst)

length=100

endpt=(int(midpt[0]+length),int(midpt[1]-math.tan(avgangle)*length))
print(endpt)
print(avgangle)

#cv.line(img,midpt,endpt,(color1,color2,color3),4)




# Maintain a simples lookup list for points
# lines_list.append([(x1,y1),(x2,y2)])

cv.imshow('frame', img)  # Initial Capture
# cv.imshow('frame1', gray)
#cv.imshow('frame2', edges)# Transformed Capture

#cv.imwrite('/Users/local/Downloads/uwu.jpeg',result)

cv.waitKey()
img.release()
cv.destroyAllWindows()












