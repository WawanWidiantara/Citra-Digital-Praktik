import cv2
import numpy as np

# membaca gambar
img = cv2.imread("D:/Citra Digital Praktik/5210411135/image/fruit.jpg")

# mengkonversi ke grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# mengkonversi ke b&w dengan numpy
row = len(gray_img)
column = len(gray_img[0])

bw_img = np.zeros((row, column)) # pembuatan array kosong
traceholder = 157

for rw in range(row):
    for cl in range(column):
        if gray_img[rw, cl] <= traceholder:
            bw_img[rw, cl] = 0
        else:
            bw_img[rw, cl] = 1

# menampilkan gambar
cv2.imshow("Gray Image", gray_img)
cv2.imshow("B&W Image", bw_img)
cv2.waitKey()
