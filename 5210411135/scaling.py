import cv2
import numpy as np
import time

# membaca gambar
img = cv2.imread("D:/Citra Digital Praktik/5210411135/image/fruit.jpg")
cvimg = img.copy()

row, column = img.shape[:2]

# scale
ratio = 1.2
nrow, ncolumn = ((int(row * ratio)), (int(column * ratio)))
newImg = np.uint8(np.zeros((nrow, ncolumn, 3))).astype(np.uint8)

# opencv
cvstart = time.time()
cvscale = cv2.resize(cvimg, (nrow, ncolumn), interpolation=cv2.INTER_AREA)
cv2.imshow("scaling opencv", cvscale)
cvend = time.time()

# manual
mnstart = time.time()
for i in range(nrow):
    for j in range(ncolumn):
        newImg[i, j] = img[round(i / ratio), round(j / ratio)]
cv2.imshow("scaling manual", newImg)
mnend = time.time()

cv2.waitKey()
print(f"opencv \t:{cvend - cvstart}\nmanual \t:{mnend - mnstart}")
