import cv2
import numpy as np
import time

# membaca gambar
img = cv2.imread("D:/Citra Digital Praktik/5210411135/image/fruit.jpg")
cvimg = img.copy()

row, column = img.shape[:2]
newImg = np.uint8(np.zeros((row, column, 3))).astype(np.uint8)

# translasi
hor = False
ver = True

# opencv
cvstart = time.time()
if hor == True:
    cvflip = cv2.flip(cvimg, 1)
if ver == True:
    cvflip = cv2.flip(cvimg, 0)
cv2.imshow("translasi opencv", cvflip)
cvend = time.time()

# manual
mnstart = time.time()
for i in range(len(img)):
    for j in range(len(img[0])):
        if hor == True:
            newImg[i, column - 1 - j] = img[i, j]
        if ver == True:
            newImg[row - 1 - i,j] = img[i,j]
cv2.imshow("translasi manual", newImg)
mnend = time.time()

cv2.waitKey()
print(f"opencv \t: {cvend - cvstart}\nmanual \t: {mnend - mnstart}")
