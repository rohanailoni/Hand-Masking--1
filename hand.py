import cv2
import numpy as np
import imutils
image=cv2.imread('hand1.png')


im=cv2.cvtColor(image,cv2.COLOR_BGR2HLS_FULL)

# lower=np.array((0, 0.8 * 255, 0.6 * 255))
# upper=np.array((15, 0.1 * 255, 0.05 * 255))
lower = np.array([0,0,0])
upper=np.array([40, 255, 255])
im=cv2.inRange(im,lower,upper)


im = cv2.GaussianBlur(im, (7, 7), 3)



thresh = cv2.adaptiveThreshold(im, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
thresh = cv2.bitwise_not(thresh)
_,th=cv2.threshold(im,200,255,cv2.THRESH_BINARY)

con=cv2.findContours(th,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
con=imutils.grab_contours(con)

con = sorted(con, key=cv2.contourArea, reverse=True)
cv2.drawContours(image,con[0],-1,(0,255,0),5)



hull=[]
for i in range(len(con)):
    hull.append(cv2.convexHull(con[i], False))
drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)

for i in range(len(con)):
    color_contours = (0, 255, 0)
    color = (255, 0, 0)
    cv2.drawContours(drawing, con, i, color_contours, 1, 8)
    cv2.drawContours(drawing, hull, i, color, 1, 8)
    break

epsilon = 0.0005 * cv2.arcLength(con[0], True)
approx = cv2.approxPolyDP(con[0], epsilon, True)
hull_c=cv2.convexHull(con[0])
hull_c=cv2.convexHull(approx,returnPoints=False)
defects=cv2.convexityDefects(approx,hull_c)
for i in range(defects.shape[0]):
    s,e,f,d=defects[i,0]

cv2.imshow("image",drawing)
cv2.waitKey(0)


