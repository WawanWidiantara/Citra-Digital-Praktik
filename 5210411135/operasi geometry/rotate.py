import cv2
import numpy as np
import time
import math

# membaca gambar
img = cv2.imread("D:/Citra Digital Praktik/5210411135/image/fruit.jpg")
cvimg = img.copy()

row, column = img.shape[:2]
newImg = np.zeros(((row,column,3))).astype(np.uint8)

derajat = 45
t = math.radians((derajat))
cos,sin = (math.cos(t), math.sin(t))

cx,cy = (row//2, column//2)

# opencv
cvstart = time.time()
rotM = cv2.getRotationMatrix2D((cx,cy), -derajat, 1)
cvRot = cv2.warpAffine(cvimg, rotM, (column,row))
cv2.imshow('rotate opencv', cvRot)
cvend = time.time()

# manual
mnstart = time.time()
for i in range(row):
    for j in range(column):
        x = round(cx + (i-cx) * cos - (j-cy) * sin)
        y = round(cy + (i-cx) * sin + (j-cy) * cos)
            
        if (0 <= x < row)and(0 <= y < column):
            newImg[i,j] = img[x,y]         
cv2.imshow("ratate", newImg)
mnend = time.time()

cv2.waitKey()
print(f"opencv \t:{cvend - cvstart}\nmanual \t:{mnend - mnstart}")