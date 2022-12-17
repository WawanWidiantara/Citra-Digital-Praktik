import cv2
import numpy as np
import math

img = cv2.imread("D:/Citra Digital Praktik/5210411135/image/fruit.jpg")

row, column = img.shape[:2]
newImg = np.zeros(((row,column,3))).astype(np.uint8)

derajat = 45
t = math.radians((derajat))
cos,sin = (math.cos(t), math.sin(t))

cx,cy = (row//2, column//2)

x = [round(cx + (i-cx) * cos - (j-cy) * sin) for i in range(row) for j in range(column)]
y = [round(cy + (i-cx) * sin + (j-cy) * cos) for i in range(row) for j in range(column)]

nrow = (abs(max(x) - min(x)) + 1)
ncolumn = (abs(max(y) - min(y)) + 1)

