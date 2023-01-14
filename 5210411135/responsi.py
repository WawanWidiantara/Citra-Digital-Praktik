# %% import
import cv2
import numpy as np
import time
import math

# %% flipping
# membaca gambar
img = cv2.imread("D:/Citra Digital Praktik/5210411135/image/fruit.jpg")
cvimg = img.copy()

row, column = img.shape[:2]
newImg = np.uint8(np.zeros((row, column, 3))).astype(np.uint8)

# translasi
hor = False
ver = True

# opencv
cvstart = time.time()
if hor == True:
    cvflip = cv2.flip(cvimg, 1)
if ver == True:
    cvflip = cv2.flip(cvimg, 0)
cv2.imshow("flipping opencv", cvflip)
cvend = time.time()

# manual
mnstart = time.time()
for i in range(len(img)):
    for j in range(len(img[0])):
        if hor == True:
            newImg[i, column - 1 - j] = img[i, j]
        if ver == True:
            newImg[row - 1 - i, j] = img[i, j]
cv2.imshow("flipping manual", newImg)
mnend = time.time()

cv2.waitKey()


# %% scaling
# membaca gambar
img = cv2.imread("D:/Citra Digital Praktik/5210411135/image/fruit.jpg")
cvimg = img.copy()

row, column = img.shape[:2]

# scale
ratio = 1.2
nrow, ncolumn = ((int(row * ratio)), (int(column * ratio)))
newImg = np.uint8(np.zeros((nrow, ncolumn, 3))).astype(np.uint8)

# opencv
cvstart = time.time()
cvscale = cv2.resize(cvimg, (nrow, ncolumn), interpolation=cv2.INTER_AREA)
cv2.imshow("scaling opencv", cvscale)
cvend = time.time()

# manual
mnstart = time.time()
for i in range(nrow):
    for j in range(ncolumn):
        newImg[i, j] = img[round(i / ratio), round(j / ratio)]
cv2.imshow("scaling manual", newImg)
mnend = time.time()

cv2.waitKey()

# %% translasi
# membaca gambar
img = cv2.imread("D:/Citra Digital Praktik/5210411135/image/fruit.jpg")
cvimg = img.copy()

row, column = img.shape[:2]
newImg = np.uint8(np.zeros((row, column, 3))).astype(np.uint8)

# translasi
hor = 20
ver = 20

# opencv
cvstart = time.time()
t = np.float32([[1, 0, hor], [0, 1, ver]])
cvTranslasi = cv2.warpAffine(cvimg, t, (column, row))
cv2.imshow("translasi opencv", cvTranslasi)
cvend = time.time()

# manual
mnstart = time.time()
for i in range(row):
    for j in range(column):
        if (0 <= i + ver < row) and (0 <= j + hor < column):
            newImg[i + ver, j + hor] = img[i, j]
cv2.imshow("translasi manual", newImg)
mnend = time.time()

cv2.waitKey()

# %% rotate
# membaca gambar
img = cv2.imread("D:/Citra Digital Praktik/5210411135/image/fruit.jpg")
cvimg = img.copy()

row, column = img.shape[:2]
newImg = np.zeros(((row,column,3))).astype(np.uint8)

derajat = 45
t = math.radians((derajat))
cos,sin = (math.cos(t), math.sin(t))

cx,cy = (row//2, column//2)

# opencv
cvstart = time.time()
rotM = cv2.getRotationMatrix2D((cx,cy), -derajat, 1)
cvRot = cv2.warpAffine(cvimg, rotM, (column,row))
cv2.imshow('rotate opencv', cvRot)
cvend = time.time()

# manual
mnstart = time.time()
for i in range(row):
    for j in range(column):
        x = round(cx + (i-cx) * cos - (j-cy) * sin)
        y = round(cy + (i-cx) * sin + (j-cy) * cos)
            
        if (0 <= x < row)and(0 <= y < column):
            newImg[i,j] = img[x,y]         
cv2.imshow("ratate", newImg)
mnend = time.time()

cv2.waitKey()

# %% konvolusi
ori = cv2.imread("D:/Citra Digital Praktik/5210411135/image/fruit.jpg")
row, column = ori.shape[:2]

img = np.zeros(((row + 2, column + 2, 3))).astype(np.uint8)
img[1:-1, 1:-1] = ori
prow, pcolumn = img.shape[:2]
newImg = np.zeros(ori.shape).astype(np.uint8)

#  kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) # sharp
kernel = np.array([[1, 2, 1], [1, 4, 1], [1, 2, 1]]) # blur

t_kernel = kernel.sum()
if t_kernel == 0:
    t_kernel = 1
    
for i in range(1, prow - 1):
    for j in range(1, pcolumn - 1):
        for k in range(3):
            mconv = img[i - 1 : i + 2, j - 1 : j + 2, k]
            konvolusi = np.round((mconv * kernel).sum() / t_kernel)
            
            if konvolusi > 255:
                konvolusi = 255
            if konvolusi < 0:
                konvolusi = 0

            newImg[i-1, j-1, k] = konvolusi

cv2.imshow("ori", ori)
cv2.imshow("konvolusi", newImg)
cv2.waitKey()

# %% edge detect
img = cv2.imread('D:/Citra Digital Praktik/5210411135/image/fruit.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
row, col = img.shape[:2]

newImg = np.zeros(((row, col))).astype(np.uint8)

laplace1 = np.array([[0,1,0],[1,-4,1],[0,1,0]])
laplace2 = np.array([[1,1,1],[1,-8,1],[1,1,1]])
sobel1 = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
sobel2 = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
prewit1 = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
prewit2 = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])

for i in range(1, row-1):
    for j in range(1,col-1):
        konv = 0
        for k in range(2):
            if k == 0:
                kernel = prewit1
            else:
                kernel = prewit2
                
            mconv = img[i-1:i+2,j-1:j+2]
            h_konv = abs(np.round((mconv*kernel).sum()))
            
            if konv < 0:
                konv = 0
            if konv > 255:
                konv = 255
            
            konv += h_konv
            
        newImg[i,j] = konv
 
cv2.imshow('ori', img)
cv2.imshow('Deteksi Tepi', newImg)
cv2.waitKey()