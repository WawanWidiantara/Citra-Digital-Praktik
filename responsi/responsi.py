# loop sengaja dibuat berulang di tiap soal untuk merpermudah pembacaan code

# import module
import cv2
import numpy as np
from matplotlib import pyplot as plt

# read image (soal 1 {unduh gambar})
img = cv2.imread("D:/Citra Digital Praktik/responsi/uang 100rb - 4.jpg")

# split img sesuai channel warna
b, g, r = img[:, :, 0], img[:, :, 1], img[:, :, 2]

# soal 2
his_r = np.zeros(256)
his_g = np.zeros(256)
his_b = np.zeros(256)

for i in range(len(img)):
    for j in range(len(img[0])):
        # blue
        px_b = b[i, j]
        his_b[px_b] += 1 / (len(img) * len(img[0])) # normalisasi
        # red
        px_r = r[i, j]
        his_r[px_r] += 1 / (len(img) * len(img[0])) # normalisasi
        # green
        px_g = g[i, j]
        his_g[px_g] += 1 / (len(img) * len(img[0])) # normalisasi

# membuat histogram dengan matplotlib
plt.plot(his_b, color="blue")
plt.plot(his_g, color="green")
plt.plot(his_r, color="red")


# soal 3
gray = np.zeros((len(img), len(img[0]))).astype(np.uint8)  # array kosong untuk grayscale

for i in range(len(img)):
    for j in range(len(img[0])):
        gray[i, j] = round(0.299 * (r[i, j]) + 0.587 * (g[i, j]) + 0.114 * (b[i, j]))


# soal 4
bright = np.zeros((len(img), len(img[0]))).astype(np.uint8)  # array kosong untuk grayscale

# manual
addbr = 30
for i in range(len(gray)):
    for j in range(len(gray[0])):
        px = gray[i, j] + addbr
        if px > 255:
            bright[i, j] = 255
        else:
            bright[i, j] = px
            
# bawaan opencv
bright_cv2 = cv2.addWeighted(gray, 1, np.zeros(bright.shape, bright.dtype), 0, addbr)

# soal 5
bw = np.zeros((len(img), len(img[0]))).astype(np.uint8)  # array kosong b&w

# manual
th = 160
for i in range(len(bw)):
    for j in range(len(bw[0])):
        if bright[i, j] <= th:
            bw[i, j] = 0
        else:
            bw[i, j] = 255
            
# bawaan opencv
bw_cv2 = cv2.threshold(bright, th, 255, cv2.THRESH_BINARY)[1]


# menampilkan hasil
cv2.imshow("original", img)
cv2.imshow("grayscale", gray)  # menampilkan grayscale
cv2.imshow(f"add brightness {addbr}", bright)  # menampilkan tambahan brightness
cv2.imshow(f"add brightness {addbr} opencv", bright_cv2) # menampilkan tambahan brightness cv2
cv2.imshow("black & white", bw)  # menampilkan b & w
cv2.imshow("b & w opencv", bw_cv2)# menampilkan b & w cv2
plt.show()  # menampilkan histogram

# mencegah window langsung tertutup
cv2.waitKey()
