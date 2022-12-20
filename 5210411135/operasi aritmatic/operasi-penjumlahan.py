import cv2
import numpy as np

# membaca gambar
img = cv2.imread("D:/Citra Digital Praktik/5210411135/image/fruit.jpg",0)
add = cv2.imread("D:/Citra Digital Praktik/5210411135/image/adddragronfruit.jpg", 0)
newImg = np.zeros((len(img), len(img[0]))).astype(np.uint8)

for i in range(len(newImg)):
    for j in range(len(newImg[0])):
        px = int(img[i,j]) + int(add[i,j])
        if px > 255:
            newImg[i,j] = 255
        elif px < 0:
            newImg[i,j] = 0
        else:
            newImg[i,j] = px
            
cv2.imshow("original", img)
cv2.imshow("add", add)
cv2.imshow("hasil", newImg)

cv2.waitKey()    