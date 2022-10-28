import cv2
import numpy as np

# membaca gambar
img = cv2.imread("D:/Citra Digital Praktik/5210411135/image/fruit.jpg")

# mengkonversi ke grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresholder = 200

# mengkonversi ke b&w dengan numpy
row = len(gray_img)
column = len(gray_img[0])

bw_img = np.zeros((row, column))  # pembuatan array kosong

for rw in range(row):
    for cl in range(column):
        if gray_img[rw, cl] <= thresholder:
            bw_img[rw, cl] = 0
        else:
            bw_img[rw, cl] = 1

# mengkonversi ke b&w dengan opencv
im_bw = cv2.threshold(gray_img, thresholder, 255, cv2.THRESH_BINARY)[1]

# menampilkan gambar
cv2.imshow("Gray Image", gray_img)
cv2.imshow("B&W Image", bw_img)
cv2.imshow("W&B Image", im_bw)
cv2.waitKey()
