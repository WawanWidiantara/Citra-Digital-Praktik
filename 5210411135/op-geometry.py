import cv2
import numpy as np
from copy import deepcopy

# membaca gambar
img = cv2.imread("D:/Citra Digital Praktik/5210411135/image/fruit.jpg")
newImg = np.zeros((len(img), len(img[0]), len(img[0][0]))).astype(np.uint8)


def translasi(px=0, py=0):
    tr = deepcopy(newImg)
    for i in range(len(img)):
        for j in range(len(img[0])):
            if (0 < j + px < len(img[0])) and (0 < i - py < len(img)):
                tr[i - py, j + px] = img[i, j]
    return tr


def flipping(px=False, py=False):
    tr = deepcopy(newImg)
    for i in range(len(img)):
        for j in range(len(img[0])):
            if px == True:
                tr[i, j] = img[len(img) - 1 - i, j]
            if py == True:
                tr[i, j] = img[i, len(img[0]) - 1 - j]
    return tr


cv2.imshow("original", img)
cv2.imshow("kiri 100 & atas 100", translasi(px=100,py=100))
cv2.imshow("flip vertical", flipping(px=True))
cv2.imshow("flip horizontal", flipping(py=True))
cv2.waitKey()
