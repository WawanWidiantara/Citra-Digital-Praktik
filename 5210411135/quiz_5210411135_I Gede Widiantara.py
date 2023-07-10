import cv2
import numpy as np
import math

# membaca gambar
img = cv2.imread("D:\Code\py_code\Citra-Digital-Praktik/5210411135\image\Latihan - pekan 10.jpg")
row, column = img.shape[:2]


# merotasi gambar 5 derajat ccw
derajat = -5
t = math.radians((derajat))
cos,sin = (math.cos(t), math.sin(t))
rotImg = np.zeros(((row,column,3))).astype(np.uint8)

cx,cy = (row//2, column//2)

for i in range(row):
    for j in range(column):
        x = round(cx + (i-cx) * cos - (j-cy) * sin)
        y = round(cy + (i-cx) * sin + (j-cy) * cos)

        if (0 <= x < row) and (0 <= y < column):
            rotImg[i,j] =  img[x,y]

cv2.imshow('rotasi 5 derajat ccw', rotImg)


gray = cv2.cvtColor(rotImg, cv2.COLOR_BGR2GRAY)
grow, gcolumn = gray.shape[:2]

# meningkatkan brightness
addbr = 20
bright = np.zeros(gray.shape).astype(np.uint8)

for i in range(grow):
    for j in range(gcolumn):
        px = gray[i, j] + addbr
        if px.any() > 255:
            bright[i, j] = 255
        else:
            bright[i, j] = px 

cv2.imshow('menerangkan', bright)


# menajamkan gambar
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
konImg = np.zeros(bright.shape).astype(np.uint8)

for i in range(1, grow - 1):
    for j in range(1, gcolumn - 1):
        mconv = bright[i - 1 : i + 2, j - 1 : j + 2]
        konvolusi = round((mconv * kernel).sum() / kernel.sum())
        
        if konvolusi > 255:
            konvolusi = 255
        if konvolusi < 0:
            konvolusi = 0

        konImg[i, j] = konvolusi

cv2.imshow('menajamkan', konImg)


cv2.waitKey()