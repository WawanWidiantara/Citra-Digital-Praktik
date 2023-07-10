# %% import package
import cv2
import numpy as np

# %% read img
img = cv2.imread('D:\Code\py_code\Citra-Digital-Praktik/responsi\Bunga_Mawar_Merah.jpg')
row, col = img.shape[:2]

# %% soal 2
ratio = 1.5
zrow = round(row * ratio)
zcol = round(col * ratio)
zoomImg = np.zeros(((zrow,zcol,3))).astype(np.uint8)

for i in range(zrow):
    for j in range (zcol):
        zoomImg[i,j] = img[int(i/ratio),int(j/ratio)]

# %% soal 3
kernel = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])
sharpImg = np.zeros(zoomImg.shape).astype(np.uint8)

zpad = np.zeros(((zrow + 2,zcol + 2,3))).astype(np.uint8)
zpad[1:-1, 1:-1] = zoomImg # membuat zero padding menggunakan slicing list

t_kernel = kernel.sum()
if t_kernel == 0:
    t_kernel = 1

for brs in range(1, len(zpad) - 1):
    for klm in range(1, len(zpad[0]) - 1):
        for cn in range(3):
            a = zpad[brs - 1, klm - 1, cn] * kernel[0, 0]    
            b = zpad[brs - 1, klm, cn] * kernel[0, 1]        
            c = zpad[brs - 1, klm + 1, cn] * kernel[0, 2]    
            d = zpad[brs, klm - 1, cn] * kernel[1, 0]       
            e = zpad[brs, klm, cn] * kernel[1, 1]        
            f = zpad[brs, klm + 1, cn] * kernel[1, 2]  
            g = zpad[brs + 1, klm - 1, cn] * kernel[2, 0]
            h = zpad[brs + 1, klm, cn] * kernel[2, 1]    
            i = zpad[brs + 1, klm + 1, cn] * kernel[2, 2]

            konvolusi = np.round((a + b + c + d + e + f + g + h + i) / t_kernel)

            if konvolusi < 0:
                konvolusi = 0

            if konvolusi > 255:
                konvolusi = 255

            sharpImg[brs-1, klm-1, cn] = konvolusi

# %% soal 4
artImg = np.zeros(sharpImg.shape).astype(np.uint8)
add_r = 30
add_g = 20
add_b = 20

for i in range(len(artImg)):
    for j in range(len(artImg[0])):
        for k in range(3):
            if k == 0:
                px = sharpImg[i,j,k] + add_b
            if k == 1:
                px = sharpImg[i,j,k] + add_g
            else:
                px = sharpImg[i,j,k] - add_r
            
            if px > 255:
                artImg[i,j,k] = 255
            elif px < 0:
                artImg[i,j,k] = 0
            else:
                artImg[i,j,k] = px

# %% show image
cv2.imshow('ori', img)
cv2.imshow('zoom 1.5x', zoomImg)
cv2.imshow('sharpening', sharpImg)
cv2.imshow('operasi aritmatik', artImg)
cv2.waitKey()