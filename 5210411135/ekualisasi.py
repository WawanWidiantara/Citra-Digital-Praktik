import cv2
import numpy as np
from matplotlib import pyplot as plt
from copy import deepcopy

# membaca gambar
img = cv2.imread("D:/Citra Digital Praktik/5210411135/image/fruit.jpg")

b, r, g = cv2.split(img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def normalisasi(channel, ks=np.zeros(256)):
    c = deepcopy(channel)
    his = deepcopy(ks)
    for rw in range(len(c)):
        for cl in range(len(c[0])):
            px_b = c[rw, cl]
            his[px_b] += 1 / (len(c) * len(c[0]))
    return his


def ekualisasi(channel):
    p = deepcopy(normalisasi(channel))
    c = deepcopy(channel)
    for i in range(len(c)):
        for j in range(len(c[0])):
            px = c[i, j]
            c[i, j] = round(((len(c) * len(c[0])) - 1) * sum(p[0 : px + 1]))
    return normalisasi(c)


# cv2.imshow("gambar", img)
plt.plot(normalisasi(b), color="red")
plt.plot(ekualisasi(b), color="blue")
plt.plot(normalisasi(gray), color="black")
plt.plot(ekualisasi(gray), color="gray")

plt.show()

# cv2.waitKey()
