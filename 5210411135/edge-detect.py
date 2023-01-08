# %% import
import cv2
import numpy as np

# %% read img
img = cv2.imread('D:/Citra Digital Praktik/5210411135/image/fruit.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
row, col = img.shape[:2]

# %% create zeros
newImg = np.zeros(((row, col))).astype(np.uint8)

# %% kernel
laplace1 = np.array([[0,1,0],[1,-4,1],[0,1,0]])
laplace2 = np.array([[1,1,1],[1,-8,1],[1,1,1]])
sobel1 = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
sobel2 = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
prewit1 = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
prewit2 = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])

# %%
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
        
# %% show image
cv2.imshow('ori', img)
cv2.imshow('Deteksi Tepi', newImg)
cv2.waitKey()