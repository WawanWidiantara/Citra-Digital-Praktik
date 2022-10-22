import cv2
import numpy as np
from matplotlib import pyplot as plt

# membaca gambar
img = cv2.imread("D:/5210411135/fruit.jpg")

b, r, g = cv2.split(img)

row = len(b)
column = len(b[0])

his_b = np.zeros(256)
his_r = np.zeros(256)
his_g = np.zeros(256)

for rw in range(row):
    for cl in range(column):
        px_b = int(b[rw, cl])
        px_r = int(r[rw, cl])
        px_g = int(g[rw, cl])

        his_b[px_b] += 1 / (row * column)
        his_r[px_r] += 1 / (row * column)
        his_g[px_g] += 1 / (row * column)


cv2.imshow("gambar", img)
plt.plot(his_b, color="blue")
plt.plot(his_r, color="red")
plt.plot(his_g, color="green")
plt.show()

cv2.waitKey()

# buat histogram grayscale
