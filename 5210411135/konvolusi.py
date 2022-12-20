import cv2
import numpy as np

# membaca gambar
ori = cv2.imread("D:/Citra Digital Praktik/5210411135/image/fruit.jpg")
img = cv2.cvtColor(ori, cv2.COLOR_BGR2GRAY)
newImg = np.zeros(ori.shape).astype(np.uint8)

#  kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) # sharp
kernel = np.array([[1, 2, 1], [1, 4, 1], [1, 2, 1]]) # blur

row, column = ori.shape[:2]
krow, kcolumn = kernel.shape[:2]

for i in range(1, row - 1):
    for j in range(1, column - 1):
        mconv = img[i - 1 : i + 2, j - 1 : j + 2]
        konvolusi = round((mconv * kernel).sum() / kernel.sum())
        
        if konvolusi > 255:
            konvolusi = 255
        if konvolusi < 0:
            konvolusi = 0

        newImg[i, j] = konvolusi

cv2.imshow("ori", img)
cv2.imshow("konvolusi", newImg)
cv2.waitKey()
