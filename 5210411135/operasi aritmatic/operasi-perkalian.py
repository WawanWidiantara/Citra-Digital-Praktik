import cv2
import numpy as np

# membaca gambar
img = cv2.imread("D:/Citra Digital Praktik/5210411135/image/fruit.jpg")
newImg = np.zeros((len(img), len(img[0]), 3)).astype(np.uint8)

kali = 4
for i in range(len(newImg)):
    for j in range(len(newImg[0])):
        px = img[i, j] * kali
        if px.any() > 255:
            newImg[i, j] = 255
        else:
            newImg[i, j] = px

cv2.imshow("original", img)
cv2.imshow(f"kali {kali}", newImg)

cv2.waitKey()
