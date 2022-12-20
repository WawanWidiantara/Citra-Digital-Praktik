import cv2
import numpy as np
import time

# membaca gambar
img = cv2.imread("D:/Citra Digital Praktik/5210411135/image/fruit.jpg")
cvimg = img.copy()

row, column = img.shape[:2]
newImg = np.uint8(np.zeros((row, column, 3))).astype(np.uint8)

# translasi
hor = 20
ver = 20

# opencv
cvstart = time.time()
t = np.float32([[1, 0, hor], [0, 1, ver]])
cvTranslasi = cv2.warpAffine(cvimg, t, (column, row))
cv2.imshow("translasi opencv", cvTranslasi)
cvend = time.time()

# manual
mnstart = time.time()
for i in range(row):
    for j in range(column):
        if (0 <= i + ver < row) and (0 <= j + hor < column):
            newImg[i + ver, j + hor] = img[i, j]
cv2.imshow("translasi manual", newImg)
mnend = time.time()

cv2.waitKey()
print(f"opencv \t:{cvend - cvstart}\nmanual \t:{mnend - mnstart}")
