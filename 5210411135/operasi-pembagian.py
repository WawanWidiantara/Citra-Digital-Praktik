import cv2
import numpy as np

# membaca gambar
img = cv2.imread("D:/Citra Digital Praktik/5210411135/image/fruit.jpg")
newImg = np.zeros((len(img), len(img[0]), len(img[0][0]))).astype(np.uint8)

pembagi = 4
for i in range(len(newImg)):
    for j in range(len(newImg[0])):
        newImg[i, j] = np.round(img[i, j] / pembagi)

cv2.imshow("original", img)
cv2.imshow(f"bagi {pembagi}", newImg)

cv2.waitKey()
