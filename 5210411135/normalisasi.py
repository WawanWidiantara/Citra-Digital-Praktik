import cv2
import numpy as np
from matplotlib import pyplot as plt

# read image
img = cv2.imread("D:/Citra Digital Praktik/5210411135/image/fruit.jpg")

# split sesuai channel warna
b, r, g = cv2.split(img)

# rgb to grayscale package bawaan
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# buat array kosong 1D untuk tempat normalisasi
his_b = np.zeros(256)  # channel blue
his_r = np.zeros(256)  # channel red
his_g = np.zeros(256)  # channel green
his_gr = np.zeros(256)  # channel gray

# membaca jumlah row dan column
row = len(b)
column = len(b[0])

# normalisasi
for i in range(row):  # perulangan untuk row
    for j in range(column):  # perulangan untuk column
        # blue
        px_b = b[i, j]  # membaca tiap pixel pada channel
        his_b[px_b] += 1 / (row * column)  # menghitung peluang pixel yang muncul
        # red
        px_r = r[i, j]
        his_r[px_r] += 1 / (row * column)
        # green
        px_g = g[i, j]
        his_g[px_g] += 1 / (row * column)
        # gray
        px_gr = gray[i, j]
        his_gr[px_gr] += 1 / (row * column)

# menampilkan gambar
cv2.imshow("gambar", img)  # rgb
cv2.imshow("gray", gray)  # gray

# membuat & menampilkan histogram
plt.plot(his_b, color="blue")
plt.plot(his_r, color="red")
plt.plot(his_g, color="green")
plt.plot(his_gr, color="gray")
plt.show()

cv2.waitKey()
