import cv2
import numpy as np

# membaca gambar
minus = cv2.imread("D:/Citra Digital Praktik/5210411135/image/fruit.jpg", 0)
img = cv2.imread("D:/Citra Digital Praktik/5210411135/image/minusbucket.jpg", 0)
newImg = np.zeros((len(minus), len(minus[0]))).astype(np.uint8)

for i in range(len(newImg)):
    for j in range(len(newImg[0])):
        px = int(img[i, j]) - int(minus[i, j])
        if px > 255:
            newImg[i, j] = 255
        elif px < 0:
            newImg[i, j] = 0
        else:
            newImg[i, j] = px

cv2.imshow("minus", minus)
cv2.imshow("original", img)
cv2.imshow("hasil", newImg)

cv2.waitKey()
